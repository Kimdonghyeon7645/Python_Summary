import pprint   # pprint 모듈을 가져옴

pprint.pprint('haha')   # 모듈명.함수() 로 모듈에 있는 함수를 사용
# 참고로 import 문은 코드 중간에 사용해도 된다. 모듈과 패키지를 사용하기 이전에서라면 어디든지 사용가능
""" 모듈(module) 가져오기:
파이썬의 내장함수(built-in function)(ex> input, print)에서 넘어서서
복잡한 프로그램을 만들기 위해 모듈과 패키지를 불러올 수 있는데, 이때 import 키워드를 사용한다.

import 모듈 
import 모듈1, 모듈2, ...
으로 모듈을 사용하기 전에 가져온 다음,

모듈.변수
모듈.함수()
모듈.클래스()
으로 모듈에 있는 객체들을 활용할 수 있다.


import 모듈 as 이름
으로 모듈명을 그대로 입력하지 않고, 모듈명을 다른 이름으로 대체할 수도 있으며, 이럴땐

이름.변수  이름.함수()
등등 as 에서 정해준 모듈의 이름으로 모듈명 대신 사용할 수 있다.


from 모듈 import 변수
from 모듈 import 함수
from 모듈 import 클래스
등으로 모듈 전체를 가져오는 것이 아니라, 모듈의 일부만 가져올 수 있다.
이럴때는 모듈. 을 앞에 붙일 필요 없이 
변수  함수()  클래스() 
로 바로 활용 할 수 있다.

from 모듈 import 변수, 함수, 클래스
으로 여러개를 가져올 수도 있고,

from 모듈 import *
으로 모두 가져올 수도 있다. (이러면 앞에 모듈. 을 붙일 필요 없이 모듈의 모든 객체를 사용할 수 있다.)
그리고,

from 모듈 import 변수 as 이름
from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3
처럼 여기서도 as 문을 활용해서 가져온 객체를 원하는 이름으로 지정해 사용할 수 있다.
"""