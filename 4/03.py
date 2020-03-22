n = int(input("원하는 단의 숫자를 입력하세요: "))
y = dict(zip(range(1, 11), [n*i for i in range(1, 10)]))
for x in y:
    print(f"{n} * {x} = {y[x]}")