"""
블로그 포스팅 : https://bodhi-sattva.tistory.com/66
"""

# -*- coding: utf-8 -*-
"""문자열 함수 정리:
03-2에서 본 함수 말고도 문자열함수는 꽤 많다. 그래서 새로 정리했다.
(출처 : https://simplesolace.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EB%AC%B8%EC%9E%90%EC%97%B4 )
(출처의 문자열함수는 파이썬 2버전 정도를 기준으로 작성했단다)
"""
''' 1. 대, 소문자 변환 :
.upper()  문자열을 대문자로 변환
.lower()  문자열을 소문자로 변환
.swapcase()  문자열을 대소문자 반전
.capitalize()  문자열의 첫문자를 대문자로 변환
.title()  단어들의 첫문자를 대문자로 변환  
'''

''' 2. 검색:
.count('~')  문자열에서 ~가 들어간 횟수 반환

* 2-1. find() 함수와 index() 함수
.find('~')  문자열에서 ~가 있는 위치(인덱스)를 왼쪽우선으로 반환
.find('~', n)  문자열에서 ~가 있는 위치를 왼쪽우선으로 n번째 위치(인덱스)를 반환 
.rfind('~')  문자열에서 ~가 있는 위치(인덱스)를 오른쪽우선으로 반환
.index() 함수도 find() 와 같은 일 수행, 
.index('~', n), 
.rindex() 도 이와 같음
# 둘의 차이점은 찾는 문자열이 없을경우 find()는 -1을, index()는 에러를 반환 

* 2-2, startswith() 함수와 endswith() 함수
.startswith('~')  문자열이 ~로 시작하는 문자열인지 참또는 거짓 반환
.endswith('~')  문자열이 ~로 끝나는 문자열인지 참또는 거짓 반환
# 두 함수 모두 두번째 매개변수(n)을 넣어 n번째 인덱스 부터 찾을 수 있고, 
# 세번째 매개변수(m)을 넣는다면, n~m번째 인덱스 사이에 있는 문자열을 찾을 수 있음
<ex> endswith('~', 0, 3),  .startswith('~', 6)
'''

''' 3, 바꾸기, 제거:
.replace('~', '..')  문자열에서 ~를 ..로 변경
.expandtabs(n)  탭(\t)을 n자 공백으로 변경, 매개변수 없을시 8자 공백으로 변경
.rstrip('~')  오른쪽 ~ 제거, 매개변수 없을시 공백제거
.lstrip('~')  왼쪽 ~ 제거, 매개변수 없을시 공백제거
.strip('~')  좌우에있는 ~ 제거, 매개변수 없을시 공백제거
'''

''' 4. 분리, 결합:
.split('~')  문자열에서 ~기준으로 분리(문자열1개 -> 문자열여러개), 매개변수 없을시 공백 기준으로 분리
.split('~', n)  왼쪽에서부터 n번 만큼 ~기준으로 분리
.rsplit('~', n)  오른쪽에서부터 n번 만큼 ~기준으로 분리
.splitlines()  라인(\n) 단위로 분리
'~'.join(strs)  리스트나 여러개의 문자열(strs 변수)를 ~를 틈새에 넣어서 결합(문자열여러개 -> 문자열1개)    
'''

''' 5. 정렬:
.center(n)  n만큼 가운데 정렬
.ljust(n)  n만큼 왼쪽 정렬
.rjust(n)  n만큼 오른쪽 정렬
# 위의 세 정렬 함수에서 두번째 매개변수로 '~'(문자열)을 넣어준다면, 정렬후 공백을 문자로 채울 수 있다.
.zfill(n)  n만큼 오른쪽 정렬 후 공백을 0으로 채움
'''

''' 6. 구성 문자열 판별:
.isdigit()  문자열에 숫자 있는지 참 또는 거짓 반환
.isalpha()  문자열에 영문자 있는지 참 또는 거짓 반환
.isalnum()  문자열에 숫자 + 영문자 있는지 참 또는 거짓 반환
.islower()  문자열에 소문자 있는지 참 또는 거짓 반환
.isupper()  문자열에 대문자 있는지 참 또는 거짓 반환
.isspace()  문자열에 공백(화이트 스페이스) 있는지 참 또는 거짓 반환
.istitle()  단어 첫글자마다 대문자인지 참 또는 거짓 반환
'''

''' #, string 모듈:
# import string 하고 사용하면됨, 임의의 문자가 어떤 종류인지 판별할 때 활용할 수 있다.
string.digits == '0123456789' (0~9, 10진수 숫자)
string.octdigits == '01234567' (0~7, 8진수 숫자)
string.hexdigits == '0123456789abcdefABCDEF' (0~F, 16진수 숫자)
string.letters == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' (영문자)
string.lowercase == 'abcdefghijklmnopqrstuvwxyz' (소문자)
string.uppercase == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' (대문자)
string.puctuation == '!"#$%…' (특수문자)
string.printable (인쇄 가능한 문자 모두)
string.whitespace (공백 문자 모두, 8진수 형식임)
<ex> ch in string.digits -> (참 또는 거짓 반환됨)
'''
