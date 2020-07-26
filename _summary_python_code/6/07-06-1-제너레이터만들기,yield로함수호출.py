def generator_range(end):
    n = 0
    while n < end:
        yield n
        n += 1


for i in generator_range(5):
    print(i)
""" 제너레이터 만들기:
이터레이터를 만들었던 것보다 간편하게 함수와 yield 로 제너레이터를 만들 수 있다. 
(for 문 말고 __next__ 메쏘드로도 사용가능)
"""


def upper_words(x):
    for i in x:
        yield i.upper()


words = ['ppap', 'hahaha', 'wow']
for i in upper_words(words):
    print(i)
"""
yield 에서 값을 함수(메쏘드)의 반환값으로도 넘길 수 있다.
위같이 yield 의 동작 방식만 이해하면 이터레이터 보다 훨씬 간단한 구조로 제너레이터를 만들 수 있다.
"""

