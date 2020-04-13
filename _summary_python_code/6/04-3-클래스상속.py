class BaseClass:
    def base_func(self):
        print("부모클래스의 메쏘드")


class DerivedClass(BaseClass):
    def derived_func(self):
        print("자식클래스의 메쏘드")


temp = DerivedClass()
temp.base_func()        # 자식 클래스에서 부모클래스의 메쏘드도 그대로 사용가능.
temp.derived_func()
""" 클래스 상속(inheritance):
상속은 무언가를 물려받는 다는 뜻으로, 클래스 상속도 마찬가지로 클래스를 물려받은 것이다.

이때 기능을 물려주는 클래스는 기반클래스(base class = 부모 클래스(parent class), 슈퍼 클래스(superclass))
기능을 물러(상속)받는 클래스는 파생클래스(derived class = 자식 클래스(child class), 서브 클래스(subclass))라고 한다.

새로운 클래스를 만들지 않고 상속 개념을 만든 이유는,
클래스 마다 중복되는 부분을 반복해서 만들 필요없이 상속을 사용한다면, 중복되는 기능을 생략할 수 있기 때문.
(상속으로 기반클래스의 기존 기능들을 파생클래스에서도 똑같이 사용할 수 있어 효율적)

참고로 클래스의 상속관계를 확인할 때는 issubclass() 함수를 사용한다.
issubclass(파생클래스, 기반클래스) 같은 형식으로 인자값을 넘기며, 파생클래스와 기반클래스(상속)관계가 맞을경우,
참(True), 아니면 거짓(False)를 반환하는 함수.
"""
print(issubclass(DerivedClass, BaseClass))
# 인자값으로 인스턴스가 올 수는 없다. (인자값으로 클래스가 와야됨)
