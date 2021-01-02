y = dict(zip(range(1, 11), [2**i for i in range(1, 11)]))
for x in y:
    print(f"{x} - {y[x]}")  # x = 키, y = 전체딕셔너리객체, y[x] = 값

"""zip함수 dict응용 2:
마찬가지로 zip함수로 딕셔너리 자료형을 만들어서, 
그 키와 값을 출력하는 코드다.
"""
