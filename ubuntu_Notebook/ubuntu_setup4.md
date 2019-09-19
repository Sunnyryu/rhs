## setup4

1. ubuntu에 네임서버 구축

1) 캐싱 전용 네임 서버 관련 패키지 설치

  - apt-get -y install bind9 bind9utils
  ![Deepin스크린샷_select-area_20190917175920](https://i.imgur.com/KJJKeS7.png)

  - 설정파일 수정
  /etc/bind/named.conf.options 파일을 에디터로 열어 2행을 추가한다.

    recursion yes;
    allow-query { any;};
    (해당 내용은 다른 가상머신의 네트워크 주소에 있는 모든 컴퓨터가 네임 서버 사용 가능)

2) 시스템 재시작
  - systemctl restart bind9
  - systemctl enable bind9
  - systemctl status bind9

3) 방화벅 허용
  - ufw allow 53 / ufw status

4) 네임서버 작동 확인
  - dig @네임서버ip 도에민주소
  - nslookup
  - 도메인주소
![Deepin스크린샷_select-area_20190917182510](https://i.imgur.com/QhodOLJ.png)
![Deepin스크린샷_select-area_20190917182523](https://i.imgur.com/gHJZXNf.png)

1-2. 가상머신 clinet에 server를 네임서버로 사용
1) 가동확인
  - nslookup
  - server naverserverip
  - www.naver.com(도메인주소)
![Deepin스크린샷_select-area_20190917181417](https://i.imgur.com/MgZ0puw.png)
2) 네임서버 변경
  - /etc/resolv.conf
  - 주소 변경

1-3. 가상머신 서버로 텍스트 기반 웹브라우저 접속
  - apt-get -y install elinks
  - elinks
  - 영문 주소 입력(한글 주소면 한글 설정을 하지 않아 깨짐)
  - (ex www.ubuntu.com에 접속)
![Deepin스크린샷_select-area_20190917182053](https://i.imgur.com/yzUjMfQ.png)

2. 마스터 네임 서버 구축
  1) 웹서버 설정 (apache2 사용)
  - apt-get -y install apache2
  - systemctl restart/enable/status apache2
  ![Deepin스크린샷_select-area_20190917183200](https://i.imgur.com/uK7uGw7.png)
  2) 방화벽 허용
  - ufw allow 80
  - 파일 수정
  ![Deepin스크린샷_select-area_20190917183324](https://i.imgur.com/xAdz0LH.png)

2-1. 가상머신 server에 FTP 서버 설치 및 설정
  - apt-get -y install vsftpd
  - 방화벽허용 (ufw allow 21)
  - msg 파일을 만들어서 /srv/ftp에 넣고 내용 추가(ex: ubuntu 18.04 lts ftp server)
  - /etc/vsftpd.conf 파일 수정
  ![Deepin스크린샷_select-area_20190917183909](https://i.imgur.com/ru7lb3T.png)

  - systemctl restart vsftpd

3. server에 도메인 설정
  - ex) john.com 이라는 것 만들어보기
  ![Deepin스크린샷_select-area_20190917184244](https://i.imgur.com/LMOCq1O.png)
  - named-checkconf 명령을 확인하여 문법 확인
  ![Deepin스크린샷_select-area_20190917184329](https://i.imgur.com/iqr808J.png)
  - john.com.db라는 빈파일 생성 후에 파일에 아래의 내용 추가
  ![Deepin스크린샷_select-area_20190917184708](https://i.imgur.com/mwmutKs.png)
  - named-checkzone john.com john.com.db 명령 입력해서 문법 이상 확인
  ![Deepin스크린샷_select-area_20190917184731](https://i.imgur.com/S6v63v7.png)
  - system restart bind9, systemctl status bind9 확인

4. 가상머신 client로 작동확인

  - sudo gedit /etc/resolv.onf 명령어 이용하여 네임 서버 변경
  - 홈페이지 들어가보기
![Deepin스크린샷_select-area_20190918193524](https://i.imgur.com/AfzXaBK.png)

5. 심화로 john.com을 실행시킬 때마다 설정된 다른 홈페이지 실행시키기
  - john.com.db에 내용을 아래와 같이 수정함!
![Deepin스크린샷_select-area_20190918200541](https://i.imgur.com/Pr0tJKX.png)
  - nslookup을 이용해서 www.john.com을 치게되면 아래와 같은 그림이 나타남
![Deepin스크린샷_select-area_20190918194045](https://i.imgur.com/Jelzveq.png)

  - client로 들어가서 /etc/resolv.conf에 있는 nameserver를 server의 ip로 바꿔줌
  - www.john.com 을 실행하고 확인 후에 종료 후에 다시 키면 설정된 다른 사이트들이 돌아가면서 1개가 열림!
![Deepin스크린샷_select-area_20190918195721](https://i.imgur.com/05FXy6y.png)
![Deepin스크린샷_select-area_20190918195730](https://i.imgur.com/cifNp1O.png)
![Deepin스크린샷_select-area_20190918195803](https://i.imgur.com/6hxB0zk.png)
