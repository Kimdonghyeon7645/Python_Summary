n = int(input("끊어 읽을 수를 입력하세요 : "))
word = input("문장을 입력하세요 : ")
a = word.split(' ')
if n < 0:
    print("<에러>수가 음수 입니다.")
elif len(a) < n:
    print("<에러>수가 단어보다 더 큽니다.")
else:
    for i in range(len(a)+1-n):
        for j in range(i, n+i):
            print(a[j], end=' ')
        print(' ')