# def fib(i):
#     if i < 3:
#         return 1
#     return fib(i-1) + fib(i-2)


def fib(i):
    if i in [0, 1]:
        return i
    return fib(i-1) + fib(i-2)


n = int(input())
print(fib(n))

""" 피보나치수열 재귀함수로 반환:
n을 입력하면 n번째의 피보나치수열 값이 출력된다.

좀 머리좀 잘써야 대가리가 돌아갈듯? https://dojang.io/mod/quiz/view.php?id=2356
"""