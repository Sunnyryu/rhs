## My Ubuntu

#### Ubuntu 6

```
원격자 시스템 관리

서버에 접속하려면 꼭 클라이언트 프로그램에 접속해야함
서버와 클라이언트가 같은 OS여야 하는 것은 아님
웹서버 - 웹 클라이언트
텔넷 서버 - 텔넷 클라이언트
FTP 서버 - FTP 클라이언트
VNC 서버 - VNC 클라이언트
SSHD 서버 - SSH 클라이언트
오라클 서버 - 오라클 클라이언트

텔넷

텔넷 서버 설치  - 설정 파일 편집 - 텔넷 전용 사용자 생성 - 텔넷 서비스 가동 - 방화벽 설정(포트열기) - 클라이언트 접속
(apt-get install xinetd telnetd - /etc/xinetd.d/telnet - adduser. 사용자명 - systemctl restart xinetd - ufw allow 23/tcp)

OPENSSH 서버

텔넷에 비해 보안이 강화됨.
데이터 전송시 암호화가 되어 있음

SSH 서버 설치/가동 - 방화벽 설정 - 리눅스 클라이언트 접속
(apt-get install openshh-server - ufw allow 22/tcp - ssh 사용자명@서버ip)

VNC 서버

그래픽 모드로 원격 관리를 지원하는 VNC서버 사용
별도의 클라이언트 프로그램 필요
텔넷에 비해 느림

VNC 서버 설치 - 서버 설정 파일 수정 - VNC 서비스 가동 - 방화벽 설정 - VNC 클라이언트설치 - VNC 클라이언트 실행 - 해상도 조절
(apt-get install vnc4server - xstartup - vncserver : 1 - ufw allow 5901/tcp- apt-get install xfghlvncviewer - vncviewer (ip) <번호> - Options 의 Color level)
```


```
네임서버
네임서버는 DNS(DOmain Name System) 서버라고도 하며,실제 원하는 서버에 접근하려면 URL을 해당 컴퓨터에 IP 주소로 변경해야 하는데 DNS 서버가 담당함
nslookup : name server 와 관련한 조회를 할 수 있는 명령어
네임서버를 주석처리하면 홈페이지를 들어갈 때 접속이 안됨. (그렇지만 ip주소로 들어가면 가능함)

URL 입력 - /etc/host.cont 조회 - /etc/host - (있다면 ip주소 획득)
- (없다면 /etc/resolv.conf로 감  ) - (네임서버 설정이 없으면 호스트 이름을 알수 없음) - (네임서버 설정이 존재하면 질의를 하고 이 때 응답이 있다면 ip 주소를 획득하지만 응답이 없다면 호스트 이름을 알 수 없음)

웹 브라우저는 최종적으로 얻은 IP주소가 진짜 IP 주소든 가짜 IP 주소든 검증할 능력이 없고 네임서버나 호스트 파일에서 알려준 IP 주소로 접속을 시도함

네임서버 구축

도메인 이름 체계

Root라는 네임서버(도메인)가 있을 때
1단계 네임서버인 com,net,org,edu 등의 네임서버와 kr, fr, us 등의 국가 도메인을 관리하며 밑의 1단계 네임서버들이 2단계 네임서버를 관리하는 방식으로 관리를 한다.

로컬 네임 서버

리눅스에서는 네임 서버가 nameserver IP 주소 형식으로 설정되어 있는데 이 것을 로컬 네임서버라고 함

예를 들어 주소창에 네이벌르 입력했고 로컬 네임 서버를 확인 후에 질의를 하여 로컬 네임서버로 넘어간다. 그 후에 자신의 캐시 DB를 검색하여 정보가 있다면 응답 받는다. 허나 없다면 최상위인 Root 네임서버, 1단계 네임서버, 2단계 네임서버에 질의를 하여 응답을 받는다.
그리고 2단계에서 캐시 db에 있다면 2단계 네임서버가 캐시 db의 정보를 받아 응답해줄 것이고 이것을 PC에 응답을 해줘 PC에서 획득한 IP 주소로 웹 서버를 접속함

캐싱 전용 네임 서버

캐싱 전용 네임서버는 PC에서 URL로 IP 주소를 얻고자 할 때 URL의 IP 주소를 알려주는 서버임

bind9, bind9utils를 이용하여 모든 컴퓨터가 네임 서버를 사용할 수 있게 해주는 것임(가상 공간에 같이 있는 네트워크 주소)

포워드 존 파일의 문법
; = 주석
$TTL = TIme TO Live (질의해간 다른 서버가 해당 ip 주소를 캐시에 저장하는 시간)
@ = 정의된 com을 의미함
IN = 클래스 이름으로 인터넷
SOA = Start Of Authority(권한의 시작)
NS = Name server
MX = Mail Exchanger (메일 서버 컴퓨터를 설정)
A  = 호스트 이름에 상응하는 IP 주소
CNAME : 호스트 이름에 별칭을 부여할 때 사용

역병향으로 다루는 것은 리버스 존이라고 함

라운드 로빈 방식의 네임 서버

여러 대의 웹서버를 운영해서 교대로 서비스를 실행하고 웹 서버의 부하를 공평하게 여러 대가 나누는 방식
```
