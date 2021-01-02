it = iter(range(3))
print(next(it), next(it), next(it))

"""
iter() 함수와 next() 함수는 기본적으로 객체의 __iter__, __next__ 메쏘드를 호출한다.
하지만 이런 기능이외에도 다양한 방식으로 활용할 수 있다.
"""

import random

it = iter(lambda: random.randint(0, 5), 2)
print(next(it))     # 랜덤으로 0 ~ 5 중 반환한 값이 2일 경우 반복멈춤(에러 발생)
"""
iter(반복가능한객체) 말고
iter(호출가능한객체, 반복을 끝낸 값)
과 같은 방법으로 iter() 를 쓸 수 있다. 호출가능한 객체(함수같이)를 넣어서 반환되는 값이 반복을 끝낸 값이면
반복을 끝낸다. (반복을 끝낼 값은 sentinel(감시병)이라 부른다. (반환되는 값을 감시하고 걸리면 반복을 끝내서) )

이렇게 하면 if 조건문으로 검사하는 코드를 간단하게 요약할 수 있다.
"""

it = iter(range(2))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
"""
next(반복가능한객체, 기본값)
으로 반복이 끝났을 때 대신 출력할 기본값을 지정할 수 있다.
이터레이터에서 반복이 끝나면 에러가 나는 것이 아니라 기본값을 반환해서 에러를 막을 수 있다.
"""
