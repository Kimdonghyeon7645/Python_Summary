import random as r

r_list = [r.randint(1, 100) for i in range(10)]    # 랜덤 기본 리스트
r_list.append(50)    # 맨 뒤에 50 추가
r_list.sort()    # 정렬
del r_list[::2]    # 짝수 자리의 요소 제거
r_list2 = [r.randint(100, 200) for i in range(5)]    # 새로운 리스트
f_list = r_list + r_list2    # 두 리스트 합체
print(f_list)

""" random 모듈 응용:
randint() 함수 : randint(n, m)같이 하면, n~(m-1)사이에서 랜덤숫자 1개를 뽑아냄
이러한 randint() 함수와 리스트 표현식을 짬뽕해서 응용하는 프로그램.
"""