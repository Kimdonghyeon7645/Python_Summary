class BaseClass:
    def base_func(self):
        print("부모클래스의 메쏘드")


class DerivedClass(BaseClass):
    def derived_func(self):
        print("자식클래스의 메쏘드")


temp = DerivedClass()
temp.base_func()        # 자식 클래스에서 부모클래스의 메쏘드도 그대로 사용가능.
temp.derived_func()
""" 상속관계 vs 포함관계:
상속은 같은종류, 동등한 관계일 때 사용하며, is-a 관계라고 부른다.
(ex> 부모클래스가 사람, 자식클래스가 학생이면, 학생은 사람이다. 학생 is-a 사람)
"""


class Three:
    def prt_num(self):
        print(3)


class Number:
    def __init__(self):
        self.number_list = []

    def append_num(self):
        self.number_list.append(Three())    # Three 클래스의 인스턴스를 속성에 포함.


num = Number()
num.append_num()
print(num.number_list)
num.number_list[0].prt_num()    # 포함된 클래스의 메쏘드를 호출
""" 
포함은 상속을 사용하지않고, 클래스안에서 다른 클래스를 포함하는 관계로, has-a 관계라고 부른다.
상속을 사용하지 않고, 속성에 인스턴스를 만들고, 넣어서 관리하므로, 동등한 관계가 아닌 포함하는 관계다.
(ex> 포함하는클래스가 숫자, 포함되는 클래스가 셋이라면, 숫자는 셋을 포함하고 있다. 숫자 has-a 셋)

포함을 사용할 때는, 클래스 전체를 상속받고 싶지 않을때, (클래스의 일부만(속성, 메소드)사용할 때) 사용하며,
포함된 인스턴스를 속성에 담아서, 

클래스 안에서는

속성.포함된인스턴스의메쏘드()
속성.포함된인스턴스의속성

클래스 바깥에서는

포함하는인스턴스.속성.포함된인스턴스의메쏘드()
포함하는인스턴스.속성.포함된인스턴스의속성
와 같이 포함된 인스턴스의 메쏘드와 속성을 사용할 수 있다.
"""
