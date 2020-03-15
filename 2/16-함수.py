# 함수(명명규칙, 소문자+언더스코어)
def sum_mul(a, b):
    return a + b, a * b
# 튜플에서 배웠듯이 반환 값이 여러개면 튜플로 반환


result = sum_mul(3, 4)
# result = (7,12)
sum, mul = sum_mul(3, 4)
# sum = 7, mul = 12
print(result, sum, mul)
