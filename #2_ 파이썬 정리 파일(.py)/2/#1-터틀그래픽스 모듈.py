import turtle as t
"""
터틀(turtle) 그래픽스 모듈:
파이썬에서 지원하는 기본 모듈로, 
거북이가 기어가는 모양대로 그림을 그려줌.

.shape() 함수:
그림을 그리는 아이콘의 모양을 설정
'classic' (기본값), 'triangle' (삼각형), 'circle'(원), 'arrow'(화살표), 'turtle'(거북이)...
.shape()만 쓰면, 현재 모양을 문자열로 반환함.

.forward() 함수 (=.fd())
거북이 머리방향으로 입력한 인자값 만큼 이동

.backward() 함수 (=.bk())
거북이 꼬리방향으로 입력한 인자값 만큼 이동

.right() 함수 (=.rt())
거북이를 오른쪽으로 입력한 인자값(도)만큼 회전

.left() 함수 (=.lf())
거북이를 왼쪽으로 입력한 인자값(도)만큼 회전

.setheading() 함수
인자값 각도롤 회전, (오른쪽 기준, x축 양의 방향을 0도(기준)으로 시계 반대방향의 각을 말함)

.circle() 함수
인자값 만큼의 반지름을 가지는 원을 그림

.color(펜색깔, 칠하는색깔) 함수
색이름을 인자값으로 사용('red', 'blue', 'green'...) (기본값 검정)
(웹 색상(#RRGGBB)를 이용해서 세밀한 색상을 인자값으로 쓸 수 있음)
인자값이 하나일 경우 그 색으로 펜과 칠하는 색깔을 통일함.

.pencolor() 함수
색이름을 인자값으로, 도형을 그릴때의 선 색깔을 지정

.fillcolor() 함수
도형 내부를 칠하는 색을 지정

.turtle.speed() 함수
움직이는 속도를 조절 (1이 느림 ~ 10이 빠름, 10을 넘어서면 0으로 취급(0은 가장빠름))

외에도 메쏘드가 너무 많다...
https://m.blog.naver.com/PostView.nhn?blogId=python_math&logNo=221214856867&proxyReferer=https%3A%2F%2Fwww.google.com%2F

링크로 축약한다.
"""
t.shape('turtle')
n = int(input("n각형의 각 : "))
for i in range(n):
    t.right(360 / n)
    t.forward(800 / n)

t.mainloop()
"""
위는, 각을 입력받아서 n각형을 그리는 코드
* 파이참같은 환경에서는 터틀 그래픽스 창이 열렸다가 바로 닫히기도 하는데, 창을 유지시키기 위해 .mainloop() 함수를 마지막에 덧붙임
"""