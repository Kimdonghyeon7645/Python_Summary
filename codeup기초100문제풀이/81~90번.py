'''81'''
a, b = map(int, input().split(' '))
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)

'''82'''
num16 = input()
num10 = int(num16, 16)
for i in range(1, 16):
    print(num16, '*', '%X' % (i), '=', '%X' % (num10*i), sep='')

'''83'''
n = int(input())
for i in range(1, n+1):
    if i == 3 or i == 6 or i == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')

'''84'''
n = 0
r, g, b = map(int , input().split(' '))
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            n = n+1
print(n)

'''85'''
h, b, c, s = map(int, input().split(' '))
mb = (h *b *c *s) / (8 *1024 *1024)
print(round(mb, 1), 'MB')

'''86'''
w, h, b = map(int, input().split(' '))
mb = (w *h *b) / (8 *1024 *1024)
print(round(mb, 2), 'MB')

'''87'''
sum = 0
n = int(input())
for i in range(1, n+1):
    sum += i
    if sum >= n:
        print(sum)
        break

'''88'''
n = int(input())
for i in range(1, n+1):
    if i%3 != 0:
        print(i, end=' ')

'''89'''
n, w, re = map(int, input().split(' '))
n += w*(re-1)
print(n)

'''90'''
a, r, n = map(int, input().split(' '))
a *= r**(n-1)
print(a)