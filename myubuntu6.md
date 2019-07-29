## My Ubuntu

#### 웃으면서 정리해 !

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
