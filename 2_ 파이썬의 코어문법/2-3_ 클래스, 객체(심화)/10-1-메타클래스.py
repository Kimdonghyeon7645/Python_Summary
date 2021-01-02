"""
메타클래스(metaclass)란 한 줄로 정의하자면 클래스를 만드는 클래스라고 할 수 있다.
대부분의 객체 지향 언어에서의 클래스는 어떻게 객체를 생성할지에 대해 정의할 뿐이지만, 파이썬에서의 클래스는 객체 그자체다.
그렇다. 파이썬에서의 클래스는 객체를 어떻게 생성할지 정의할 뿐 아니라 객체이기도 한 존재다.(너무 욕심이 많은 친구다...)
"class" 키워드를 사용할 때 Python이 실행하면 "객체"를 만들어 낸다. 다음 코드는 메모리에 ObjectCreator라는 이름의 객체를 생성한다.

"""
class ObjectCreator:
    pass


"""
이 객체(클래스)는 새로운 객체(인스턴스)를 만들 수 있다. 즉 클래스와 인스턴스는 모두 객체인데, 클래스는 인스턴스를 만드는 객체인 것이다.
클래스는 변수에 할당할 수도 잇고 복사할 수도 있고 새로운 속성을 추가할 수 있고 함수의 인자로 넘길 수 있다. 
"""

#클래스를 변수에 할당하는 경우
ClassVariable = ObjectCreator

#클래스를 함수의 매개변수에 전달하는 경우
print(ObjectCreator)

#클래스에 새로운 속성을 추가하는 경우
ObjectCreator.new_attribute = 'foo'

"""
우리가 아는 클래스를 만드는 방법은 class 키워드를 이용해 함수에서 클래스를 만드는 방법이다. 하지만 클래스는 객체기 때문에 그때그때 동적으로 
새로운 클래스를 만들 수 있는 방법이 존재한다. type 함수는 객체의 타입을 알 수 있는 함수인데, 완전히 다른 기능을 하나 더 가지고 있다.
type 함수는 클래스를 만들 때 사용할 수 있다. type은 인자로 클래스의 정의를 받아 클래스를 반환한다.(같은 함수를 인자에 따라 완전히 다른 용도로 사용되는데 
이는 매우 나쁜 방법이다. 여기에는 Python 하위 호환성 문제가 얽혀있다고 한다.)
"""

#class 키워드를 이용해 함수에서 클래스를 만든다
def create_class(name):
    if name=='Foo':
        class Foo():
            pass
        return Foo
    else:
        class Bar():
            pass
        return Bar
Foo = create_class('Foo')

#type 함수를 이용해서 클래스를 만든다.
#type(Class 이름, 상속할 클래스들의 튜블, 속성들에 대한 딕셔너리)
MyClass = type("MyClass", (ObjectCreator, Foo), {'attribute_name': "attribute_value"})
print(MyClass)

def my_method():
    print("my_method 실행")

MyMethodClass = type("MyMethodClass", (), {'my_method': my_method})
MyMethodClass.my_method()

# 동적으로 만든 클래스에 메소드 추가 (속성도 마찬가지로 추가 가능)
MyClass.my_method = my_method
MyClass.my_method()


"""
이제 파이썬의 class 키워드의 작동방법에 대해서 이해했다. 그리고 이방법은 metaclass를 사용할 떄에도 동일하게 작동한다.
그러면 최종적으로 metaclass란 무엇일까? 위에서 설명했듯, 메타클래스란 클래스를 만드는 클래스이다. 객체를 만들기 위해 클래스를 정의했는데
python 클래스는 곧 객체라는 것을 알았다. 메타클래스는 이러한 객체(클래스)를 만드는 무언가이다. type 함수는 실제로 파이썬 코드 뒤에서
클래스를 생성하는 메타클래스이다. type이 클래스인데 왜 소문자인지 물어본다면 아마 문자열 객체를 반환하면 str이나 정수 객체를 반환하는 int 클래스와 같은
이유일 것이다. 파이썬에서 모든 것은 객체로 표현된다. 정수, 문자열, 함수, 클래스 모두 객체다, 그리고 이 객체는 클래스로부터 생성된다.

"""
integer=32
print(integer.__class__) # <class 'int'>

string='string'
print(string.__class__) # <class 'str'>

def f(): pass
print(f.__class__) # <class 'function'>

class Bar(): pass
b = Bar()
print(b.__class__) # <class '__main__.Bar'>

""" 그렇다면, 클래스의 클래스를 살펴보자 """
print(integer.__class__.__class__) # <class 'type'>
print(string.__class__.__class__) # <class 'type'>
print(f.__class__.__class__) # <class 'type'>
print(b.__class__.__class__) # <class 'type'>

