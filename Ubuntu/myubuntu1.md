## My Ubuntu

#### Yes Ubuntu 1

```
커널 사용자 관련 명령어
adduser - 사용자 추가

adduser sunny1 : sunny1을 추가

adduser --uid 9999 sunny2: sunny2를 생성하고 id를 9999라고 함

adduser --gid 1000 sunny3 ; sunny3을 생성하고 그룹 id가 1000인 그룹에 추가

adduser --home /sunnyhome sunny4 : sunny4를 생성하고 홈 디렉토리를 sunnyhome으로 함

adduser --shell /bin/kkk sunny5 : sunny5를 생성하고 기본 셀을 /bin/kkk로 함

passwd : 사용자의 비밀번호를 변경

passwd sunny : sunny의 비밀번호를 지정(변경)

usermod : 사용자의 속성을 변경

usermod --shell /bin/ooo sunny5 : sunny5의 기본 셀을 /bin/ooo로 변경
usermod --groups ubuntu sunny5 : sunny5의 보조그룹에 ubuntu를 추가

userdel 사용자 삭제

-r : 홈 디렉토리까지 삭제

chage : 사용자의 암홀르 주기적으로 변경하게 설정

chage -l sunny1 sunny1의 설정 사항 확인

-m : 암호를 사용해야하는 최소일자 설정
-M : 암호를 사용해야하는 최대일자 설정
-E : 암호가 만료되는 날짜날짜를 설정
-W 암호가 만료되기 전에 경고하는 기간 ( 지정을 하지 않을 떄에는 7일)

groups : 사용자가 소속된 그룹을 보여줌

groupadd : 새로운 그룹 생성

groupmod : 그룹의 속성을 변경한다.

groupmod --new-name sunnys sunnyhome : sunnyhome 그룹의 이름을 sunnys로 변경

groupdel : 그룹 삭제

gpasswd : 그룹의 암호를 설정하거나 그룹관리를 수행
```

```
파일 유형
b(블록 디바이스) c(문자 디바이스) i(링크)

파일 허가권
r(읽기) w(쓰기) x(실행가능)

rw- r-- r-- (rw-는 소유자의 파일 접근 권한/r--은 그룹의 파일 접근 권한/r--은 그 외 사용자의 파일 접근 권한 )

r : 4 w: 2로 쓰임

ex ) 754 : rwxr-xr--으로 불리고 777은 모든 사용자가 읽고 쓰고 실행할 수 있는 파일로 만듬

whoami : 지금 사용자가 누구인가요?
./a : 현재 디렉토리의 a를 실행
하드 링크를 생성하려면 ln 링크대상이름 링크파일이름으로 명령 실행

하드 링크는 디렉토리에서 원본 파일이 없어져도 아무런 이상이 없지만 심볼릭 리으(소프트링크)는 디렉토리에서 원본 파일이 없어지면 연결이 끊김
```

```
dpkg = 파일을 설치하기 위한 명렁어 중 하나
*.deb를 사용하며 패키지라고 함

설치 : dpkg -i packagename.deb(-i = --install)

삭제 : dpkg -r packagename.deb ( -r = --remove)
      dpkg -p packagename.deb ( -p = --purge)
조회:  dpkg il packagename : 설치된 패키지에 대한 정보 보여줌
      dpkg -L packagename : 패키지가 설치한 파일 목록 보여줌
      dpkg --info packagename.deb: 패키지 파일에 대한 정보 보여줌
dpkg의 단점 : 의존성 문제가 있어 apt-get을 많이 사용 함

apt-get : 특정 패키지를 설치하고자 할 떄 의존성이 있는 다른 패키지를 자동으로 먼저 설치해주는 명렁어

apt-get -y install packagename / 설치 방법
apt-cache show packagename : 패키지의 정보를 화면에 출력
apt-cache depends packagename : 패키지에 대한 의존성 정보 출력
apt-cache rdepends packagename: 패키지에 의존하는 다른 패키지 보여줌
apt-get의 작동 방식
ex) apt-get install 입력 - /etc/apt/sources.list 파일을 열어서 URL 주소 확인 - 설치와 관련된 패키지 목록을 요청 - 설치와 관련된 패키지 목록만 다운로드 - 설치할 패키지와 관련된 패키지의 이름을 화면에 출력 - Y를 입력하면 설치에 필요한 패키지 파일 요청함 - 설치할 패키지 파일을 다운로드해서 자동 설치!

()폴더 - 인터넷 - 우분투 패키지 저장소)

종류 : main(공식적인 무료 소프트웨어)/universe(지원하지 않은 무료 소프트웨어)/restricted(공식적인 유료 소프트웨어)/multiverse(지원하지 않은 유료 소프트웨어)
