# 직접 예외 처리 만들기
class KimDongError(Exception):
    pass


try:
    word = input()
    if word == 'kimdong':
        raise KimDongError('오류입나이다')
except KimDongError as e:
    print(e)

""" 사용자 정의 예외:
파이썬에는 내장된 함수가 있으면 사용자 정의 함수가 있듯이,
내장된 예외(지금까지 사용했던 예외)가 있으면 사용자 정의 예외도 있다.

사용자 정의 예외는 클래스에 Exception 을 상속받아서 만들 수 있으며,
에러이름은 클래스의 이름이며,
에러메시지는 

raise 에러이름("에러메시지")
로 raise 문에서 에러메시지를 넣을 수도 있고,
에외 class의 __init__ 안에서 

super().__init__("에러메시지")
로 예외 class 부모클래스(Exception)의 __init__ 메쏘드를 호출하면서 인자값으로 에러 메시지를 넣어 줄수도 있다.
"""


class KimSeungError(Exception):
    def __init__(self):
        super().__init__("김승현에러다!으악!")


try:
    word = input()
    if word == 'kimseung':
        raise KimSeungError
except KimSeungError as e:
    print(e)