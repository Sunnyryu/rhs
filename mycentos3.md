## hello centos 3

#### centos !

```
bash shell의 한 줄의 문자열 출력 : echo
bash shell의 한 줄의 문자열을 %지시자와 |문자를 이용하여 출력 형식으 지정 : printf

표준 입력 파일 디스크립터 stdin 0
표준 오류 파일 디스크립터 stderr 2
표준 출력 파일 디스크립터 stdout 1

출력 리다이렉션 : > (기존 파일의 내용을 삭제하고 새로 결과를 저장)
ls -l > ls.out
출력 리다이렉션 : >> (기존 파일의 내용 뒤에 추가 저장)    
입력 리다이렉션
ls -l < ls.in

셀 변수 : 현재 shell에서만 사용 가능, 서브 shell로는 전달되지 않음
환경 변수 : 현재 shell 사용 가능, 서브 shell로도 전달 가능
set : shell 변수, 환경 변수 모두 출력
환경 변수만 출력: env

환경변수 종류
HISTSIZE, HOME, LANG, PATH, PWD, SHELL....

Shell 변수 정의.. : 변수명=문자열
정의된 shell 변수를 환경변수로 설정 : export 변수명=문자열, export 변수명
환경변수를 다시 shell 변수로 바꾸려면 : export -n
기존 명령을 대신해서 다른 이름을 붙여서 사용하려면 : alias 이름 = '명령'
alias 설정 해제 : unalias

사용자가 이전에 입력한 명령을 다시 불러와서 사용하려면 : history
바로 직전에 사용했었던 명령을 재실행 하려면 : !!
히스토리에서 사용했었던 명령을 재실행 하려면 : !번호
히스토리에서 문자열로 시작하는 명령중에서 마지막에 실행된 명령을 재실행 하려면 : !문자열

bash shell에서 시스템 환경 설정 파일
/etc/profile : 모든 shel에서 공통으로 적용되는 환경  설정, bash.bashrc 파일을 실행시킴
/etc/bash.bashrc - 기본 프롬프트 설정, 시스템 공통으로 적용되는 환경 설정
/etc/profile.d/*.sh - 언어나 명령별로 필요한 환경을 설정

bash shell에서 사용자의 환경 설정 파일 :
~/.profile : 사용자가 정의하는 환경 설정, bashrc 파일을 실행시킴
~/.bashrc :  히스토리의 크기 설정, alias 설정, 함수 설정
~/.bash_aliases : 사용자가 정의한 alias를 별도 파일로 저장
~/.bash_logout : 로그아웃할때 필요한 함수들을 설정

ls -l 옵션으로 출력 내용
- 또는 d는 파일의 종류
rwxrwxrwx는 소유자 파일 접근권한, 소유자 그룹, 기타사용자
하드링크 수 개수 / 소유자 id / 소유자 group 이름 / 파일크기 / 날짜(수정된 날짜),시간  / 파일명 - 경로

파일 접근 권한 변경
chmod  
파일 접근 권한 변경(하위 디렉토리까지)
chmod -R
기호모드 / 숫자모드

기호 모드 : +, -, r, w, x
숫자 모드 : r=4, w=2, x=1
ex) chmod 777 / 644....

기본 접근 권한을 확인하려면
umask
기본 접근 권한을 변경하려면
umask
기본 접근 권한 변경 umask는 파일이나 디렉토리 생성 시 부여하지 않을 권한을 지정함

특수 접근 권한 : SetUID, SetGID, Sticky bit
SetUID : 맨 앞자리가 4로 설정 (해당 파일이 실행되는 동안에는 파일을 실행시키는 사용자 권한이 아니라 파일 소유자의 권한으로 실행 `s`로 표시됨)
SetGID : 해당 파일이 실행되는 동안에는 파일을 실행하는 사용자 권한이 아니라 파일 소유자의 그룹 권한으로 실행
맨 앞자리를 2로 설정함

sticky bit는 디렉토리에 설정
sticky bit는 맨 앞자리가 1로 설정
sticky bit가 설정된 디렉토리에는 누구나 파이릉ㄹ 생성가능, 다른 사용자가 생성한 파일은 삭제 불가 (ex: /tmp)

daemon process : 특정 서비스를 제공하기 위해 존재, 리눅스 커널에 의해 실행
goa process : 자식 프로세스가 아직 실행 중인데, 부모 프로세스가 먼저 종료된 프로세스
zombie process : 자식 프로세스가 종료했는데도 ps로 확인 했을 때 남아 있는 프로세스(프로세스 테이블에 남아있는 경우)
(defunct 프로세스로 출력됨)

ps
상세 정보 출력 : -f
UID PID PPID, C, STIME, TTY, TIME, CMD
터미널에서 실행한 프로세스의 정보를 출력 : -a
STAT 필드 추가
현재 실행 중인 프로세스의 메모리 사용량 출력 : -u
%cpu, %mem, vsz, rss, tty, stat, start 등

실행중인 특정 프로세스 정보 검색 : pgrep
프로세스 강제 종료 : kill [-시그널] pid번호
pkill : 프로세스 이름으로 강제 종료 할 때 씀

현재 실행중인 모든 작업을 보려면 : jobs
background 작업
forground 작업
ctrl + z / stop %작업번호
bg %작업번호
fg %작업번호

특정 시간에 작업을 한번만 수행하도록 예약 : at [옵션] 시간
at 12pm +2 days
at 12am tomorrow
정해진 시간에 작업을 반복적으로 수행하도록 예약 : crontab
```
