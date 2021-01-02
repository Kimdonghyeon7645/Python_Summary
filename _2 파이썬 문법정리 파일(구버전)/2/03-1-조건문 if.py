a, b = map(int, input("a와 b를 입력하세요: ").split(' '))
if a > b:
    print(a*b)
else:
    print(b-a)
""" if else:
조건문은 c언어 처럼 if 문을 사용할 수 있다. switch case 문은 없다. 
(대신에 딕셔너리(dic)을 사용한 함수로 구현가능하다.)
추가로 else if 문은 파이썬에서 elif 로 표현한다.
"""
