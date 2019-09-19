## setup7

1. 프록시 서버 설치 및 구현
  (1) 설치
    - apt-get -y install squid3 (squid 프록시 서버 패키지 설치)
    - vi /etc/squid/squid.conf 파일을 실행시키고 수정하기
    ```
    acl myserver src 192.168.122.1/255.255.255.0
    http_access allow myserver
    cache_dir ufs /var/spool/squid 1000 16 256
    visible_hostname myserver
    ```
    - ufw disable 포트 허용 하기! (방화벽 중지)
    - systemctl stop squid 실행 후  (프록시 서버 중지)
  (2) 가상머신 클라이언트로 실행해보기
    - firefox에서 프록시 설정에 porxy와port를 수정하고 use this proxy severfor all protocols의 체크박스를 체크함
  (3) 서버에서 가동 재가동 시키기
    - systemctl restart squid, systemctl enable squid, systemctl status squid 명렁을 입력하여 squid 서비스를 시작/ 상시 가동/ 상태를 확인 함
  (4) 클라이언트 재확인
   - 가상머신 메인서버에 squid를 재가동 시켯으므로 firefox를 들어가면 잘됨!!

2. 방화벽 컴퓨팅과 pxe 서버는 다른 가상머신이 필요하여 추후에 설치 및 진행 예정
