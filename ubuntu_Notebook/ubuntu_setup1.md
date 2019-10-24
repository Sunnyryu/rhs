## setup1

1. 우분투에서 자바 설치하기

```
root 권한으로 들어가서 로그인 하기
  sudo su  + 비밀번호 입력
jdk 검색
  apt-cache search jdk
open jdk 11 설치
  apt-get install openjdk-11-jdk

javac 나 java 이용하여 버전 확인 하기
  javac -version or java -version
```
![Deepin스크린샷_select-area_20190911084326](https://i.imgur.com/s0yeEk9.png)
```
java 환경변수 설정
  vi /etc/bash.bashrc (vim 에디터를 이용해서 bash.bashrc 파일로 들어감)
  맨 아래 줄에 export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
  (export 하여 변수 JAVA_HOME 위치 설정)
  source /etc/bash.bashrc (bash 파일 적용)
```
![Deepin스크린샷_select-area_20190911084623](https://i.imgur.com/feUGuCX.png)
```
eclipse 설치
  www.eclipse.org 로 들어가서 eclipse ide java develop 설치

  설치 후에 tar.xz 파일 압축을 품

terminal로 eclipse 실행
  eclipse 파일로 넘어가서 ./eclipse로 실행
```

2. 우분투에서 python 설치 (추후 terminal 이미지도 추가할 예정~~)
```
우분투를 설치 할 때에 소프트웨어를 설치하는 체크박스에 체크를 하면 python3가 자동적으로 설치되어 있고
이 것을 삭제하면 시스템이 붕괴될 수 있기에 pyenv, pyenv-virturalenv를 사용하여 개발환경을 구축해야 함!
(버전이 다르면 관리하기가 어렵기에 ^_^)

먼저 패키지 관리자가 설치가 안되어 있다면 해줘야함 ㅠㅠ

pyenv : 파이썬 버전 관리 시스템
virtualenv, pyenv-virtualenv : 가상환경은 프로젝트별로 설치된 패키지들간의 충돌을 막아주기 위해 필요

1. curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash 을 이용하여 설치를 해줌!!

2. 설치를 하면 아래의 메시지가 나오는데 복사한다.
export PATH="/home/lhy/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
echo "export PATH=\"${PYENV_ROOT}/bin:\$PATH\""
     echo "eval \"\$(pyenv init -)\""
     echo "eval \"\$(pyenv virtualenv-init -)\""


3. .bashrc 파일에 2번 메세지(3줄)를 맨 아래 넣어줘야 하므로 vi ~/.bashrc를 실행시켜 넣어줌

4. 설치가 다 된다면 터미널을 재시작함

5. 그리고 pyenv를 이용하기 전에 밑의 패키지를 다 설치해줌
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

6. 그 후 pyenv를 친 후에 가능한 list를 보는 것은 pyenv install --list 이며, 기본 작동 확인 용이므로 3.7.4를 설치함 (pyenv install 3.7.4)

7. pyenv versions를 이용해서 버전을 확인하며 *로 된것이 현재 default 값임(git branch와 비슷한 느낌)

8. pyenv global 3.7.4를 친 후에 버전 확인
```

```
pyenv-virtualenv

1.pyenv virtualenv <version> <env_name>을 이용하여 가상환경을 생성해준다.
ex) virtualenv 3.7.4 name-env

2. 폴더 지정
cd ~/
mkdir exname
cd exname
mkdir name
cd name

3. pyenv local name-env 사용 (해당 폴더에 특정 가상환경을 적용)

4. pyenv versions 명렁어로 확인

5. pip list로 가상환경 패키지 목록 확인
```

3. mariadb 설치

```
우분투 18.04를 포맷 시키고 다시 우분투에 있는 패키지로 받으려고 보니 10.1 버전이라서 홈페이지 받아야 할 것 같음..

http://mariadb.org 에 들어가면 행복하게도 오픈소스라 다운로드를 무료로 받을 수 있음

https://downloads.mariadb.org/mariadb/repositories/#distro=Ubuntu&distro_release=bionic--ubuntu_bionic&mirror=kaist (제가 사용한 미러)에 들어가면 운영체제 / 운영체제의 버전 / mariadb 버전 / 미러 까지 고를 수 있다.

다 완료하면 밑의 코드가 나오니 터미널에 치게 되면 기존에 있던 10.1 버전이 아닌 위에서 고른 버전을 설치할 수 있음

sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://ftp.kaist.ac.kr/mariadb/repo/10.4/ubuntu bionic main'

그리고 난 후에 아래 내용을 터미널에 작성을 함
sudo apt update
sudo apt install mariadb-server
sudo apt install mariadb-client

그러면 10.4 버전이 설치된 것을 확인 가능

그리고 만약에 외부에서 접속을 허용하게 한다면
systemctl start mysql / systemctl status mysql 을 친 후에

firewalld 패키지를 설치 후에 firewall-cmd --permanent --add-port=3306/tcp && firewall-cmd --reload를 쳤을 때 success가 나오면 완료됨..
```
