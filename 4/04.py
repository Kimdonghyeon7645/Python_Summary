def lock_(a):
    for i in range(len(a)):
        if ord(a[i]) > 64 and ord(a[i]) < 91:
            a[i] = chr(ord(a[i])+n)
        if ord(a[i]) > 96 and ord(a[i]) < 123:
            a[i] = chr(ord(a[i])+n)

def unlock_(b):
    for i in range(len(b)):
        if ord(b[i]) > 64 and ord(b[i]) < 91:
            print(chr(ord(b[i])-n), end='')
        if ord(b[i]) > 96 and ord(b[i]) < 123:
            print(chr(ord(b[i])-n), end='')

n = int(input("n칸을 입력하세요: "))
word = list(input("암호화 할 평문을 입력하세요: "))
ppap = word
lock_(word)
print("암호화 완료:",''.join(word))
y = input("복호화 하시겠습니까?(y/n): ")
if y == 'y' or y == 'Y':
    unlock_(list(word))
else:
    print("프로그램 종료")
