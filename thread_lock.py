import threading
import time
from time import sleep


class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        print(f"starting thread {self.name}")
        lock.acquire()
        task(self.name, self.number)
        lock.release()

    def _del_(self):
        print(f"exiting thread {self.name}")
        
def task(threadName, number):
    while number > 0:
        sleep(1)
        data_list[number-1] += 1
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"[{current_time}]{threadName}: {number}\n")
        number -= 1
    print(f"thread {threadName} finished")
    
lock = threading.Lock()
data_list = [0,0,0,0]

thread1 = MyThread(1)
thread2 = MyThread(2)
thread3 = MyThread(3)

thread1.start()
thread2.start()
thread3.start() 

thread1.join()
thread2.join()
thread3.join()

print("all threads finished")