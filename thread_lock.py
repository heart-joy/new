import threading
import time
from time import sleep
from classlibrary import MyThread

def task(threadName, number):
    while number > 0:
        sleep(1)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"[{current_time}]{threadName}: {number}/n")
        number -= 1
    print(f"exiting thread {threadName}")
    
lock = threading.Lock()
data_list = [0,0,0,0]

thread1 = MyThread(1)
thread2 = MyThread(2)
thread3 = MyThread(3)