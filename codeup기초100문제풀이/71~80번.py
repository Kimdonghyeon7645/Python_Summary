'''71'''
a = list(map(int, input().split(' ')))
for i in a:
    print(i)
    if i == 0:
        break

'''72'''
n = int(input())
a = list(map(int, input().split(' ')))
for i in range(n):
    print(a[i])

'''73'''
a = list(map(int, input().split(' ')))
for i in a:
    print(i)
    if i == 0:
        break

'''74'''
n = int(input())
for i in range(n, 0, -1):
    print(i)

'''75'''
n = int(input())
for i in range(n, 0, -1):
    print(i-1)

'''76'''
n = input()
for i in range(97, ord(n)+1):
    print(chr(i), end=' ')

'''77'''
n = int(input())
for i in range(0, n+1):
    print(i)

'''78'''
sum = 0
n = int(input())
for i in range(2, n+1, 2):
    sum += i
print(sum)

'''79'''
a = list(input().split(' '))
for i in a:
    print(i)
    if i == 'q':
        break

'''80'''
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(i)
        break