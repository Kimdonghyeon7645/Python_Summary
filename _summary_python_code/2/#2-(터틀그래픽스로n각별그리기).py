import turtle as t

t.shape('turtle')
t.speed('fastest')

n, length = map(int, input("별의 꼭짓점 개수와 선의 길이를 입력하세요(둘은 공백으로 구본해서) : ").split())
for i in range(n):
    t.forward(length)
    t.right((360/n) * 2)
    t.forward(length)
    t.left(360/n)

t.mainloop()

"""
n개의 꼭짓점을 가지는 별을 그리는 코드
"""