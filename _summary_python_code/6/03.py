# 클래스(Class)
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
