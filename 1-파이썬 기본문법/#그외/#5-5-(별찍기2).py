# 별찍기 문제 (정삼각형)
n = int(input("폭을 입력하시오 : "))
for i in range(1, n+1, 2):
    print(f"{'*'*i : ^10}")
    # print(f"{format('*'*(i), '^10'}") 과 같다.
