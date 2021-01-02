summary = """
파이썬 패키지 인덱스에서 패키지 설치하기:

(방법도 종류가 있는데, 파이참 Settings > Project: (프로젝트이름) > Project Interpreter 에서 설치하거나,
명령 프롬프트(콘솔, 터미널)에서 설치하는 방법이 있다. 여기선 명령 프롬프트로 설치하는 법에 대해 알아본다.)

우선 pip(파이썬 패키지 인덱스의 패키지 관리 명령어)를 설치해야 한다.
윈도우용 파이썬은 기본적으로 깔려있기에 할 필요 없고, 리눅스, macOS 에서만 pip 를 따로 설치해야 한다.
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
위 명령어를 콘솔(터미널)에 치면 되는데, 만약 curl 도 설치되있지 않으면,
우분투 : $ sudo apt-get install curl
CentOS : $ sudo yum install curl
같은 방법으로 설치한다.


그리고, 
$ pip install 패키지이름
으로 원하는 패키지를 설치하면 된다. (윈도우는 명령 프롬포트에서, 리눅스, 맥에서는 콘솔(터미널)에서)


마지막으로 다른 패키지 처럼 
파이썬 스크립트 안에서 install 패키지 
형식등으로 설치한 패키지를 가져와서 사용하면 된다.


참고로 파이썬 버전이 2와 3모두 깔려 있다면, (보통 리눅스와 macOS 는 같이 깔려있음.) 
python2(python) 에서는 pip2(아니면 pip)로 명령을 사용하고,
python3(python3) 에서는 pip3(아니면 pip)로 명령을 사용한다. 
(파이썬 3만 깔려있으면 pip 가 파이썬 3 용 명령으로 쓰임.)


* pip 에 대한 추가 명령어
$ pip search 패키지    -> 패키지 검색
$ pip install 패키지==버전    -> 패키지를 특정 버전으로 설치
$ pip list 아니면 $ pip freeze    -> 패키지 목록 출력
$ pip uninstall 패키지    -> 패키지 삭제
"""
print(summary)