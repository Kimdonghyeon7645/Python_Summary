'''책 딕셔너리'''
books = {'394039': {'title': '파이썬 코딩의 기술', 'year': 2016, 'author': '브렛 슬라킨', 'price': 21600},
        '230999': {'title': '골빈해커의 3분 딥러닝', 'year': 2017, 'author': '김진중', 'price': 19800},
        '220333': {'title': 'c언어 트레이닝', 'year': 2017, 'author': '아서 줄리아니', 'price': 16200},
        '551139': {'title': '웹 해킹 입문', 'year': 2016, 'author': '이상환', 'price': 20500},
        }

# print(books.keys())
# print(books.values())
# print(books.items())

for k, v in books.items():
    if v['price'] > 20000:
        print(f"ISBN :{k} 책 제목 : {v['title']} 가격 : {v['price']}")

#두번째 방법
for k, v in books.items():
    if v.get('price') > 20000:
        print("ISBN :", k, "책 제목 :", v['title'], "가격 :", v['price'])
