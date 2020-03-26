# 직접 예외 처리 만들기
class KimDongError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    word = input()
    if word == 'KimDong':
        raise KimDongError('오류입나이다')
except KimDongError as e:
    print(e)