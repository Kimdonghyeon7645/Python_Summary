n, m = map(int, input().split())
a = {i for i in range(1, n+1) if n % i == 0}
b = {i for i in range(1, n+1) if m % i == 0}
divisor = a & b
print(divisor)
"""
집합연산(&)으로 공약수 구하는 코드
"""
