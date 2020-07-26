'''51'''
a, b = map(int, input().split(' '))
if b >= a:
    print(1)
else:
    print(0)

'''52'''
a, b = map(int, input().split(' '))
if b != a:
    print(1)
else:
    print(0)

'''53'''
x=int(input())
b=bool(x)
x=int(not b)
print(x)

'''54'''
a, b = map(int, input().split(' '))
if a == 1 and b == 1:
    print(1)
else:
    print(0)

'''55'''
a, b = map(int, input().split(' '))
if a == 1 or b == 1:
    print(1)
else:
    print(0)

'''56'''
a, b = map(int, input().split(' '))
if a == b:
    print(0)
else:
    print(1)

'''57'''
a, b = map(int, input().split(' '))
if a == b:
    print(1)
else:
    print(0)

'''58'''
a, b = map(int, input().split(' '))
if a == 0 and b == 0:
    print(1)
else:
    print(0)

'''59'''
a= int(input())
print(~a)

'''60'''
a, b = map(int, input().split(' '))
print(a & b)
