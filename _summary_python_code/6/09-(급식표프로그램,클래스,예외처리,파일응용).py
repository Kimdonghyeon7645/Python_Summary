# (클래스, 예외처리, 파일)종합 창작
class Lunch:
    def __init__(self, meal, soup, main_dish, side_dish):
        self.meal = meal
        self.soup = soup
        self.main_dish = main_dish
        self.side_dish = side_dish
    def __str__(self):
        msg = f"점심 식단\n밥: {self.meal}\n국: {self.soup}\n주메뉴: {self.main_dish}\n반찬: {self.side_dish}"

print(" 이번주 월~수요일의(7월 29일 ~ 7월 31일) 점심 급식표 관리 프로그램 입니다. ")
days = input("어떤 요일의 점심을 보시겠습니까?(숫자입력)  1: 월요일, 2: 화요일, 3: 수요일 : ")
try:
    int(days)
except Exception as e:
    print(f'잘못된 {type(e)}입니다')
    print(f'잘못된 {type}입니다')
else:
    print(f'\n{days} 점심 식단표')

if days == 1:
    f = open(r"C:\PycharmProjects\06\venv\1.txt", 'r')
    f.close()
elif days == 2:
    f = open(r"2.txt", 'r')
elif days == 3:
    f = open(r"3.txt", 'r')
lines = f.readlines()
Today = Lunch(lines[0], lines[1], lines[2], lines[3])
print(Today)
f.close()

""" 급식표 보는 프로그램:
클래스와 예외처리, 파일 개념을 모두 종합해서 응용한 예제
"""
