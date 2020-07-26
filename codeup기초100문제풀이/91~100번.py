'''91'''
# a, m, d, n = map(int, input().split(' '))
# for i in range(n-1):
#     a = a *m +d
# print(a)

'''92'''
# a, b, c = map(int, input().split(' '))
# i = a
# while i%a != 0 or i%b != 0 or i%c != 0:
#     i += 1
# print(i)

'''93'''
# n = int(input())
# b = list(map(int, input().split(' ')))
# arr = []
# for _ in range(24):
#     arr.append(0)
# for i in range(n):
#     arr[b[i]] += 1
# for p in range(1, 24):
#     print(arr[p], end= ' ')

'''94'''
# arr = []
# n = int(input())
# b = input().split()
#
# for i in range(n):    # arr = [0 for i in range(n)]같은 리스트 내포로 배열 초기화 가능
#     arr.append(int(b[i]))
# i = n - 1
# while i >= 0:
#     print(arr[i], end=' ')
#     i -= 1

'''95'''
# n = int(input())
# new = list(map(int, input().split(' ')))
# for i in range(n):
#     if i == 0 or min > new[i]:
#         min = new[i]
# print(min)

'''96'''
# arr = [[0 for i in range(19)] for i in range(19)]
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split(' '))
#     arr[a-1][b-1] = 1
# for i in range(19):
#     for j in range(19):
#         print(arr[i][j], end=' ')
#     print()

'''97'''
# arr = [[0 for i in range(20)] for i in range(20)]
# for i in range(19):
#     a =list(map(int, input().split(' ')))
#     for j in range(19):
#         arr[i+1][j+1] = a[j]
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split(' '))
#     for j in range(1, 20):
#         arr[j][y] = 1 if arr[j][y] == 0 else 0
#         arr[x][j] = 1 if arr[x][j] == 0 else 0
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(arr[i][j], end=' ')
#     print()

'''98'''
# ax, ay = map(int, input().split(' '))
# arr = [[0 for _ in range(ax+2)] for _ in range(ay+2)]
# n = int(input())
# for _ in range(n):
#     l, d, x, y = map(int, input().split(' '))
#     for i in range(l):
#         if d == 1:
#             arr[x - 1 + i][y - 1] = 1
#         else:
#             arr[x - 1][y - 1 + i] = 1
# for i in range(ax):
#     for j in range(ay):
#         print(arr[i][j], end=' ')
#     print()

'''99'''
# arr = [[0 for _ in range(11)] for _ in range(11)]
# for i in range(10):
#     jj = list(map(int, input().rstrip().split()))
#     for j in range(10):
#         arr[i][j] = jj[j]    # 미로상자 입력 끝, 개미 이동 시작
# antx = anty = 1
# while True:
#     if arr[anty][antx] == 2:
#         arr[anty][antx] = 9
#         break
#     arr[anty][antx] = 9
#     if arr[anty][antx + 1] != 1:
#         antx += 1
#     elif arr[anty + 1][antx] != 1:
#         anty += 1
#     else:
#         break    #개미 이동 끝, 경로 출력 시작
# for i in range(10):
#     for j in range(10):
#         print(arr[i][j], end=' ')
#     print()