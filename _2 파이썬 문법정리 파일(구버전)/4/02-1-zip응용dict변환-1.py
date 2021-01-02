# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 말고 아래의 리스트 내포를 사용
keys = [i for i in range(1, 11)]
# values = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
values = [2**i for i in range(1, 11)]
myzip = zip(keys, values)
mydict = dict(myzip)

print(mydict)

"""zip함수 dict응용:
zip의 인자가 2개라면, 2개씩 묶어주기 때문에, dict()함수를 통해
딕셔너리 자료형을 쉽게 변환할 수 있다.
"""
