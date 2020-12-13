class Class1:
    class_attr = 10
    @classmethod
    def class_method(cls, n):
        print(n + cls.class_attr)


Class1.class_method(10)
Class1.class_method(5)
Class1.class_method(0)
"""클래스 메쏘드:
클래스 속성처럼, 클래스 메쏘드도 존재한다.
클래스메쏘드는 메쏘드위에 @classmethod 를 붙이며, (여기서 @를 붙여 사용하는 것을 데코레이터라고 하며, 자세한건 다음에 언급된다.)

클래스 메쏘드의 첫번째 매개변수는 인스턴스 자신을 나타내는 self 대신, cls (Class 의 약자,클래스 자신)
를 지정한다. (인스턴스 메쏘드가 아닌, 클래스 메쏘드이니까)

클래스.메쏘드(인자값)
과 같이 클래스 메쏘드에 접근할 수 있으며, 

클래스 메쏘드의 매개변수 cls 를 이용해서, 클래스 속성(cls.클래스속성이름) 이나, 클래스 메쏘드(cls.클래스 메쏘드()) 를 접근할 수 있다.
또한 인스턴스 매쏘드가 아니다 보니까, 인스턴스 없이 호출할 수 있다. (인스턴스 생성없이도 호출가능)
"""


class Temp:
    def __init__(self, n):
        print("인스턴스 생성", n, "전달받음")

    @classmethod
    def create_instance(cls, n):
        ins = cls(n)
        return ins


Temp.create_instance(5)
Temp.create_instance(10)
"""
추가로 cls 를 이용해서, 현재 클래스의 인스턴스를 만들수도 있다. (인스턴스의 매개변수도 넘겨받을 수 있다.)
cls 자체가 클래스 이므로, cls() 는 현재클래스() 와 같기 때문이다.
"""


class Class2:
    @staticmethod
    def static_method(n, m):
        print(n + m)


Class2.static_method(1, 2)
Class2.static_method(2, 3)
""" 정적메쏘드:
정적 메쏘드는 클래스 메쏘드와 비슷하다.
클래스 메쏘드처럼 메쏘드 위에 @staticmethod 를 붙여야 하며, 정적메쏘드는 self를 매개변수에 지정하지 않는다.

다시말해서 self를 매개변수로 받지 않으므로, 인스턴스 속성, 메쏘드에 접근할 수 없다.
그래서 보통 정적 메쏘드는 메쏘드의 실행이 외부 상태에 영향을 끼치지 않는 순수함수(pure function)를 만들 때 사용한다.
(쉽게말해 인스턴스의 상태를 변화시키지 않는 메쏘드를 만들때 정적 메쏘드를 활용한다.)

대신에 정적 메쏘드도 클래스 속성과 메쏘드는 

클래스이름.속성이름
클래스이름.메쏘드이름
과 같이 접근할 수 있다. 
(대신에 정적메쏘드와 비슷한 클래스 메쏘드에서 클래스 속성과 메쏘드를 참조하는 목적으로 사용하며,
정적메쏘드는 목적이 외부 메쏘드, 속성에 영향을 주지않는 메쏘드를 만드는 목적으로 사용법이 갈린다.)
"""