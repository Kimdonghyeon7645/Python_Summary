word = input('단어를 입력하세요: ')

oh = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        oh = False
        break

if oh == True:
    print("회문입니다")
else:
    print("회문이 아닙니다")