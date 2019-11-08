## flask 관련 정리

#### python & flask


1. python 가상 세팅..

```
pyenv / virturalenv

pyenv : python의 여러 버전을 설치하고 관리를 할 수 있게 해주는 버전 매니저!!
virtualenv: 로컬에 다양한 파이썬 환경을 구축할 수 있도록 함 => 쉽게 말해 또다른 가상공간에 파이썬을 사용하여 그 공간에서만 사용할 수 있게 해줌(pip도 그 공간마다 설치해야함!)
autoenv : 스크립트를 이용해서 (가상환경으로 설정한) 특정 프로젝트 폴더로 들어가면 .env파일을 찾아서 자동으로 개발 환경을 로딩

pyenv 사용법

리눅스 경우 ... curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash를 이용해서 설치!

나오는 메세지를 복사하고 ~/.bashrc or ~/.bash_profile에 넣음

그리고 유닉스 계열(linux 계열 / mac)의 경우에는
alias python=python3
alias pip=pip3
를 넣어준다.
(유닉스 게열의 경우 기본 구성으로 파이썬 2.x가 python으로 구성되어 있기에, 3.x대 버전은 python3으로 명렁어가 되어 있으므로!)

pyenv에 패키지를 다 설치하여 준비함(이용하기 위한 패키지)
make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev를 모두 설치한다.

pyenv 명령어
pyenv install --list (python 설치 가능한 버전 리스트)
(ex: pyenv install 3.7.x로 설치)
pyenv versions를 이용했을 시 *로 되어 있는 것이 default 값임

pyenv global x.x.x를 하면 버전이 확인 될 거임!
그리고 pyenv를 쓰는 이유는 기본 설치한 파이썬이 협업을 할 때에 버전이 다를 수 있어.. pyenv를 이용해서 버전을 맞춰서 쓸 수 있기 떄문임!

pyenv-virtualenv

설치 방법 1
pyenv virtualenv <version> <env_name>을 이용!

폴더로 이용 후 ! -> pyenv local name-env 사용(해당 폴더에 특정 가상환경을 적용)

설치 방법 2
virtualenv를 설치 -> pip install virtualenv를 확인 -> virtualenv venv를 하면 venv라는 파일이 생김-> source venv/bin/activate로 시작 -> 종료는 deactivate

virtualenv 버전 바꾸는 법
ex1) virtualenv venv --python=python3.7
ex2)alias python='/usr/bin/python2.7'(~/.bashrc 또는 ~/bash_profile 이용 )

virtualenv 패키지 가져오기!
virtualenv venv --system-site-packages

pip freeze
다른 사람과의 협업에서 혹은 새로운 개발환경에서도 쉽게 같은 환경으로 동기화하기 위해 많이 사용

pip freeze > requirements.txt를 이용해서 설치되어 있는 python 패키지를 기록에 남긴다.

pip install -r requirements.txt를 이용해서 requirements.txt에 있는 패키지를 가상 파이썬에 설치를 해줌. (requirements는 보통 사용되는 이름, 같은 가상환경 버전에서 사용하는 것을 권장)
```

2. flask setting 및 개념 설명

```
flask를 1달 정도 사용해보면서, 자료의 부족으로 인해 정리를 해둡니다.

flask는 python의 프레임워크 중 하나로 정말 가볍고 자유도가 높다는 특성을 가지고 있음..

설치
flask는 pip install flask를 이용하여 설치를 합니다.
flask에는 여러가지 라이브러리 등이 있음
1. request : get 방식으로 받을 때 request.args.get() 등을 이용함.
2. redirect : url로 보낼 때 많이 사용하며, return redirect(x, code='200')으로 되어있다면 x라는 곳으로 가며, 200을 받으면 끝난다고 생각하면 쉬움
3. url_for : html에서 url_for을 사용을 많이하며, url_for을 이용하면 파일명과 파일주소를 쉽게 설정할 수 있음
4. render_template : html로 값 등을 렌더링(전달?) 하기 위해 사용하며, render_template('index.html', a=a) 라면 index.html로 전달하고 python에서의 a변수가 html에서 a로 쓰인다는 것임 !

사용
init.py / app.py 등으로 많이 기본파일을 사용함

app = Flask(__name__)으로 설정을 많이함..
@app.route('/') => 라우트이며, /로 가게 됨!

if __name__=='__main__':
  app.run(host='주소', port=사용할 포트 명, threaded=True) 등을 사용하며, app.run이 있어야 terminal에서 python3 app.py를 할 때 실행 할 때 주소로 연결을 할 수 있음 그리고 외부연결을 위해서는 0.0.0.0을 사용하여 접속하고 있음

다른 파이썬 파일에서 함수를 가져올 때는
from 파일명 import * (전체 함수 / *가 a 일경우 함수 a만을 가져온다는 것임!)

html!

flask가 html에서 쓰일 때는 {{}} 구조인 jinja2를 사용하며, Django에서도 사용됨

{{}}에 변수가 들어가 있으면 flask에서 ex) render_template('a.html', a=a)가있으면 a를 보내서 {{}}에 넣어주면 해당값이 html에서 보여짐!

{% if, for %} 등을 사용가능하며, endfor endif 등으로 닫아줘야 문법 오류가 없이 사용이 가능함!

패키지
flask는 기본 내장 패키지가 다른 프레임워크보다 적다보니.. pip로 다운받아 사용하는 것이 많음
(나중에 따로 소개!)

파일:
flask 는 크게 기본 파일 위치 안에 static , templates 등이 같이 저장되며, static 안에는 css, js, img, font 등을 저장하며, templates에는 html을 저장해서 render_template에서 뽑아오는데 사용하며, url_for을 이용해서 css나 js, img 등을 뽑을 때는 static을 사용해서 설정하므로 기본 세팅을 이와같이 해야함

flask 같은 경우, 자료가 부족하여 stackflow, google 등에서 영문으로 나오는 것이 많다보니, 어려운 점이 있지만.. 적응을 하면 한 없이 좋을 프레임워크이며, 구성되어 있는 것이 적은만큼 이해를 하고 사용하면 매우 활용성도 좋을 것이다. 
