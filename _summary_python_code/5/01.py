import random as r

r_list = [r.randint(1, 100) for i in range(10)]    # 랜덤 기본 리스트
r_list.append(50)    # 맨 뒤에 50 추가
r_list.sort()    # 정렬
del r_list[::2]    # 짝수 자리의 요소 제거
r_list2 = [r.randint(100, 200) for i in range(5)]    # 새로운 리스트
f_list = r_list + r_list2    # 두 리스트 합체
print(f_list)