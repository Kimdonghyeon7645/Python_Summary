"""
블로그 포스팅 : https://bodhi-sattva.tistory.com/65
"""

no_char = "언젠가 파이썬 정리도 끝나겠지?"
print(no_char[2], no_char[-4])
"""인덱싱, 슬라이싱:
인덱싱(Indexing, 가리킴)과 슬라이싱(Slicing, 잘라냄)은 각각 문자열에서 한개 또는 여러개를 뽑아내는 방법이다.
인덱싱은 그중 1개의 값을 뽑아내는 것으로, (변수이름)[n] 과 같이 쓴다. 
[n]이라고 하면, 문자열의 인덱스 n 번째에 있는 값을 가리킨다. (참고로 인덱스는 0 ~ 문자열의개수-1 으로 차례대로 존재한다)
참고로 n가 음수라면, 문자열의 맨끝부터 거꾸로 해서 -n 번째에 있는 값을 가리킨다.
"""
print(no_char[:], no_char[3:], no_char[3:7], no_char[4:7:2], no_char[6:3:-2])
"""
슬라이싱은 여러개의 값을 뽑아내는 것으로, 다양한 방법으로 쓸 수 있는데,
(변수이름)[:] 비워놓으면 끝을 의미한다. 따라서 맨처음부터 맨끝까지 이다.
(변수이름)[n:] n번째 인덱스부터 맨 끝까지 가리킨다.
(변수이름)[n:m] n번째 인덱스부터 m-1번째 인덱스까지 가리킨다.
(변수이름)[n:m;s] n번째 인덱스부터 m-1번째 인덱스까지 s 간격만큼 건너뛰어서 가리킨다.
* 여기서 특징은 n <= 출력되는 문자열 인덱스 < m 라는 점이다. [:m]를 해도 인덱스 m-1까지 문자열이 출력된다.
와 같다. 인덱싱처럼 n, m, s가 음수일 수도 있고, 특히 s(간격)이 음수면, 거꾸로 진행한다.  
"""


"""문자열 내장 함수:
문자열 변수에 .을 붙이고 특정 함수를 달면, 문자열만 있는 함수를 실행할 수 있다. (이걸 내장 함수라 한다)
대표적이고, 자주쓰이는 함수는 아래와 같다. 
확실하게 알아볼 셈이면 03-3을 확인하자.
"""
ex = "Hello! Omm... PPAP?"
print(ex.count('.'))
# 인자 값(문자, 문자열)이 문자열에 몇번 쓰이는지 숫자 반환

print(ex.find('e'))
# 인자 값(문자, 문자열)이 가장 처음 쓰인 문자열 인덱스를 반환 (없을시 -1 반환)

print(ex.index('e'))
# find 와 같은 역할 (찾을려는 것이 없으면 오류 발생)

print('-'.join(ex))
# 인자 값(리스트, 문자열)에 점 앞에 있는 문자, 문자열(ex> '-')을 요소 사이사이에 삽입

print(ex.upper())
# 문자열의 문자를 모두 대문자로 변환

print(ex.lower())
# 문자열의 문자를 모두 소문자로 변환

print(ex.replace('PPAP', '샌즈'))
# 문자열의 모든 첫번째 인자 값(문자, 문자열)을 두번째 인자 값으로 수정

print(ex.split(' '))
# 문자열을 인자 값(문자, 문자열(괄호 비워놓을시 화이트 스페이스가 인자))을 기준으로 나누어서 리스트로 반환

ex2 = "       널널 하쥬?       "
print(ex2.lstrip(), "<문자열 끝")
# 왼쪽 공백 삭제

print(ex2.rstrip(), "<문자열 끝")
# 오른쪽 공백 삭제

print(ex2.strip(), "<문자열 끝")
# 양쪽 공백 삭제

