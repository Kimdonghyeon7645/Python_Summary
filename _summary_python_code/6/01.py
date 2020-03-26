dic = {1:'2', 2:'4', 3:'6'}
target = int(input())
print(dic.get(target, f'{target}은 읎어요.'))
# 키 값을 못 뽑아 올때 없다고 출력할 수 있다.