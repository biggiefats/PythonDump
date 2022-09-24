import time


def timestuff():

    h = 0
    m = 0
    s = 0

    while True:

        def timer():
            if h == 0 and m == 0:
                print('00 : ', '00 : ', s)

            elif h == 0 and m != 0:
                print('00 : ', m, ' : ', s)

            else:
                print(h, ' : ', m, ' : ', s)

        if s / 60 == 1:
            s = 0
            m += 1

        elif m / 60 == 1:
            m = 0
            h += 1

        elif h / 24 == 1:
            h = 0

        else:
            s += 1
            time.sleep(1/10)
            timer()
            continue


timestuff()
