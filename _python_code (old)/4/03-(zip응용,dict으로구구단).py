n = int(input("원하는 단의 숫자를 입력하세요: "))
y = dict(zip(range(1, 11), [n*i for i in range(1, 10)]))
for x in y:
    print(f"{n} * {x} = {y[x]}")

"""zip함수 dict응용해서 구구단 출력:
input으로 원하는 숫자를 입력해서, 그 숫자의 구구단을 출력하는 프로그램
"""
