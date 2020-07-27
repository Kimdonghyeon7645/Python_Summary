def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)


f = int(input("입력값 : "))
pr = factorial(f)
print(pr)

""" 재귀함수(recursive call) :
함수안에서 스스로(함수)를 다시 호출하는 것. (return 이 되지 않는 한 무한반복(호출))

파이썬에서 재귀함수의 최대횟수는 기본적으로 1000 임.
넘어설경우 RecursionError 에러 발생. (sys 모듈의 setrecursionlimtit(재귀함수 최대호출횟수)함수로 최댓값을 변경해줄 수 있음)

따라서 재귀함수를 무한반복 하기 싫다면, 멈추고 싶은 조건을 걸어서 그조건에 함수가 return 하게 만들어야함.
참고로 return 시 함수가 호출됬던 바로 그 위치로 돌아온다.    
(함수가 종료되는 것은 중간에 return 됬거나 or 함수의 마지막 실행문까지 실행이 끝난 후)
ex>
def func(a):
    func(a-1)
    print(a)
    if a is 0:
        return
    

이라는 재귀함수 func()에서

func(5)의 실행결과는, 
1
2
3
4
5
가 될것임.

"""
