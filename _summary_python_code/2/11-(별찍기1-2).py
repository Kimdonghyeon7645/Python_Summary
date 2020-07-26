# 별찍기 문제 (직각삼각형 좌우대칭)
n = int(input("높이를 입력하시오 : "))
for i in range(1, n+1):
    print(f"{'*'*i : >10}")
    # 포맷팅 f-string에서는 (출력할 것) or (출력할 것 : 출력 형식)
