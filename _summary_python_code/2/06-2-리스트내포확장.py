print("딕셔너리내포")
print({k*2: v*3 for k, v in {1: 1, 2: 2, 3: 3}.items()})
print({v: k for k, v in {1: '값', 2: '값2', 3: '값3'}.items()})   # 키와 값을 뒤집어서 응용 할 수도 있다.
print({0: value for value in {1: '1', 2: '2', 3: '3'}.values()})     # 참고로 딕셔너리 내포에서 반복되는 값을 값으로 해도, 값은 1개만 들어간다.
print({value: 0 for value in {1: '1', 2: '2', 3: '3'}.values()})
print({key: 0 for key in {1: '1', 2: '2', 3: '3'}.keys()})

print("집합내포")
print({n for n in 'ppap!'})
print({n for n in 'ppap!' if n is not '!'})

print("튜플내포")
print(tuple(n*2 for n in range(1, 6)))
"""
리스트 내포는 사실 문자열을 뺀 모든 군집자료형(리스트, 딕셔너리, set, 튜플)
에서도 사용가능하다.

딕셔너리는 
{키: 값 for 키, 값 in 딕셔너리} 아니면,
dict({키: 값 for 키, 값 in 딕셔너리}) 같은 형식이다.
(딕셔너리 부분에는 달랑 {~~}같은 딕셔너리 객체가 들어가면 에러가 난다.
항상 뒤에, .items()로 키-값 쌍아니면, .keys()로 키들 아니면, .values()로 값들을 반환하게 해야한다.)
if문을 활용할 수 있으며, if문의 조건식으로 키 또는 값을 활용하면 된다.


set(집합)에서는
{식 for 변수 in 반복가능한객체}
set(식 for 변수 in 반복가능한객체) 같은 형식이다. 
반복가능한 객체는 문자열이든 리스트, 튜플이든 다 올수 있다. 

튜플에서는 
tuple(식 for 변수 in 반복가능한객체) 같이 사용한다. 
(식 for 변수 in 반복가능한객체) 같이 사용하면 제너레이터 표현식(튜플이 아니게)이 된다.
"""