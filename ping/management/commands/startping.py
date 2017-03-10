import subprocess
import threading
import time

from django.core.management.base import BaseCommand

from visualization.models import Node

DB_REFRESH_RATE = 60


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._stop2 = threading.Event()

    def stop(self):
        self._stop2.set()

    def stopped(self):
        return self._stop2.isSet()


class Command(BaseCommand):
    help = 'Start the monitoring service'

    @staticmethod
    def extract_latency(ping_process):
        if ping_process.poll() == 0:
            return float(str(ping_process.communicate()[0]).split('/')[4])
        return 0

    @staticmethod
    def ping_node(node_ip, limit=100):
        node_status = Node.objects.get(ip=node_ip).connected
        while True:
            p = subprocess.Popen(['ping', '-c', '1', '-W', str(limit), '-i', '0.1', node_ip], stdout=subprocess.PIPE)
            time.sleep(1)
            success = p.poll() == 0
            p.kill()
            if node_status != success:
                node_status = success
                node = Node.objects.get(ip=node_ip)
                node.connected = success
                node.save(update_fields=['connected'])
            if threading.current_thread().stopped():
                return

    def handle(self, *args, **options):
        while True:
            all_threads = []
            for node in Node.objects.all():
                thread = StoppableThread(target=self.ping_node, args=(node.ip,))
                thread.start()
                all_threads.append(thread)
            time.sleep(DB_REFRESH_RATE)
            for thread in all_threads:
                thread.stop()
            for thread in all_threads:
                thread.join()