import time
import threading
import queue

class Worker(threading.Thread):
    def __init__(self, queue, num, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num
        self.lock = lock

    def run(self):
        while self.queue.qsize() > 0:
            msg = self.queue.get()

            lock.acquire()
            print("Lock acquired by Worker %d" % self.num)

            print("Worker %d: %s" % (self.num, msg))
            time.sleep(1)

            print("Lock released by Worker %d" % self.num)
            self.lock.release()

my_queue = queue.Queue()
for i in range(5):
    my_queue.put("Data %d" % i)

lock = threading.Lock()

my_worker1 = Worker(my_queue, 1, lock)
my_worker2 = Worker(my_queue, 2, lock)

my_worker1.start()
my_worker2.start()

my_worker1.join()
my_worker2.join()

print("Done!!!")
