v = []
for a in range(10):
    for b in range(10):
        if a is b:
            v.append(1)
        else:
            v.append(0)
    print(v)
    v.clear()
'''
for 문과 range()함수, 리스트 함수를 응용한 코드다.
대각선 출력! 
'''