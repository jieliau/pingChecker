import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print("Thread: ", self.num)
        time.sleep(1)

threads = list()
for i in range(5):
    threads.append(MyThread(i))
    threads[i].start()

for i in range(5):
    threads[i].join()

print("Done")
