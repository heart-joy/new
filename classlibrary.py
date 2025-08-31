class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        print(f"starting thread {self.name}")
        lock.acquire()
        task(self.name, self.number)
        lock.release()

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