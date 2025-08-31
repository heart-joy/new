class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        print(f"starting thread {self.name}")
        lock.acquire()
        task(self.name, self.number)
        lock.release()

