"""
블로그포스팅 : https://bodhi-sattva.tistory.com/61
"""

b1 = True
b2 = False
print(b1, type(b1), b2, type(b2))
"""불 자료형:
불은 bool 으로, 2진수처럼 참 또는 거짓, 1 또는 0, True 또는 False 를 가진다.
이거 자체로 if 나 while 문의 조건식에 넣을 수도 있다.
근데 불 자료형을 쓰지않아도 참과 거짓이 이미 구분되어 있는데,
[], (), {}, 0, "", None 같은 것은 자료형에서 비여있는 형태로 거짓으로 인식하고,
반대로 비여있지 않거나, 0이 아닌 값을 가지면 참으로 인식한다.
bool()함수의 인자로 값을 넘기면, 그 값이 참또는 거짓으로 인식하는지 판별할 수 있다.

그리고 이러한 불 자료형으로 반환되는게, 비교, 논리연산자다.
(연산자들을 별개로 묶어서 코드를 분할했다.)
"""
print(bool([]), bool({}), bool(0), bool(""), bool(None))
print(bool([1]), bool({1}), bool(-3), bool("wow"), bool(0.1))

print(not None)
