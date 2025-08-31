import threading
import time

num = 0

def add():
    global num
    for i in range(1000000):
        num += 1

def sub():
    global num
    for i in range(1000000):
        num -= 1
        
if __name__ == "__main__":
      t1 = threading.Thread(target=add)
      t2 = threading.Thread(target=sub)

      t1.start()
      time.sleep(2)
      t2.start()

      t1.join()
      t2.join()

      print(f"current_num: {num}")