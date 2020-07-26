name = ['kim', 'dong', 'hyeon']
age = [19, 31, 26]

for n, a in zip(name, age):
    print(n, a)
    print(type(n), type(a))

"""zip() 내장함수:
zip()함수는 요소의 개수가 동일한 인자들을 전달받아서, (인자로는 반복가능한 객체)
인자들를 인덱스별로 쪼개서 같은 인덱스끼리 튜플로 묶어서 zip객체로 반환한다.

list(), tuple()로 묶어서 리스트, 튜플 자료형으로 반환 할수 있다.
"""
