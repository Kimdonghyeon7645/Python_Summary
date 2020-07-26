# for x1, x2, y in [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]:
#     print(x1, x2, '|', y)
# """
# == for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
#        print(x1, x2, '|', x1 and x2)
# 의 코드로도 같은 실행 결과를 볼 수 있다. (리스트 안의 값이 두 변수의 and 연산 결과를 가지고 있다.)
# """
test = [[1, 2], [3, 4], [5, 6]]
print([n2-n1 for n1, n2 in test])
"""리스트내포 심화:
위처럼 리스트내포로 한번에 여러값을 받을 수 있는 것쯤은 알것이다.
이건 아까 했던 거니까 그렇다 치고, 이젠 더 고급지게, 리스트 내포를 이중으로도 해보자.
"""

print([x*y for x in range(1, 10) for y in range(1, 10)])  # 이렇게 구구단의 모든 출력 내용을 파이썬에선 한줄로 소화해낼 수 있다.
# 위의 한줄이 아래 세줄 코드와 동일하다.
# for y in range(1, 10):
#     for x in range(1, 10):
#         print(x*y, end=' ')
"""이중 리스트내포:
말그대로, 이중 for 문처럼, for 문을 연달아서 두번 사용하는 것이다.
이 상황에서 오른쪽의 for 문이 바깥 반복문이고, 왼쪽의 for 문이 안쪽 반복문이다.
물론 여기서도 if 문을 혼합할 수 있다.
"""

print([x*y for x in range(1, 10) if x is not 1 for y in range(1, 11) if y is not 10])
"""
여기서 if 문은 자신의 왼쪽에 위치한 for 문에 속해있는 것같다. 
if 문까지 들어가니까 좀 보기 어려워 졌는데...
"""

print([x+y+z for x in range(1, 11) for y in range(1, 11) for z in range(1, 11)])
print([x+y+z+a for x in range(1, 11) for y in range(1, 11) for z in range(1, 11) for a in range(1, 11)])
print([x+y+z for x in range(1, 11) if x is not 10
       for y in range(1, 11) if y is not 10
       for z in range(1, 11) if z is not 10])
"""
삼중, 사중 리스트도 가능하고, 한술 더떠서 if 문을 넣는것도 된다.
이정도 되니까 한줄로 가독성좋던 리스트 내포가 복잡해졌다.
다중 리스트에서는 for 문 단위로 끊어주는 센스가 필요할 것 같다.
"""
print([a+b+c+d+e+f+g+h+i+j+k+l+m+n+o for a in range(1, 3) for b in range(1, 3) for c in range(1, 3) for d in range(1, 3)
       for e in range(1, 3) for f in range(1, 3) for g in range(1, 3) for h in range(1, 3) for i in range(1, 3)
       for j in range(1, 3) for k in range(1, 3) for l in range(1, 3) for m in range(1, 3) for n in range(1, 3)
       for o in range(1, 3)])
"""
근데 다중리스트에도 끝이 있을까? 15중첩 리스트내포까지 갔는데도 멀쩡하다. 슬슬 무서워 지는것 같아서 여기까지만 하고 그만둬야 겠다.
"""