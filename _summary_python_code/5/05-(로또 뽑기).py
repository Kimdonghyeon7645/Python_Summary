import random


def lotto_dong(x):
    for i in range(x):
        lotto = [random.randint(1, 45) for i in range(6)]
        lotto = list(set(lotto))
        while len(lotto) < 6:
            lotto = [random.randint(1, 45) for i in range(6)]
            lotto = list(set(lotto))
        lotto.sort()
        print(f'{i+1}번째 뽑은 번호:', lotto)


def lotto_hyeon():
        Xlotto = [random.randint(1, 45) for i in range(6)]
        Xlotto = list(set(Xlotto))
        while len(Xlotto) < 6:
            Xlotto = [random.randint(1, 45) for i in range(6)]
            Xlotto = list(set(Xlotto))
        Xlotto.sort()
        Xbonus = random.randint(1, 45)
        while Xbonus in Xlotto:
            Xbonus = random.randint(1, 45)
        print("\n이번 회차 로또 번호:", Xlotto, '보너스 번호:', f'[{Xbonus}]')


a = int(input("복권 얼마어치 사실거에요?(원단위) : "))
lotto_dong(a//1000)
lotto_hyeon()

"""
입력한 돈만큼 로또(자동)를 구매하고,
당첨 번호도 출력하는 프로그램.

random 모듈의 randint 함수 활용
"""
