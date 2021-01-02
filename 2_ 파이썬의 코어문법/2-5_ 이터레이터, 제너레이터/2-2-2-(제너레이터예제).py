def prime_number_generator(s, l):
    for i in range(s, l):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                yield i


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
"""
제너레이터를 사용해서 시작 숫자와 끝 숫자를 입력받아, 그 수 사이의 소수들을 출력하는 예제.
"""
