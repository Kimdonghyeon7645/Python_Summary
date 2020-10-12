class Car:
    def __init__(self, speed, color, model):
        print("생성자 호출")
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

    def __del__(self):
        print("소멸자 호출")


myCar = Car(0, 'blue', 'Sonata')
print(f"자동차의 속도는 {myCar.speed}km/h")
print(f"자동차의 색상은 {myCar.color}")
print(f"자동차의 모델은 {myCar.model}")
myCar.drive()
print(f"자동차의 속도가 올라서 현재는 {myCar.speed}km/h 입니다.")


""" 생성자(constructor), 소멸자(destructor):
생성자는 클래스의 인스턴스(객체)를 생성할 때 파이썬에서 자동으로 호출되는 함수다. 
객체를 생성하면서 초기화 작업을 바로 생성자 안에서 할 수 있으며, 문법은

def __init__(self):
    코드
    
와 같다. __init__ 의 매개변수를 추가해서, 객체를 생성할 때 인자값을 전달 받을 수 있다.
생성자에서 인스턴스 속성들을 생성하게 되는데, 생성하는 속성들의 값을 전달받은 인자값으로 처리해 줄수도 있다. (위 코드 참고)

소멸자는 반대로 클래스의 인스턴스(객체)가 소멸될 때 파이썬에서 자동으로 호출되는 함수다.
del 인스턴스 와 같이 인스턴스를 소멸시키거나, 프로그램이 끝나서 자동으로 인스턴스가 소멸되는 때에 자동으로 호출되며.

def __del__(self):
    코드
    
와 같은 문법이다. 생성자와 소멸자 모두 __가 메쏘드 앞뒤에 붙게 되는데, 이러한 메쏘드들을 스페셜 메쏘드, 매직 메쏘드라 한다.

"""
# (스페셜 메쏘드, 매직 메쏘드에는 이것말고도 많은 메쏘드가 있으며, 파이썬에서 중요한 문법중 하나다. 이부분에 대해서는 다음 파일 참고.)
