## setup5

1.우분투에서 가상머신으로 AMP 설치 및 웹 서버 응용

(1). 패키지 설치
  - apt-get install apache2, php7.2-common, mysql-server 설치
  - apt-get install lamp-server^로도 가능(리눅스 아파치, mysql, php)

(2) apache2 작동 확인 및 mysql 작동 확인
  - systemctl restart apache2 / systemctl enable apach2 / systemctl status apache2를 입력하여 에러가 없는지 확인
  - systemctl restart mysql / systemctl enable mysql로 mysql 작동 확인
(3) php 작동확인
  - localhost를 들어가면 apache2 page가 뜸
  - vi /var/www/html/phpinfo/php 명령 실행
  - <?php phpinfo(); ?>를 추가
  - localhost/phpinfo.php에 들어가면 phpserver가 실행됨!!
  - ufw allow 80으로 웹 서버 접근 권한 포트 허용

(4) XE 설치 후 운영
  - apt-get -y install php php-gd php-xml 패키지를 먼저 설치
  - systemctl restart apache2로 아파치 서버 재시작
  - xe 홈페이지에 들어가서 xe core를 설치
  - /var/www/html에 디렉토리로 가서 다운로드 받은 파일을 이동 시키고 압축을 품
  - 외부에서 접근할 수 있도록 chmod를 707로 바꿈
  - mysql로 들어가서 xe에서 사용할 database 사용자를 만들고 db도 만들어둔다!!

(5) xe 게시판에 용량 제한을 높일 수 있도록 php 설정 변경
  - vi /etc/php/7.2/apache2/php.ini 열기
  - max_executio_time = 30을 300으로 수정 (초단위임!)
  - post_max_size = 8M 을 500M 으로 수정
  - upload_max_filesize = 2M을 500M으로 수정( 500MB까지 업로드 하기 위해서!)
  - systemctl restart apache2로
(6) 웹하드 설치
  - ajaxploror를 설치
  - /var/www/html 디렉토리에 있는 파일을 압축을 풀고 이름을 변경함
  - chmod를 707로 바꿔서 외부 접속자가 읽고 쓰고 실행을 할수 있도록 바꿔줌
  - chown -R www.data.www.data webhard -> webhard 디렉토리와 그 하위 디렉토리의 소유자 및 그룹을 www-data로 변경
  - apt-get -y install php-mcrypt 패키지 설치
  - vi /etc/apache2/apache2.conf 를 들어가서 AllowOverride None을 ALL로 수정(155,160,166행 쯤)
  - systemctl restart apache2로 재시작
 (7) 클라우드 서비스 기능을 제공하는 오픈소스인 ownCloud 에디션을 설치하고 운영(lamp가 설치 되어있어서 크게 문제 없음)
  - apt-get -y install php-zip php-mbstring php-curl( 패키지 설치 )
  - owncloud.org에서 서버를 다운로드!!
  - /var/www/html/ 디렉토리에서 이동하고 다운로드한 파일을 복사한후에 압축!!
  - chomod 707 owncloud 외부에서 사용가능하게끔!
  - chown -R www-data.www-data ownclound
  - systemctl restart apache2 - 아파치 서버 재시작
  - ufw allow 443 owncloud는 https 프로토콜로 사용하므로 ufw allow 443 포트 허용!
 (8) 다른 가상머신 클라이언트 설치 및 실행
 - 홈페이지 들어가서 필요한 패키지 받음
 - owncloud 클라이언트 설치
 - 터미널에 owncloud &로 실행
 - http://localhost/owncloud 입력 후 next 클릭
 - username에는 ubuntu / 비밀번호도 입력
 - 디렉토리 지정
 - 새 키 모음의 암호 지정
 - finish 클릭
 - 동기화 될떄까지 기다리면 다른 클라이언트에서 보왔던 파일 확인 가능
2. 웹서버 설정파일 과 폴더
 - /etc/apache2/apache2.conf가 설정파일임
 - SeverRoot "/etc/apache2" -> 웹 서버의 설정파일, 로그 파일 등이 저장되는 최상위 디렉토리
 - Listen 80 -> 웹 서버의 포트번호, 기본적으로 80으로 함
 - include conf.modules.d/.conf -> 설정파일에 포함될 파일의 경로와 파일 이름이 들어 있음
 - User ${APACHE_RUN_USER} -> 웹 서비스를 작동하는 사용자,ENVVARS 파일에 WWW-DATA로 설정 되어 있음
 - Group ${APACHE_RUN_GROUP} -> 웹 서비스를 작동하는 그룹, envvars 파일에 www-data로 설정되어있음
 - MaxKeepALiveREquest 10 -> 처리할 수 있는 최대 요청 수
