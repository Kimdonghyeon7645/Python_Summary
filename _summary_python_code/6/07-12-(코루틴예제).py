def calc():
    x = 0
    while True:
        w = (yield x)
        a, oper, b = w.split(' ')
        if oper == '+':
            x = int(a) + int(b)
        elif oper == '-':
            x = int(a) - int(b)
        elif oper == '/':
            x = int(a) / int(b)
        elif oper == '*':
            x = int(a) * int(b)


expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
"""
코루틴으로 연속되는 사칙연산을 문자열로 받아서 그에 맞게 처리하는 코루틴 예제.
"""