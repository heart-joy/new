import time

def show_progress(total, current):
    progress = current / total
    bar_length = 20
    filled_length = round(progress * bar_length)
    empty_length = bar_length - filled_length
    bar = '=' * filled_length + ' ' * empty_length
    print(f'[{bar}] {current}/{total}', end='\r')

total = 100
for i in range(1, total+1):
    show_progress(total, i)
    time.sleep(0.1)  # 暂停0.1秒
print("\n进度条动画结束")
