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
