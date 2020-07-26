'''21'''
word = input()
print(word)

'''22'''
word = input()
print(word)

'''23'''
a, b = map(int, input().split('.'))
print(a)
print(b)

'''24'''
mylist = list(input())
for i in range(len(mylist)):
    print(f"'{mylist[i]}'")

# 코드업(예전 방법)
# mylist = list(input())
# for i in range(len(mylist)):
#     print("'{}'".format(mylist[i]))

'''25'''
n = input()
for i in range(5):
    print(f"[{int(n[i]) * 10 ** (4-i)}]")

# n = input()    #옛 방법
# for i in range(5):
#     print("[{}]".format(int(n[i]) * 10 ** (4-i)))

'''26'''
a = input().split(':')
print(a[1])

'''27'''
a = input().split('.')
print(a[2], end='-')    #end는 어떻게 끝낼지 정해주는 것( 문자도 가능 )
print(a[1], end='-')
print(a[0], end='')

'''28'''
a = input()
print(a)

'''29'''
a = input()
print(a)

'''30'''
a = input()
print(a)
