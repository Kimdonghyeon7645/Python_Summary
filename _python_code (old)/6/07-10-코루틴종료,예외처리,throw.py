def good_corotin():
    while True:
        print((yield), end=' ')


coro = good_corotin()
coro.send(None)

for i in range(10):
    coro.send(i)

coro.close()
print()
"""
코루틴은 보통 실행 상태가 유지되게 무한루프를 사용하는데, 코루틴을 만약 강제로 종료한다면, .close() 메쏘드를 이용함.
(사실 close() 메쏘드를 사용하지 않아도 코루틴은 파이썬 스크립트가 끝나면 같이 끝남.)
이를 활용해 코루틴의 종료 시점을 코드로 표현할 때 사용할 수 있음.

코루틴이 close() 로 종료된다면 코루틴에선 GeneratorExit 예외가 발생하는데,

이 예외를 try except 문으로 처리해서 코루틴의 종료 시점에 원하는 코드를 실행할 수 있음.
"""


def haha_corotin():
    try:
        while True:
            print((yield), end=' ')
    except GeneratorExit:       # 코루틴이 종료될 때 이 예외가 발생
        print("\n코루틴 종료")


co = haha_corotin()
co.send(None)

for i in range(10):
    co.send(i)

co.close()
"""
위같이 하면 코루틴이 종료될 때 코루틴 종료가 출력되게 함.

또한 일부러 예외를 발생 시킬수도 있는데, throw() 메쏘드를 사용함.

코루틴객체.throw(예외이름, 에러메시지)
같이해서 코루틴 바깥에서 에러를 코루틴 안으로 던질 수 있으며, 이렇게 해서 코루틴을 종료시킬 수도 있음.
"""


def no_more_corotin():
    sum = 0
    try:
        while True:
            x = (yield)
            print(x, '가 누적')
            sum += x
    except IndexError as e:
        print(e)
        yield sum


cr = no_more_corotin()
next(cr)

cr.send(1)
cr.send(3)
cr.send(2)
print("누적된 값 :", cr.throw(IndexError, "갑자기 분위기 에러"))
"""
위같이 해서 코루틴을 throw 로 예외를 만들게 하고, 예외 처리에서 예외를 만날 때 값도 반환하고 에러메시지도 출력하게 함.
"""