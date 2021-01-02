# 예외 처리
try:
    print(ppap)
except:
    print("예외 발생!")

""" 예외(exception)처리:
예외란, 코드를 실행중에 발생한 에러를 말하며, 예외에도 다양한 종류가 있는데(ex> TypeError, NameError,...)
이러한 예외가 발생했을때 원래처럼 에러를 띄으며 스크립트 실행을 중단하지 않고,
계속실행하게 해주는 방법이 바로 '예외처리'다.

예외 처리는 try except 문을 사용해서 
# try:
#     실행할 코드
# except:
#     예외가 발생했을 때 처리하는 코드
위같은 형식으로 예외처리르 할 수 있으며, try: 안의 코드에서 예외가 발생하면, except: 안의 코드를 실행한다.
이때 try: 코드중 예외가 발생하면 해당 줄에서 코드실행을 중단하고(그 아래 코드들은 무시된다) 
바로 except: 안의 코드를 실행한다.

except 에 예외 이름을 지정해서 특정 예외가 발생했을 때만 처리코드를 실행하도록 할 수 있는데,
except: 를 except 예외이름: 과 같이 나타내면된다. (ex> except IndexError: )
except 예외이름: 은 예외 이름의 종류에 따라서 여러개를 사용할 수 있다.
"""
try:
    a = int(input())
    print(10 / a)
except ZeroDivisionError:   # 입력받은 값이 0이면 0으로 나눌때의 에러
    print("숫자를 0으로 못나눠요.. ㅡㅡ")
except ValueError:      # 입력받은 값이 숫자로 변환할 수 없을때의 에러
    print("숫자가 아닌 값을 입력했네요.. ㅡㅡ")

"""
예외처리에서 except 에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아 올수도 있다.

except 예외이름 as e:
같이 하면, (변수이름으로 보통 예외(Exception)의 앞글자를 딴 e를 사용)
e 변수에서 에러 메시지가 담기게 된다.

그리고 e 변수를 type()함수의 인자값으로 넘기면, e 변수에 담긴 에러메시지에서 에러의 종류를 반환할 수 있다.

만약 모든 예외의 에러 메시지를 가져오고 싶다면 

except Exception as e:
와 같이 하면 된다.  
"""
try:
    int('python')
except NameError as e:
    print(e)
    print(type(e))
except ValueError as e:
    print(e)
    print(type(e))

# 참고로 예외도 클래스 상속으로 구현되고, 여러 개충으로 구현되어 있다.
# 나중에 새로운 예외를 만들 때는 Exception 을 상속받아서 구현한다.
