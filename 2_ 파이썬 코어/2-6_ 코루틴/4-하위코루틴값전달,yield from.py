def gogo_coroutine():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total
        total += x


def load_coroutine():
    while True:
        x = yield from gogo_coroutine()
        print(x)


co = load_coroutine()
next(co)
co.send(1)
co.send(2)
co.send(3)
co.send(None)
"""
yield 도 쓸수 있듯이 yield from 도 쓸 수 있는데,
제너레이터 처럼, 반복가능한 객체등을 반환할 때 쓰는 것이 아니라, 코루틴 바깥에서 하위 코루틴을 잇는 역할로 쓴다.

yield from 코루틴()
을 사용한다면 코루틴 바깥과 yield from 뒤의 코루틴과를 연결시키고, 값을 주고 받을 수 있게 한다.
따라서 코루틴 바깥에서 값을 주면 yield from 코루틴() 으로 하위 코루틴으로 받은 값이 고스란히 전달되고,

반대로 하위 코루틴에서 반환한 값을 yield from 코루틴() 에서 전달받아서, 코루틴 바깥으로 전달 할 수 있다.
정말 하위 코루틴과 코루틴 바깥에서 오고가는 값을 사이에서 연결해주는 느낌이다.


전에서 설명했듯이 코루틴도 제너레이터여서, return 을 사용했을 때 제너레이터처럼 StopIteration 예외가 발생한다.
그걸 이용해 파이썬 3.6이하 까지는 raise StopIteration(값)으로 return 값 과 같은 효과를 낼 수 있다.

대신에 파이썬 3.7부터는 raise StopIteration() 해도 RuntimeError 로 바뀌기 때문에 사용할 수 없다.
"""

