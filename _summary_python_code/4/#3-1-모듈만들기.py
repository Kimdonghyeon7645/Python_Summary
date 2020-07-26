import hi_module

print(hi_module.hi)     # hi_module 의 변수 hi 를 사용
hi_module.hello()       # hi_nodule 의 함수 hello() 를 사용
h = hi_module.Hey()     # hi_module 의 클래스 Hey() 를 사용(인스턴스 생성)

h.hey()         # hi_module 의 Hey() 클래스 메쏘드 hey() 를 사용
print(h.ha)     # hi_module 의 Hey() 클래스 속성 ha 를 사용
"""
사용자가 직접 모듈을 만든다면, 간단하게 .py 로 끝나는 파일을 저장한 후, 다른 곳에서

import 파일이름
으로 그 파일을 모듈로써 가져올 수 있다. 
그러면 그 모듈(파일)의 변수, 함수, 클래스 같은 것들을 모듈처럼 사용할 수 있는 것이다.
(모듈을 가져와 사용하는 것에 대해서는 #2-1, 모듈 가져오기 의 내용과 동일하다.)
"""
