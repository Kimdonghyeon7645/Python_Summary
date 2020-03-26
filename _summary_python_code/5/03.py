import time as t

print('30초 세보세요')
t0 = t.time()
print('*'*20, "마음속으로 30초 세신후 엔터 누르세요", '*'*20, sep='\n')
a = input()
if a == '':    # 엔터키 입력 받으면 ''이 저장
    t1 = t.time()
    print(f"{t1-t0 : .2f}초 지났습니다.")
    if t1-t0 >= 29.5 and t1-t0 <= 30.5:
        print("정답입니다!")

