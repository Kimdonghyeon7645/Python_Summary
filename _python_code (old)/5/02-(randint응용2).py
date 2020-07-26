import random as r

rand = r.randint(1,100)
while True:
    a = int(input("숫자를 입력하세요\n"))
    if a > rand:
        print("입력하신 숫자가 큽니다.")
    elif a < rand:
        print("입력하신 숫자가 작습니다.")
    elif a == rand:
        print(f"{a} 정답입니다!")
        break