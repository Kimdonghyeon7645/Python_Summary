# 예외 처리
try:
    int('10')
except:
    print("예외 발생!")
else:
    print("예외가 발생 안함!")

""" 예외처리에서 else, finally:
try 문에서 반대로 예외가 발생하지 않았을 때 코드를 실행하는 else: 문도 있다.
else 는 except 바로 다음에 오며, except 를 생략하고 else 문을 사용할 수 없다.
"""
try:
    int(input())
except:
    print("예외 발생!")
else:
    print("예외가 발생 안함!")
finally:
    print("예외처리가 끝났습니다.")

"""
또한 finally: 문으로 에외가 발생하는지 말든지 마지막에 실행할 코드를 쓸수 있다.
finally: 문은 except 와 else 문을 생략하고도 사용할 수 있는데,

except 가 실행되든지, else 가 실행되는지,
finally 문이 있으면 마지막에 항상 finally 문을 실행한다.
"""