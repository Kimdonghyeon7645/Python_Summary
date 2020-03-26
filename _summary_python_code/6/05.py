# 예외 처리
try:
    int('python')
except NameError as e:
    print(e)
    print(type(e))
except ValueError as e:
    print(e)
    print(type(e))

# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...

