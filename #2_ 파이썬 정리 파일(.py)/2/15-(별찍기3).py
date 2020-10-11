# 별찍기 문제 (마름모)
n = int(input("폭을 입력하시오 (홀수) : "))
for i in range(1, n+1, 2):
    print(f"{'*' * i : ^10}")
for i in range(n-2, 0, -2):
    print(f"{'*' * i : ^10}")

# .ljust(n) n만큼(n은 변수도 가능) 왼쪽 정렬   .ljust(n, 'X')하면 공백을 X로 채워줌
# .center(n) 가운데 정렬
# .rjust(n) 오른쪽 정렬
