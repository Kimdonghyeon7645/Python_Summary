class iter_name:
    def __init__(self, stop):
        self.current = 0
        self.end = stop


    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


for i in iter_name(5):
    print(i, end=' ')
"""
클래스와 스페셜 메쏘드 __iter__, __next__ 를 사용해서 직접 이터레이터 객체를 만들 수 있음,
(__init__ 로 이터레이터 객체를 생성하고, __iter__, __next__ 메쏘드에 원하는 기능을 추가해서 
마치 iter_name(n) 이 range(0, n)과 같은 기능을 하게 함.)
"""

a, b, c = iter_name(3)
print(a, b, c)

a, b = range(2)
print(a, b)     # 반복가능한 객체도 언패킹되는 것처럼,

a, b = range(2).__iter__()
print(a, b)     # 이터레이터도 언패킹할 수 있다.
""" 이터레이터 언패킹: 
이터레이터도 반복가능한 객체와 마찬가지로 언패킹(하나의 반복가능한 객체 -> 여러개의 요소를 각각의 변수에 대입)할 수 있다.
(자세한 언패킹, 패킹은 2폴더 17-2 참고)

물론 언패킹할 때의 규칙(이터레이터가 반복하는 횟수 == 변수의 개수)은 동일하며,
사실 map() 함수도 이터레이터 였기에 언패킹이 가능했던 거임.
(ex> a, b, c = map(int, input().split()) )


*** 참고로 언패킹할 때 변수이름으로 _(언더 스코어, 언더바)를 사용하는 경우가 있는데,
_에 할당하는 것은 _에 할당되는 반환 값은 나중에 사용하지 않고 무시하겠다는 관례적 표현임.
"""
a, _, c, _ = range(4)   # ex> 여기서 두번째, 네번째 변수는 사용하지 않겠다는 의미.
print(a, c)
