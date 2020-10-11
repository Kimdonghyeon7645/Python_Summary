words = input('단어를 입력하세요: ')

rewords = ''.join(reversed(words))
print(words, rewords)
if words == rewords:
    print("회문입니다")
else:
    print("회문이 아닙니다")
