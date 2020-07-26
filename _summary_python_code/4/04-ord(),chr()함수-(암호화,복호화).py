def lock_(a):
    for i in range(len(a)):
        if 91 > ord(a[i]) > 64:
            a[i] = chr(ord(a[i])+n)
        if 96 < ord(a[i]) < 123:
            a[i] = chr(ord(a[i])+n)


def unlock_(b):
    for i in range(len(b)):
        if 91 > ord(b[i]) > 64:
            print(chr(ord(b[i])-n), end='')
        if 123 > ord(b[i]) > 96:
            print(chr(ord(b[i])-n), end='')


n = int(input("n칸을 입력하세요: "))
word = list(input("암호화 할 평문을 입력하세요: "))
lock_(word)
print("암호화 완료:", ''.join(word))
y = input("복호화 하시겠습니까?(y/n): ")
if y == 'y' or y == 'Y':
    unlock_(list(word))
else:
    print("프로그램 종료")

"""영어 암호화/복호화 프로그램:
ord() : 문자(인자값)의 아스키 코드(or 유니코드) 값을 돌려줌.
chr() : 아스키코드(인자값)에 해당하는 문자를 돌려줌.

이 두 파이썬 내장함수를 이용해서, 문자의 아스키코드를 수정해서 암호, 복호화를 
하는 프로그램을 작성.
"""
