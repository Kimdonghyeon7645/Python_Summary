from urllib import request

response = request.urlopen('https://dojang.io/mod/page/view.php?id=2442')
""" 패키지 가져오기:
마찬가지로 패키지와 그 안의 모듈도 import 로 가져옴.

import 패키지.모듈
과 같으며, as from import 문도 동일하게 사용가능,

추가로는, 
from 패키지 import 모듈 
from 패키지.모듈 import 객체
와 같은 형식도 사용가능.

(from 상위요소 import 하위요소
라는 형식만 지키면, 왠만한건 되는듯.)
"""