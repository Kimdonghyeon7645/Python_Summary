print("N-gram - N개의 연속된 요소 추출기")
n = int(input("끊어 읽을 수를 입력하세요 : "))
word = list(input("문장을 입력하세요 : ").rstrip())
print(word)
if n < 0:
    print("<에러>끊어 읽을 수가 음수 입니다.")
elif len(word) < n:
    print("<에러>끊어 읽을 수가 전체 문장보다 큽니다.")
else:
    for i in range(len(word)+1-n):
        for j in range(i, n+i):
            print(word[j], end='')
        print()

"""N-gram:
2-gram, 3-gram, ... 같은 걸 묶어서 부르는 건데,
문장의 글자를 N개씩 묶은 것들을 추출하는 것.
"""
