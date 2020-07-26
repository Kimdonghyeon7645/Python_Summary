class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(t_str):
        h, m, s = map(int, t_str.rstrip().split(':'))
        if 25 > h >= 0 and 60 > m >= 0 and 60 >= s >= 0:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, t_str):
        h, m, s = map(int, t_str.rstrip().split(':'))
        t = cls(h, m, s)
        return t


time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

""" 파이썬 코딩도장 35.6 심사문제:
정적메쏘드와 클래스 메쏘드를 활용한 예제,
어렵진 않아도 문법과 개념을 까먹었으면 난감한 좋은 예제여서 추가함.
"""