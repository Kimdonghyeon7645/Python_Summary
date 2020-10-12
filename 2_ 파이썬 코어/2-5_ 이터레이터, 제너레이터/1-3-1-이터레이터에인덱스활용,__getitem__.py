class iter_name:
    def __init__(self, stop):
        self.end = stop
        self.current = 0

    def __getitem__(self, index):
        if index < self.end:
            return index
        else:
            raise IndexError

print(iter_name(5)[0], iter_name(5)[4])

for i in iter_name(5):
    print(i, end=' ')

"""
이터레이터에 인덱스도 활용할 수 있게도 직접 만들수 있다.
__getitem__ 메쏘드를 활용해서, 전달받은 인덱스 값을 출력하게 할 수 있다.

__getitem__ 메쏘드를 사용한다면, __iter__, __next__ 메쏘드를 생략해도 이터레이터를 만들 수 있다.
(그래서 위같이 for 문에 넣어서 이터레이터를 사용할 수 있다.)
"""
