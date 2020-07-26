class BaseClass:
    class_attr = "부모클래스의 클래스 속성"

    def __init__(self):
        self.base_attr = "부모클래스의 인스턴스 속성"
        print("부모클래스 생성자 호출")

    def func_base(self):
        print("부모클래스의 인스턴스 메쏘드")

    @classmethod
    def class_base(cls):
        print("부모클래스의 클래스 메쏘드")

    @staticmethod
    def static_base():
        print("부모클래스의 정적 메쏘드")


class DerivedClass(BaseClass):

    def __init__(self):
        print("자식클래스 생성자 호출")


temp = DerivedClass()
temp.static_base()
temp.class_base()
temp.func_base()
print(temp.class_attr)
# print(temp.base_attr)     # 에러
""" 부모클래스의 인스턴스 속성 사용:
상속한 자식클래스에서 부모클래스의 요소들을 참고할 때,
메쏘드는 부모의 클래스, 인스턴스, 정적 메쏘드 모두 호출할 수 있지만,
속성은 부모의 클래스 속성만 접근할 수 있지, 인스턴스 속성은 접근할 수 없다.

인스턴스 속성을 실행하면 에러가 발생하는데, 그 이유는 사실 부모클래스의 __init__ 메쏘드가 호출되지 않았기 때문이다.
(실행 결과를 보면, 자식클래스의 __init__ 메쏘드만 호출됬고, 부모클래스의 __init__ 메쏘드는 호출되지 않았다.
인스턴스 속성은 __init__ 메쏘드가 생성되어야 같이 생성되기에, 인스턴스 속성도 생성되지 않았었고, 그래서 접근할 수 없던 것이다.

그러면 상속된 자식클래스에서 부모클래스의 __init__ (생성자)를 호출하려면, super() 함수를 이용한다.

super().메쏘드()
라고 하면, 부모클래스의 원하는 메쏘드를 호출 할 수 있다.
이때 super().__init__()
로 부모클래스의 생성자를 호출하면, 비로소 인스턴스 속성도 생성되고, 접근할 수 있게된다.


super() 를 더 명확하게 사용할 수도 있는데,

super(자식클래스, self).메쏘드
로 super()와 가능은 같지만, 현재 클래스가 어떤 클래스인지 명확하게 표시할 수 있다.
"""


class Parents:
    def __init__(self):
        self.parents_attr = '와우'


class Child(Parents):
    def prt_parents_attr(self):
        print(self.parents_attr)


ins = Child()
ins.prt_parents_attr()
"""
참고로 자식클래스에서 __init__ 메쏘드를 생략하면, 
부모클래스의 __init__ 이 자동으로 호출되서 super()를 사용할 필요가 없다.
"""