import threading
import time
from time import sleep

class MyThread(threading.Thread):
    def __init__(self, number, char):
        threading.Thread.__init__(self)
        self.number = number
        self.char = char
        self.daemon = True

    def run(self):
        print(f"starting thread {self.name}")
        task(self.name, self.number, self.char)
        print(f"exiting thread {self.name}")
    
def task(threadName, number, char):
    while number > 0:
        sleep(1)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"[{current_time}]{threadName}: {char}")
        number -= 1
        
thread1 = MyThread(4,'A')
thread2 = MyThread(2,'B')

thread1.start()
thread2.start()

time.sleep(5)
