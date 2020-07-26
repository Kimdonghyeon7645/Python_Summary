try:
    ppap = input("ppap를 입력하세요: ")
    if ppap != "ppap":
        raise Exception("에잇! ppap가 아니잖아!")
    print(ppap)
except Exception as e:
    print("에러메시지 :", e)

"""예외발생:
예외를 직접 발생시킬 수도 있는데,

raise 예외이름("에러메시지")
raise 예외이름()
와 같이 사용하면, 해당에러가 발생(+ 원하는 에러메시지를 반환)되게 할 수 있다.

raise 는 try except 가 없는 상태에서도 사용할 수 있는데,
이렇게 예외를 발생시키면, 현재 코드블럭에서 처리해줄 except 를 찾을 때까지 계속 상위 코드 블록으로 올라가며,
결국에 처리해줄 except 가 없다면 코드 실행이 중지되고 에러가 표시됨.

이것을 이용해서 예외를 다시 발생(re-raise)시킬 수도 있는데,
"""


def input_ppap():
    try:
        ppap = input("ppap를 입력하세요: ")
        if ppap != "ppap":
            raise Exception("에잇! ppap가 아니잖아!")
        print(ppap)
    except Exception as e:
        print("함수에서 에러가 발생했네요. 에러메시지 :", e)
        raise


try:
    input_ppap()
except Exception as e:
    print("스크립트에서 예러가 발생했네요. 에러메시지:", e)
"""
이렇게 하면 except 안에서 raise 를 다시 사용했기에, 거기서 발생한 예외를 다시 발생시킨다.(re-raise)
그렇게 하면 상위 코드블럭의 except 를 찾아서 다시 발생한 예외를 처리하기에, 상위 코드블럭에서도 또한번 예외 처리가 된다. 

참고로 except 에서 raise 를 사용하면 이전에 발생한 똑같은 예외를 다시 발생시키지만,

raise 예외이름("예외메시지")
로 또다른 예외를 지정(새로운 에러 메시지도 추가)할 수 있다.
"""

ppap = input("또다시 ppap를 입력하세요: ")
assert ppap == 'ppap', "ppap가 아니잖아!"
print(ppap)
""" assert:
예외를 assert를 이용해 발생시킬 수도 있다.

assert 조건식
assert 조건식, "에러메시지"
와 같은 형식으로, 
지정된 조건식이 거짓일 경우에 AssertionError 를 발생시키며, (에러메시지를 추가했을 경우, 에러메시지도 함께 출력)
조건식이 참일 경우는 에러가 발생되지 않고 그냥 넘어간다.

(assert 는 디버깅 모드에서만 실행되며(파이썬은 기본적으로 디버깅모드(__debug__ == True)임)
(스크립트 파일에서 assert 가 실행되지않게 하려면, python -O 스크립트파일.py 과 같은 형식으로 실행(O는 영문대문자))
"""