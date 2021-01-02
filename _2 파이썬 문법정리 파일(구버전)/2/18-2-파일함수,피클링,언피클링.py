import pickle

lines = ["세\n", "로\n", "로\n", "보\n", "세\n", "요\n"]
with open('19.txt', 'w', encoding='utf-8') as file:
    # 파일을 open 할 때, encoding(인코딩)인자를 추가하면, 인코딩을 utf-8(한글지원)등으로 지정할 수 있다.
    file.writelines(lines)

"""파일(file) 문자열 여러개 읽고 쓰기
반복문과 .write()를 활용해서 문자열을 여러줄도 쓸 수 있다. (개행문자 '\n'가 필수)
하지만 간편하게 .writelines()를 활용해서 문자열 여러개를 한번에 입력할 수 있다. (마찬가지로 줄을 바꿀때 개행문자 필수)

대신 두 방법의 특징은, 개행문자를 넣지 않으면, 텍스트가 한줄로 붙여서 저장된다. 유의.
"""

with open('19.txt', 'r', encoding="utf-8") as file:
    # encoding 인자를 넣어서 txt 파일을 작성했으면, 읽을때도 필요하다. 없으면 에러남.
    line = None     # line 초기화
    while line != '':   # 읽어온 값이 ''(더이상 문자열이 없음)이 아닐때까지 반복
        line = file.readline()
        print(line.strip('\n'))
        # 여기서 .strip()함수는 별게 아니고, 문자열 메쏘드로 \n(개행문자)를 삭제하는 역할
"""
.readline() 메쏘드를 쓴다면, 문자열을 한 줄씩 순서대로 읽을 수 있다.
근데 for 반복문으로 똑같이 파일의 내용을 읽을 수 있음, 파일 객체를 for 문의 반복가능한 객체로 넣는 것,

참고로 이외에도 파이썬 파일 메쏘드는 많으며, c언어랑 비슷함.
참고 : https://simplesolace.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%8C%8C%EC%9D%BC
"""
with open('19.txt', 'r', encoding="utf-8") as file:
    for line in file:
        print(line.strip('\n'))

"""피클링(pickling), 언피클링(unpickling)
파이썬은 파이썬 객체를 파일에 저장하는 pickle(피클) 모듈을 제공.
파이썬 객체를 파일로 저장하는 것을 피클링, 파일에서 파이썬 객체를 읽는 것이 언피클링이라 함.

.dump()메쏘드를 사용해서 피클링을 할 수 있고,
(.dump(객체, 파일객체) 형식)
.load()메쏘드를 사용해서 언피클링을 할 수 있음. (객체를 반환)
(.dump(파일객체) 형식)

파일이름의 확장자는 자유롭게 해도 상관 없으나, 피클링, 언피클링할 때 b(바이너라)파일 형식으로 해야함.
따라서 파일모드에 b를 붙여줘야 함.

피클링 했던 순서대로 언피클링도 이루어지며, (첫번째로 객체1을 피클링 했으면, 첫번째 언피클링때 객체1를 불러올수 있음)
피클링 횟수 만큼 언피클링 해야함.
"""
word = "삼겹살"
price = {'300g': 5000, '600g': 10000}
with open('pickle.ppap', 'wb') as f:
    pickle.dump(word, f)
    pickle.dump(price, f)

with open('pickle.ppap', 'rb') as f:
    w = pickle.load(f)
    p = pickle.load(f)
    print(w, p)
