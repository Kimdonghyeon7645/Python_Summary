"""
블로그링크 : https://bodhi-sattva.tistory.com/81
"""
s1 = {1, 2, 1}
s2 = {}
s3 = set([1, 2, 3])
s4 = set()
s5 = set('ppap')
print(s1, s2, s3, s4, s5)
print(type(s1), type(s2), type(s3), type(s4), type(s5))  # 여기중에 스파이가 껴있다. 바로 s2
"""집합(set):
집합자료형은 수학에서 처럼 중복이 안되고, 순서도 정해져있지 않다.
테두리가 {}으로 되어있으며, 생성때 중복되는 값을 해도 하나로 들어간다.(중복이 자동으로 짤린다)
set() 함수로 군집자료형(여러개 값들)을 집합자료형으로 변환할 수 있다.
참고로 생성할 때 {}같이 하면, 같은 테두리를 쓰는 dic 자료형이 된다... 따로 집합자료형의 빈 상태를 만들려면 set()을 사용해야된다.

순서가 없어서 인덱싱과 슬라이싱은 못한다.(가능한 자료형으로 변환후 사용할 수 밖에)
"""
fs1 = frozenset([1, 2, 3])
fs2 = frozenset(s1)
print(fs1, type(fs1))
print(fs2, type(fs2))

"""frozenset(읽기전용집합):
frozenset은 집합중 읽기전용 집합으로, 집합자료형(set)과 성질이 똑같지만,
frozenset()함수로 선언할 수 있고, 읽기전용이기에 요소의 수정, 삭제가 불가능하다.
그 이외에는 set자료형과 같게 사용할 수 있다.
"""
s01 = {1, 2}
s02 = {2, 3}
print(s01 & s02, s01 | s02, s01 - s02, s01 ^ s02)
"""집합 연산:
집합자료형답게 교집합(논리곱), 합집합(논리합), 차집합 연산을 할 수 있다. (and, or 는 여기서 못 쓴다)
대칭차집합 연산(^)이라고(합집합 - 교집합) 두집합에서 안겹치는 것들의 집합도 구할 수 있다. 

추가로 집합연산 + 대입연산의 형태인 집합복합대입연산자? 도 가능하다.
다시말해, &=, |=, -=, ^= 가 가능하다.
또한 부분집합과 진부분집합도 연산자가 있는데, 부분집합은 >=, <= 기호, 진부분집합은 >, < 기호를 이용하면 된다. 
"""

print(s01.intersection(s02), s01.union(s02), s01.difference(s02), s01.symmetric_difference(s02))
"""집합 함수:
이러한 집합연산은 집합함수로도 연산할 수 있다.
.intersection() 교집합 함수, .union() 합집합 함수, <빼기전집합>.difference(<빼는집합>) 차집합 함수와
.symmetric_difference() 대칭차집합 함수를 사용해서 똑같은 결과를 낼 수 있다.
 .issubset()와 .issuperset() 부분집합 함수도 이와 같다.
 그외의 함수는...
"""

temp_s = {1, 2, 3}
temp_s.add(4)
print(temp_s)
''' .add() 함수: 요소 한개를 전달받아 집합에 추가'''
temp_s.update([5, 6, 7])
print(temp_s)
''' .update() 함수: 요소 여러개를 전달받아 집합에 추가'''
temp_s.remove(7)
temp_s.discard(6)
print(temp_s)
''' .remove() .discard() 함수: 요소를 집합에서 삭제
.discard() 함수도 똑같은 일을 수행하는데, 차이점은 remove()는 삭제할 요소가 없으면 에러를 발생시키고 discard()는 그러지 않는다.
'''
a = {1, 2, 3}
b = {1, 2}
print(a.issubset(b))
''' .issubset() 함수: 대상집합(.앞의 집합)에 대해 인자값(괄호안 집합)이 부분집합인지 참 거짓으로 반환'''
print(a.issuperset(b))
''' .issuperset() 함수: 인자값에 대해 대상집합이 부분집합인지 참 거짓으로 반환
(a.issubset(b) == b.issuperset(a) )
'''
print(a.isdisjoint(b))
''' .isdisjoint() 함수: 두 집합에서 교집합이 없는지 참 거짓으로 반환'''


