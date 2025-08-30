class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        print(f"starting thread {self.name}")
        task(self.name, self.number, self.char)
        print(f"exiting thread {self.name}")