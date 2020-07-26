def func():
    n = 50
    print("외부함수 호출")

    def clo_func(x):
        print("클로저 호출")
        print("입력값:", x, "기본값(지역변수):", n)
        return x+n
    return clo_func


f = func()
print(f(1), f(-1), f(10))
""" 클로저(closure):
외부함수에서 내부함수를 정의하고, 외부함수의 반환값으로 내부함수 자체를 반환 할 수 있다.
함수를 반환값으로 할 때는 괄호를 붙이지 않고(return 함수이름() 같이하면 해당 함수의 반환값이 반환됨)

return 함수이름
과 같이 한다. 그러면 반환된 함수를 변수로 전달받을 수 있는데, (함수는 변수에 할당할 수 있다. 16-1 참고)
그렇게 변수에 함수가 저장되면, 외부함수의 호출이 끝나 함수를 반환하고 외부함수가 종료되어도, 
반환값으로 내부함수를 전달받아 변수로 담은 상태로 함수를 사용할 수 있다.

이같이 쓰는 내부함수를 클로저라고 하며, 
이때 클로저(내부함수)는 자기와 관련된 환경(클로저에서 사용하는 외부함수의 매개변수)을 포함해서 유지하고 있음.
따라서 클로저는 함수와 함수를 들러싼 환경을 통채로 묶어 유지하다가, 나중에 사용하는 함수 (프로그램의 흐름을 저장)

이렇게 클로저로 지역변수와 코드(내장함수)를 묶어서 사용할 수 있으며,
클로저에 속한 지역변수는 바깥에서 직접 접근할 수 없어서 데이터를 숨길 때도 활용.
"""


def stars():
    star = "*"
    return lambda x: star * x


byeol = stars()
print(byeol(1), byeol(10), byeol(30))
""" lambda(람다) 표현식과 활용
간단하게 클로저(내부함수 + 지역변수)를 람다를 응용해서 만들 수 있음. (간단하게 클로저를 표현할 수 있어 자주 응용)
반한 할 때 람다표현식으로 함수를 만들어서 그자체(클로저)를 반환하게 함.
"""
# 람다 = 익명 (1줄)함수 vs 클로저 = 함수와 함수에 대한 환경(지역변수, 코드)를 유지했다 나중에 다시 사용하는 함수


def pencil_price():
    price = 700

    def return_price(x):
        nonlocal price
        price *= x
        return price
    return return_price


ppp = pencil_price()
print(ppp(1), ppp(5), ppp(10))
"""
클로저에서 내부함수에 사용되는 외부의 지역변수를 수정하고 싶다면, 
마찬가지로 nonloccal 키워드를 활용해서 수정할 수 있다.

클로저의 함수와 다른 특징이, 함수는 외부함수 지역변수의 값을 내부함수에서 변경해도,
함수가 종료되면 다음번 호출될때에 영향을 주지 않지만,

클로저를 호출해서 지역변수의 값이 변경되면, 
클로저가 끝나고도, 클로저의 지역변수는 바뀐채로 유지된다. (정말로 프로그램의 흐름을 저장한다)
"""


def f():
    n = 10

    def f2():
        nonlocal n
        n += 1
        return n
    return f2()


print(f(), f())
# 위에는 함수중첩, 처음 호출할때 지역변수 값을 바꿨지만, 다시 호출할때 지역변수 값이 예전 값으로 되돌아 온상태로 시작함.
# 아래는 클로저, 두번 호출하는 것은 같지만, 다시 호출할때 처음호출로 변경된 지역변수 값이 유지된 상태로 시작함.


def counter():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count


c = counter()
for i in range(10):
    print(c())
"""
그래서 위같은 실행문에서 클로저는 호출될 때마다, 예전의 지역변수 값을 유지한채로 실행되게 되서,
함수를 호출한 횟수를 카운트 하게 된다.
"""

# 보충 내용 : http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%A1%9C%EC%A0%80-closure/
# 네임스페이스로 함수안의 변수를 확인할 수 있듯이, 클로저도 네임스페이스로 확인 할 수 있음.
