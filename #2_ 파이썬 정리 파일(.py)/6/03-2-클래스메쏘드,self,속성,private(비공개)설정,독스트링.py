class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60


myCar = Car(0, 'blue', 'Sonata')
print(f"자동차의 속도는 {myCar.speed}km/h")
print(f"자동차의 색상은 {myCar.color}")
print(f"자동차의 모델은 {myCar.model}")
myCar.drive()
print(f"자동차의 속도가 올라서 현재는 {myCar.speed}km/h 입니다.")


""" (인스턴스) 메쏘드(method):
메쏘드는 클래스에서 :콜론 붙인후 다음줄부터 작성하며, 메쏘드의 형식은 함수와 같다. (위치인수, 키워드인수, 가변인수도 사용가능) 
대신 메쏘드의 첫번째 매개변수로 반드시 self 가 들어간다.
메쏘드는 인스턴스를 통해서 호출하며(클래스 통해서가 아님) 

인스턴스.메쏘드()
와 같이 호출한다. (인스턴스 뒤에 점(.)을 붙인후 메쏘드를 호출) 그리고 이런 메쏘드를 인스턴스 메쏘드라고 한다. 
(인스턴스 메쏘드와 반대로, 다음에 배울 클래스 메쏘드와 정적 메쏘드도 있다)
"""
# 클래스에서 자주 등장하는 self 의 뜻은 인스턴스 자기자신을 의미한다 (c++ 의 this 처럼)


class TempClass1:
    def method_name(self):
        print("메소드 호출")

    def another_method(self):
        self.method_name()


temp = TempClass1()
temp.method_name()
temp.another_method()
"""
클래스 바깥이 아닌, 클래스의 메쏘드안에서 다른 메쏘드를 호출하려면, 

self.메쏘드() 
와 같이 호출할 수 있다. (self. 을 앞에 안붙이고 메쏘드를 호출하면, 클래스 바깥의 함수를 호출하는 뜻이 됨)
"""


class TempClass2:
    def __init__(self):
        self.attribute_name = '값'
        print("함수호출, 속성:", self.attribute_name)


temp2 = TempClass2()
print(temp2.attribute_name)
temp2.another_attr = '갚'
print(temp2.attribute_name, temp2.another_attr)
""" (인스턴스) 속성(attribute):
속성은 기본적으로 __init__라는 메쏘드 안에서 (__init__는 인스턴스를 만들때 호출되는 스페셜 메쏘드로, 생성자라 부른다. 자세한건 3-3 참고) 

self.속성이름 = 값 
과 같은 형식으로 선언한다. 그리고 이런 속성을 인스턴스 속성이라고 한다.
(인스턴스 속성과 반대로 다음에 배울 클래스 속성도 있다.)
물론 다른 메쏘드에서도 self.속성이름 = 값 과같은 방법으로 속성을 생성할 수 있지만, 이때는 해당 메쏘드를 호출해야만 속성이 생성된다.
추가로 인스턴스를 생성한 뒤에, 해당 인스턴스에만 속성을 추가할 수 있다. 

인스턴스.속성이름 = 값
과 같이 속성을 추가하며, 다른 인스턴스에는 해당되지 않는다. 
(클래스에 __slots__ = [] 과 같은 형식을 추가해서, 인스턴스가 자유롭게 속성을 추가 못하도록 할 수 있다.
허용할 속성 이름을 리스트안에 문자열로 하나씩 지정해주면 되며, 리스트안에 없는 속성은 허용되지 않아서 추가할 때 에러가 발생함)


속성을 접근할 때, 클래스 바깥에선

인스턴스.속성
과 같이 접근하며, 메쏘드 안에서는

self.속성
과 같이 접근할 수 있다.
"""


class TempClass3:
    __slots__ = ['attr']    # __slots__으로 허용하는 속성들을 지정


temp3 = TempClass3()
temp3.attr = 10
print(temp3.attr)
# temp3.a = 20      # 에러남, __slots__ 에 없는 속성이름(허용되지 않은 속성)


""" 비공개 속성, 메쏘드:
기존의 속성과 메쏘드는 클래스 내는 물론, 클래스 바깥에서도 접근, 호출하고, 값을 수정할 수도 있었음.
반대로 클래스 안에서만 접근, 호출할 수 있고, 클래스 바깥에서는 접근, 호출할 수 없게 할수 있음. 

간단하게 속성과 메쏘드의 이름 앞에 __를 추가하면 됨. 
이렇게 하면 클래스 안에서만 호출, 접근할 수 있으며, 이런 속성, 메쏘드를 비공개 속성(private attribute), 비공개 메쏘드(private method)라고하며,

반대로 기본값(클래스 밖에서도 접근가능)인 속성, 메쏘드는 공개 속성(public attribute), 공개 메쏘드(public method)라고 함.

비공개 속성과 메쏘드는, 속성과 메쏘드를 숨기고 싶을때 사용하며, 함부로 수정, 호출되면 안되는 중요한 값, 함수등에 사용함.
"""

class Temp:
    """임시 클래스 입니다."""
    def temp_func(self):
        """임시 메쏘드라는 설명을 출력하는 메쏘드 입니다."""
        print("임시 메쏘드")


a = Temp()
a.temp_func()
""" 클래스, 메쏘드의 독스트링:
클래스와 메쏘드 에서도 함수에서처럼 독스트링을 사용할 수 있다.
클래스, 함수를 만들때 콜론(:) 바로 다음줄에 생성하며, 규칙은 함수의 독스트링과 같다.

클래스의 독스트링은 클래스.__doc__ 형식으로 반환할 수 있고,
메쏘드의 독스트링은 클래스.메쏘드.__doc__ 형식이나 인스턴스.메쏘드.__doc__ 형식으로 반환할 수 있다.
"""