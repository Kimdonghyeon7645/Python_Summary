class Mother:
    def mom(self):
        print("엄마 호출!")


class Father:
    def daddy(self):
        print("아빠 호출!")


class Child(Mother, Father):
    def child(self):
        print("자식 호출!")


son = Child()
son.mom()
son.daddy()
son.child()
""" 다중상속:
디중상속은 말처럼 상속을 다중으로 받는것이다. 여러 부모 클래스로 부터 상속받아서 자식 클래스를 만들며,
자식 클래스를 만들때 괄호()안에 부모 클래스들의 이름을 콤마(,)로 구분해서 넣는다.

이런 경우에서 자식 클래스는 부모클래스들을 모두 상속받았기에, 부모클래스들의 메쏘드와 속성(super()함수 응용)을 사용할 수 있다.
"""


class DanGun:
    def dangun(self):
        print("단군할아버지 호출!")


class Mother(DanGun):
    def mom(self):
        print("엄마 호출!")


class Father(DanGun):
    def daddy(self):
        print("아빠 호출!")


class Child(Mother, Father):
    def child(self):
        print("자식 호출!")


temp = Child()
temp.dangun()
""" 다이아몬드 상속:
여기서 예시에서는 단군클래스를 엄마클래스, 아빠클래스가 상속하고, 그러한 엄마클래스, 아빠클래스를 자식클래스가 상속하는데,
이러한 구조가 그림으로 그리면 다이아몬드(마름모)같아서 객체지향 프로그래밍에서 이런 관계를 다이아몬드 상속이라 한다.

다만 여기서 부모셋다 같은 메쏘드 이름을 가지고 있다면 어떤 클래스의 메쏘드를 호출할지 애매해지는데,
이런 애매한 문제가 다이아몬드 상속에 많아서 죽음의 다이아몬드란(다이다이아몬드ㅋㅋㅋ) 별명을 가지고 있다. 
"""

print(Child.mro())
""" 메쏘드 탐색순서(Method Resolution Order, MRO):
그래서 많은 프로그래밍 언어는 다이아몬드 상속에 대한 해결책이 있는데, 파이썬에서는 메쏘드 탐색 순서라는 해결책이 있다.

이 메쏘드 탐색 순서를 확인하려면, 메쏘드 탐색 순서(Method Resolution Order)의 약자 .mro() 메쏘드를 이용하면 된다.

클래스이름.mro()
과 같이 하면, 해당 클래스의 메쏘드 탐색 순서를 반환한다.

메쏘드의 기본적인 호출 순서는, 자기 자신이 우선이고, 그다음이 부모클래스, 그다음이 부모의 부모클래스 순이다.
같은 부모클래스 순에서는, 클래스를 다중상속 할때 괄호()안의 배치 순서대로, 왼쪽 부모클래스가 우선시된다.

ex) 자식클래스(부모클래스1, 부모클래스2): 로 상속받았으면 부모클래스1 > 부모클래스2

이런 규칙으로 탐색순서를 알수 있지만, 상속관계가 꽤 복잡하다면 mro 를 살펴보는 것이 편리하다.
"""

print(int.mro(), DanGun.mro())  # 단군클래스도 조상이 있다니.. object는 환웅인가 보다.
""" object 클래스:
참고로 mro 를 출력했을 때 항상 맨뒤에 오는 클래스가 있다.
바로 object 클래스 인데, 파이썬에서 object 는 모든 클래스의 조상이다.

파이썬3 부터 모든 클래스는 object 클래스를 상속받으며, 기본적으로 object 의 상속을 생략하지만,
사실, class 클래스:
가 class 클래스(object):
와 같은 의미다.

(파이썬 2에서는 class 클래스이름: 이 old-style 클래스고, class 클래스이름(object): 가 new-style 클래스로 구분됬지만,
파이썬 3는 old-style 클래스가 삭제되면서 두 방법 모두 new-style 클래스를 만들기에 두 방법을 혼용해도 되는 것이다.)
"""
