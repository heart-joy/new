import threading
import time

num = 0

def add():
    lock.acquire()
    global num
    for i in range(1000000):
        num += 1
    lock.release()
    
#def add():
#    with lock: withlock语句块结束会自动释放锁
#       global num
#       for i in range(1000000):
#           num += 1

def sub():
    lock.acquire()
    global num
    for i in range(1000000):
        num -= 1
    lock.release()
    
    
lock = threading.Lock()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()

t1.join()
t2.join()