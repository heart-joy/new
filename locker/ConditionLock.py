import threading
import time
from time import sleep

current_time = ""
line1 = ["海平面远方开始阴霾, 悲伤要怎么平静纯白","你用唇语说你要离开, 那难过无声慢了下来","转身离开, 你有话说不出来","我们的爱, 差异一直存在, 等待竟累积成伤害",
        "蔚蓝的珊瑚海, 错过瞬间苍白","热情不再, 笑容勉强不来, 爱深埋珊瑚海"]
line2 = ["我的脸上始终挟带, 一抹浅浅的无奈","汹涌潮水, 你听明白, 不是浪而是泪海","海鸟跟鱼相爱, 只是一场意外","转身离开, 分手说不出来"," 当初彼此, 不够成熟坦白"]

class singer(threading.Thread):
    def __init__(self, cond, name, lines):
        super().__init__(name = name)
        self.cond = cond
        self.lines = lines
                 
    def run(self):
        global current_time
        with self.cond:
            for line in self.lines:
                self.cond.notify()            # 通知对方
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"[{current_time}]{self.name}: {line}")
                self.cond.wait()

if __name__ == "__main__":
    cond = threading.Condition()
    liang = singer(cond, "梁静茹", line1)
    zhou = singer(cond, "周杰伦", line2)
    # 这里的启动顺序很重要
    liang.start()
    zhou.start()