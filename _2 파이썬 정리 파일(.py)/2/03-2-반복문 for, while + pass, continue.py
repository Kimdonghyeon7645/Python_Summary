for i in range(1, 10):
    print(i)
"""반복문:
반복문으로는 while 문과 for 문이 있다. 
for 문은 유용하고 구조도 보기쉬운데, 여기서 같이 쓰이는 함수가 range 다.
for i in [1,2,3]:
과 같은 코드는 []같은 iterable(반복가능한 객체)의 요소(1, 2, 3)를 처음부터 끝까지 i라는 변수로 뽑아내면서 for 문의 실행문을 반복한다.
여기서 리스트 요소를 간편하게 range()함수를 사용해서 나타낼 수 있다. 
"""
j = 0
while j <= 10:
    print(j)
    j += 1
"""
while 문도 있는데, c언어 에서와 같다.
그리고 반목문과 조건문에서 쓰이는 예악어들도 있는데, break, continue 추가로 pass 도 있다.
break 는 가까운 반복문을 탈출 하고,
pass 와 continue 모두 아래 실행문을 무시하고 건너뛰는데, 이때 둘의 차이점은
pass 는 다음 루프를 실행시키지 않지만, continue 는 다음 루프로 넘어간다.
"""
n = 0
while True:
    n += 1
    if n > 5:
        print("break!")
        break
    print(n)
# break 문

pas = True
for i in range(1, 3):
    if pas:
        print("pass 전 i값: ", i)    # -> 1
        pas = False
        pass
    print("pass 후 i값: ", i)    # -> 1
    break
# pass 문

con = True
for i in range(1, 3):
    if con:
        print("continue 전 i값: ", i)    # -> 1
        con = False
        continue
    print("continue 후 i값: ", i)    # -> 2
    break
# continue 값




