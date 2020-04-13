'''31'''
a = int(input())
b = list(oct(a))
for i in range(2, len(b)):
    print(b[i], end='')

'''32'''
a = int(input())
b = list(hex(a))
for i in range(2, len(b)):
    print(b[i], end='')

'''33'''
a=input()
n=int(a)
print('%X' % n)

'''34'''
a = input()
print(int(a, 8))

'''35'''
a = input()
b = int(a, 16)
b = oct(b)
for i in range(2, len(b)):
    print(b[i], end='')

'''36'''
a = input()
print(ord(a))

'''37'''
a = int(input())
print(chr(a))

'''38'''
a, b = map(int, input().split(' '))
print(a + b)

'''39'''
a, b = map(int, input().split(' '))
print(a + b)

'''40'''
a = int(input())
print(-a)