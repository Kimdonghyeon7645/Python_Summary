def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)

f = int(input("입력값 : "))
pr = factorial(f)
print(pr)
# 재귀함수