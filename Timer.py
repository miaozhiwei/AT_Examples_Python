import threading


def timer_check():
    print('hello')

    # 因为定时器构造后只执行1次，必须循环调用。
    global timer
    timer = threading.Timer(2, timer_check)
    timer.start()


def timer_check2():
    print('hello2')

    # 因为定时器构造后只执行1次，必须循环调用。
    global timer2
    timer2 = threading.Timer(2, timer_check2)
    timer2.start()

# 首次和循环的时间可以不一致，可以一致。
timer = threading.Timer(10, timer_check)
timer.start()

timer2 = threading.Timer(10, timer_check2)
timer2.start()
