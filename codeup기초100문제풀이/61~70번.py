# '''61'''
# a, b = map(int, input().split(' '))
# print(a ^ b)
#
# '''62'''
# a, b = map(int, input().split(' '))
# print(a | b)
#
# '''63'''
# a, b = map(int, input().split(' '))
# print(a if a>b else b)
#
# '''64'''
# a, b, c = map(int, input().split(' '))
# print((b if b<c else c) if a>b else (c if a>c else a))
#
# '''65'''
# a = list(map(int, input().split(' ')))
# for i in a:
#     if i%2 == 0:
#         print(i)
#
# '''66'''
# a = list(map(int, input().split(' ')))
# for i in a:
#     if i%2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# '''67'''
# a = int(input())
# if a > 0:
#     print("plus")
# else:
#     print("minus")
#
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

'''68'''
a = int(input())
if 100 >= a and a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
elif a >= 0:
    print('D')

'''69'''
def f(x):    #자칭 파이썬의 switch_case문 (  .get(x, '출력') 은 default  )
    return {'A': 'best!!!', 'B': 'good!!', 'C': 'run!', 'D': 'slowly~'}.get(x, 'what?')

a = input()
print(f(a))

'''70'''
def f(x):    #자칭 파이썬의 switch_case문 (  .get(x, '출력') 은 default  )
    return {1: 'spring', 2: 'summer', 3: 'fall'}.get(x, 'winter')

a = int(input())
print(f(a//3))
