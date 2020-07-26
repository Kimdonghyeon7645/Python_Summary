data = [1, 2, 3, 4]
print(data, [n+1 for n in data], [n for n in data if n % 2 is 0], sep='\n', end="\n"*2)
""" 리스트 내포:
리스트 컴프리헨션(list comprehension), 리스트 내장, 리스트 축약, 리스트 해석이라고도 하는데, 
리스트 안에 for 반복문이나 if 조건문을 사용하는 파이썬만의 리스트 표현식이다.

* [n+1 for n in data]
for 반복문을 복습하자면, 반복되는 여러가지 요소들(data)에서 요소를 하나하나 차례대로 변수(n)에 가져와서 반복문 아래서 쓰는 과정이였는데,
리스트 내포는 요소들에서 가져온 요소가 있는 변수(n)을 맨 앞에 위치시켜 반환한다. 이때 n에 산술연산을 덧붙이면, 변환된 상태로 반환된다(n+1). 
반환된 요소들이 모여서 리스트가 만들어진다.

* [n for n in data if n % 2 is 0]
for 문으로 data 를 가져와 차례대로 n 변수에 가져오는 것은 동일한데, if 조건문 뒤에 붙은 조건식이 거짓이면 반환하지 않고 참인 경우에만 반환한다.
반환된 요소들끼리 리스트가 만들어지는 것이다.
"""

print([n for n in [1, 2, 3]], [n for n in (1, 2, 3)], [n for n in range(1, 4)], [n for n in "123"], sep='\n')
print([n for n in {1: '일', 2: '이', 3: '삼'}], [n for n in {1, 2, 3}], sep='\n')

print([i for i in enumerate([1, 2, 3])], [i+n for i, n in enumerate([1, 2, 3])], sep='\n')
"""
range()함수를 활용해도 좋고, 기타 군집자료형들을 활용해도 된다. (딕셔너리는 역시 키 값이 차례대로 반환된다)
enumerate()함수같이 인덱스와 값을 묶어 튜플로 반환하는 경우도 된다. 두 변수로 전달받아 활용해도 된다.
"""
