import time, datetime, random

while True:
    time.sleep(random.randint(1, 5))
    t = datetime.datetime.now()     # == int(time.time)
    print(t.second, '초 - ', sep='', end='')
    if t.second %2 == 0:
        print("짝수second")
    else:
        print("홀수second")