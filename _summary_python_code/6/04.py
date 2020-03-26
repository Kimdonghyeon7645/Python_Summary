# 클래스(Class)
class Car:
    def __init__(self, speed, color, model):    # __init__ : 생성자(객체 생성시 값 초기화)
        self.speed = speed
        self.color = color
        self.model = model
    def drive(self):    #메소드 : 클래스내 함수(self는 객체의 이름이 들어감)
        self.speed = 60
    def __str__(self):    # __str__ : 객체를 print()로 출력할 때 자동 호출
        msg = f"속도: {self.speed}, 색상: {self.color}, 모델: {self.model}"
        return msg

myCar = Car(0, 'blue', 'Sonata')
momCar = Car(0, 'gray', 'Morning')
dadCar = Car(0, 'red', 'Avante')
print(myCar)
print(momCar)
print(dadCar)