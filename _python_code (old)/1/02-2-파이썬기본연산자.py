"""
블로그포스팅 : https://bodhi-sattva.tistory.com/62
"""

a = 10
b = 6
print(a + b, a - b, a * b, a / b, a ** b, a // b, a % b)
"""산술연산자
사칙연산(+,-,/,*)말고도 제곱(**), 몫(//), 나머지(%)연산자도 있다.
"""

a += 10
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 2
print(a)
a **= 2
print(a)
a //= 10
print(a)
a %= 2
print(a)
"""대입연산자
익히 쓰는 단순대입(=) 오른쪽피연산자를 왼쪽 피연산자에 대입(copy)
산술연산자가 붙어 두 피연산자를 산술연산한 후의 값을 대입하는 연산자다. 
"""

print(a > b, a < b, a >= b, a <= b, a == b, a != b, a > b > 1)
"""비교연산자
둘의 관계를 부등호나 등호로 확인해서 참인지 거짓인지를 반환하는 연산자다. (한번에 두 비교연산자도 사용가능하다)
"""

b1 = 0b1010  # 2진수 1010
b2 = 0b0101  # 2진수 0101
print(b1 & b2)
print(b1 ^ b2)
print(b1 | b2)
print(~b1)
print(b1 << 1)
print(b1 >> 1)
"""비트연산자
게이트회로에서 봤던 불대수 논리함수(and, or, not, xor)를 비트단위로 수행하는 연산자다.
"""

bo1 = True
bo2 = False
print(bo1 and bo2)
print(bo1 or bo2)
print(not bo1)
"""논리연산자
논리함수(and. or, xor)를 비트단위가 아닌, 값과 값 단위로 수행하는 연산자다.
&&, ||, ^^같은 형식과 다르게 영어로 and, or, not을 사용한다.
"""

yo = 1
print(yo in [1, 2, 3])
print(yo not in [1, 2, 3])
print([1, 2] in [1, 2, 3])
"""맴버연산자
in 으로 왼쪽 값(요소)이 오른쪽 값(요소들)중에 있는지 참거짓으로 반환한다.
"""

n1 = 256
n2 = 256
print(id(n1), id(n2))
print(n1 is n2)
print(n1 is not n2)
"""식별연산자
is, is not 으로 둘이 같은지 아닌지를 구분한다. 정확히는 둘의 메모리 위치를 비교한다.
"""

t1 = 4
t2 = 5
print("짝수" if t1 % 2 == 0 else "홀수")
print("짝수" if t2 % 2 == 0 else "홀수")
"""삼항연산자
[참일때값] if [조건문] else [거짓일때값] 으로 if else 문과 같은 분기문을 구현할 수 있다. 
차이점은 if else 에 따른 실행문이 아니라, 지정해준 값이 반환된다.
"""
