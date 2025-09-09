import threading

lock = threading.RLock()
num = 0

def add():
    global num
    for i in range(1000000):
      lock.acquire()
      lock.acquire()
      num += 1
      lock.release()
      lock.release()

def sub():
    global num
    for i in range(1000000):
      lock.acquire()
      lock.acquire()
      num -= 1
      lock.release()
      lock.release()

if __name__ == "__main__":
    num = 0
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num)