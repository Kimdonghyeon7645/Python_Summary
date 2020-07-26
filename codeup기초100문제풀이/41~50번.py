'''41'''
w = input()
print(chr(ord(w)+1))

'''42'''
a, b = map(int,input().split(' '))
print(a//b)

'''43'''
a, b = map(int,input().split(' '))
print(a%b)

'''44'''
a = int(input())
print(a+1)

'''45'''
a, b = map(int, input().split(' '))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b, 2))

'''46'''
a, b, c = map(int, input().split(' '))
print(a+b+c)
print(round((a+b+c)/3, 1))

'''47'''
a = int(input())
print(a*2)

'''48'''
a, b = map(int, input().split(' '))
print(a*(2**b))

'''49'''
a, b = map(int, input().split(' '))
if a>b:
    print(1)
else:
    print(0)

'''50'''
a, b = map(int, input().split(' '))
if a==b:
    print(1)
else:
    print(0)

