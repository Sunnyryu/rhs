## setup6

1. 우분투에 설치한 가상머신에 FTP 서버 설치와 운영

(1) vsftpd 설치
    - apt-get -y install vsftpd (vsftpd 패키지 설치)
    - vi /etc/vsftpd.conf 파일 수정 (익명 사용자가 접속할 수 있도록 !)
    (anonymous_enable=YES, write_enable=YES, anon_upload_enable=YES, anon_mkdir_write_enabel=YES)
    - /srw/ftp에 pub 디렉토리를 만들고 chmod 777을 사용하여 권한 부여!
    - systemctl restart vsftpd, systemctl enable vsftpd, systemctl status vsftpd 명령으로 서비스 재시작 및 상태 확인!
    - ufw allow ftp (포트 허용)
(1-1) 다른 가상 서버로 ftp 접속 테스트
    - apt-get -y install lftp
    - fto 서버에 접속 한우 ㅔ /pub 디렉토리에 파일 업로드 및 다운로드

(2)proftpd 설치
    - apt-get -y install proftpd ( 슈퍼 데몬 모드인 inetd 대신 standalone으로 해보기)
    - vi /etc/proftpd/proftpd.conf에 익명사용자가 접속해서 사용 할 수 있도록 설정 변경하기
      - 147행 ~ 186행까지 제일 첫 열의 주석을 모두 제거
      - 169, 179 행 - AllowAll로 수정
    - systemctl restart proftpd , systemctl enable proftpd 명렁으로 서비스 시작 / 가동
    - ufw allow ftp(21)번 포트 허용!!

2. 우분투에 설치한 가상머신에 NFS서버(File server) 설치와 운영

(1) NFS 서버 구현
    - apt-get -y install nfs-common nfs-kernel-server rpcbind (NFS 서버 패키지 설치)
    - vi /etc/exports 에 /share ip주소를 입력 후 저장
    - /share 디렉토리 생성 후에 chmod 707을 이용해서 외부에서 사용할 수 있도록 해줌
    - systemctl restart nfs-server / systectl enable nfs-server로 가동
    - exportfs -v를 이용해서 서비스가 가동하는지 확인
    - 사용하기 위해 ufw disable로 방화벽을 꺼둠 (보안에 취약하지만 서버 가동 연습으로 인해서 꺼두었음)
(2) client로 nfs 서버 디렉토리에 마운트 되도록 하기
    - sudo gedit /etc/fstab 명령으로 파일 열고 내용 추가하기
    - NFS서버IP주소:서버공유 디렉토리(/share) 클라이언트마운트 디렉토리 nfs defaults 0  0
    - client 재부팅 후 nfs 마운트 check
    - 마운트가 되면 디렉토리 하나 생성해서 읽기 / 쓰기 모드로 마운트 check

3. DHCP 서버 설치와 운영 (Dynamic Host Configuration Protocol)
(1) 설치전 원리 알기
  - pc가 전원을 키면 dhcp 서버에 자동으로 ip 주소를 요청하고 서버는 ip 주소 목록에서 할당 전 ip를 고르고 할당됨으로 변경하고 ip 주소를 할당해줌
  - 할당 받은 ip주소로 인터넷을 사용할 수 있음
  - 컴퓨터를 끄면 ip 주소를 반납하고 반환된 ip를 할당 전으로 변경 해주는 시스템
(2) client를 부팅하여 준비하기
  - nm-connection-editor 명령 실행 후 (터미널에서) 유선 연결에서 편집을 하여 자동 dhcp 로 설정
  - ifconfig으로 자동으로 할당된 ip 체크
  - /etc/resolv.conf 파일에 nameserver의 ip 확인
(3) 호스트 os에서 dhcp 서버를 끔..
(4) client에서는 현재 dhcp 서버가 없어서 안됨
(5) 가상머신의 다른서버로 들어감
  - root로 로그인 한 후에 ping -c 3 www.kernel.org를 들어가보면 고정 ip주소를 할당하였기에 dhcp 서버와 상관없이 됨!!
  - vi /etc/network/interfaces 파일 실행 -> iface ens32 inet static 부분에서 static을 dhcp로 변경하고 종료
  - 재부팅 후에 5분을 기다리거나 30초로 줄이는 방법이 있다. vi /etc/systemd/system/network-online.targets.wants/networking.service 파일을 실행하여 21행의 5min을 30sec으로 변경 후 저장
  - reboot -> ifconfig 확인시 역시 dhcp 서버가 없으므로 실패할 꺼임
(6) 가상머신 메인 서버에 dhcp 서버 설치
  - apt-get -y install isc-dhcp-server
  -vi /etc/dhcp/dhcpd.conf -> vi /etc/dhcp/dhcpd.conf를 실행
  ![Deepin스크린샷_select-area_20190919184101](https://i.imgur.com/eqrzgPL.png)
  - /var/lib/dhcp/dhcpd.leases가 없다면 touch를 이용해 만들어줌 (dhcp 클라이언트가 ip 주소를 대여해간 정보 기록)
  - systemctl restart isc-dhcp-server, systemctl enable isc-dhcp-server, systemctl status isc-dhcp-server 입력하여 시작/가동/상태확인 해줌!!
  - ufw allow 67 , ufw allow 68 명령으로 dhcp 관련 포트 허용
(7) client reboot 후에 ifconfig 명령으로 할당받은 ip 주소 받기!
(8) 가상머신의 다른 서버도 접속하여 ip 정보 할당 받기
(9) 가상머신의 메인서버에서 vi /var/lib/dhcp/dhcpd.leases를 열면 dhcp 클라이언트가 네트워크 정보를 대여해간 것이 남음!!
