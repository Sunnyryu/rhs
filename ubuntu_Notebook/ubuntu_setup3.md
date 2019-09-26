## setup3

1. ubuntu에 telnet 설치


1) telnet 설치 방법
1_ 패키지 설치
apt-get install telnetd, xinetd
(telnet이 안깔려 있다면 같이 설치!)

![Deepin스크린샷_select-area_20190916181624](https://i.imgur.com/rzAuhhA.png)

2_ telnet 설정 파일 만들어서 설정하기

vi /etc/xinetd.d/telnet - 이용해서 편집

![Deepin스크린샷_select-area_20190916181750](https://i.imgur.com/2YzJplY.png)

3_ xinetd 재시작 및 가동 및 상태 확인
systemctl restart xinetd
systemctl enable xinetd
systemctl status xinetd

- 만약 문제가 있다면 에러가 날 수 있으므로 telnet을 다시 설치하거나 vi 부분을 다시 확인

4. 방화벽 허용
- ufw allow 23/tcp (이미 있다면 존재하는 규칙을 건너뛸 것임)

5. telnet 작동
- telnet 서버ip주소
- whoami (누군지 확인 시켜주는 것)
- exit (종료)
```
다른 서버로 접속
```
![Deepin스크린샷_select-area_20190916182207](https://i.imgur.com/HmEaNgH.png)
```
문제가 없을 시에 뜨는 것
```
![Deepin스크린샷_select-area_20190916182154](https://i.imgur.com/IhyUhxD.png)

2. openssh 설치

1) ssh 서버 설치 및 가동
- apt-get install openssh-server
- systemctl restart ssh
- systemctl enable ssh
- systemctl status ssh
```
정상 작동 시 !
```
![Deepin스크린샷_select-area_20190916182825](https://i.imgur.com/XvZJJOg.png)

2) 방화벽 설정
- ufw allow 22/tcp

3) 사용법
- ssh 사용자이름@호스트이름 or 사용자이름@서버ip주소
```
암호를 입력하고 다른 서버에 접속 한 것!
```
![Deepin스크린샷_select-area_20190916183243](https://i.imgur.com/5U978eH.png)

3. VNC 서버
1) 패키지 설치
- apt-get -y install gnome-panel gnome-settings-daemon metacity vnc4server
- 설치 후에 인식을 위한 reboot 실시!

2) vnc 설정
- vncserver
- vncserver -kill :1 (최소 실행시 xstartup 파일 생성이 되므로 1회 종료후 사용한다)

- xstartup 파일에 gnome-panel &, gnome-settings-damon &, metacity &, nautilus &를 추가
- ![Deepin스크린샷_select-area_20190916183909](https://i.imgur.com/TVji1OQ.png)
- vncserver :1 (암호설정)
![Deepin스크린샷_select-area_20190916184046](https://i.imgur.com/tO6F4eJ.png)
- ufw allow 5901/tcp (5901 포트를 방화벽에서 허용)
 
