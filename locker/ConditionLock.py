




import threading
import time
from time import sleep

current_time = ""

class Zhou(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="周杰伦")
        self.cond = cond
                 
    def run(self):
        global current_time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with self.cond:
            # Condition()对象中也实现了__enter__()与__exit__()魔法方法，所以也是可以通过 with 语句调用的
            print("[{}]{}: 海平面远方开始阴霾, 悲伤要怎么平静纯白".format(current_time, self.name))
            self.cond.notify()
            self.cond.wait()

            print("[{}]{}: 你用唇语说你要离开, 那难过无声慢了下来 ".format(current_time, self.name))
            self.cond.notify()
            self.cond.wait()

            print("[{}]{}: 转身离开, 你有话说不出来 ".format(current_time,self.name))
            self.cond.notify()
            self.cond.wait()

            print("[{}]{}: 我们的爱, 差异一直存在, 等待竟累积成伤害 ".format(current_time,self.name))
            self.cond.notify()
            self.cond.wait()

            print("[{}]{}: 蔚蓝的珊瑚海, 错过瞬间苍白 ".format(current_time,self.name))
            self.cond.notify()
            self.cond.wait()

            print("[{}]{}: 热情不再, 笑容勉强不来, 爱深埋珊瑚海".format(current_time,self.name))
        
                         


class Liang(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="梁心颐")
        self.cond = cond
        
    def run(self):
        global current_time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with self.cond:
            # 在调用with cond 之后才能调用 wait 或者 notify 方法
            self.cond.wait()
            print("[{}]{}: 我的脸上始终挟带, 一抹浅浅的无奈".format(current_time,self.name))
            self.cond.notify()

            self.cond.wait()
            print("[{}]{}: 汹涌潮水, 你听明白, 不是浪而是泪海 ".format(current_time,self.name))
            self.cond.notify()

            self.cond.wait()
            print("[{}]{}: 海鸟跟鱼相爱, 只是一场意外 ".format(current_time,self.name))
            self.cond.notify()

            self.cond.wait()
            print("[{}]{}: 转身离开, 分手说不出来 ".format(current_time,self.name))
            self.cond.notify()

            self.cond.wait()
            print("[{}]{}: 当初彼此, 不够成熟坦白".format(current_time,self.name))
            self.cond.notify()
                         


if __name__ == "__main__":
    cond = threading.Condition()
    liang = Liang(cond)
    zhou = Zhou(cond)
    # 这里的启动顺序很重要
    liang.start()
    zhou.start()