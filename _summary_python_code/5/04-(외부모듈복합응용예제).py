import time
import datetime
import random

while True:
    time.sleep(random.randint(1, 5))
    t = datetime.datetime.now()     # == int(time.time)
    print(t.second, '초 - ', sep='', end='')
    print("짝수 초" if t.second % 2 == 0 else "홀수 초")


# random, time, calendar 모듈 3개를 모두 활용한 예제 프로그램
