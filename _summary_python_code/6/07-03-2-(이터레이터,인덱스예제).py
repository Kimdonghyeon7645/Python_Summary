def time_break(t):
    s = t % 60
    t //= 60
    m = t % 60
    t //= 60
    h = t % 24
    if t // 24 > 0:
        h = 0
    return f'{h:02}:{m:02}:{s:02}'


class TimeIterator:
    def __init__(self, start, stop):
        self.s = start
        self.l = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.s < self.l:
            r = self.s
            self.s += 1
            return time_break(r)
        else:
            raise StopIteration

    def __getitem__(self, item):
        if 0 <= item < self.l:
            return time_break(self.s + item)
        else:
            raise IndexError


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
"""
이터레이터를 사용해서, 처음 시간과 끝 시간까지를 시:분:초 형식으로 출력하는 프로그램

입력받는 값이 3가지인데 start = 처음 시간(초단위), stop = 끝 시간(초단위), index = 특정시간(인덱스번호)
"""

