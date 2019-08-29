## My Ubuntu

#### Ubuntu


```
커널 단축키

커널 열기
ctrl + alt + t

시스템 종료 (root 커널이 켜져있을 때는 사용자 계정으로 키를 입력해도 진행안됨 )
poweroff
shutdown -p now
halt -p
init 0
# shutdown -p +10 / 10분 후 종료
# shutdown -r 22:00 - 오후 10시에 재부팅
# shutdown -c 예약된 shutdown을 취소
# shudown - k +15 15분 후에 종료된다는 메세지만 보냄

재부팅
reboot
shutdown -r now
init 6

```

- 커널에서 사용하는 용어
```
  update
    sudo apt-get update / apt update
  upgrade
    sudo apt-get upgrade / apt upgrade
  install
    sudo apt install [패키지명]
  autoremove(사용하지 않은 패키지를 모두 지움)
    sudo apt autoremove / apt-get autoremove
  autoclean(내려받은 파일 제거)
    sudo apt autoclean / apt-get autoclean
  purge(설치된 패키지를 설정파일을 포함해서 완전 제거)
    sudo apt purge / apt-get purge
```

```
history = 커널에서 사용한 것들 확인 가능
history -c 히스토리 목록 삭제
자동 완성 = tab 2회
파일이름 이나 공백이 들어갈 때에는 ""로 묶어줘야함
ex) "i love potato"
자주 사용하는 에디터
= nano, vim, gedit

vim은 i나 a를 누르면 끼워넣기로 실행 됨
(shift i는 커서 줄의 맨 앞 / shift a는 커서 줄의 마지막 )
저장(w), 종료(q), 취소(i)
/문자열 = 검색 / n = 찾은 문자 중에서 다음문=자로 이동 !
man 명령어 = 해당 명렁어 도움말
```

```
리눅스 기본 명렁어
ls : 현재 디렉토리의 파일 목록
ls /etc/systemd : /etc/systemd 디렉토리의 목록
ls -a : 현재 디렉토리의 목록(숨김파일 포함)
ls -l : 현재 디렉토리의 목록을 자세히 보여줌
ls *.conf : conf인 목록을 보여줌
ls -l /etc/systemd/b* : /etc/systemd 디렉토리에 있는 목록 중 앞 글자가 b인 것의 목록을 보여줌
cd : change Directory 디렉토리 이동
# cd : 사용자의 홈 디렉토리로 이동
cd .. : 바로 상위의 디렉토리로 이동
cd /etc/** /etc/**로 이동 (절대경로)
cd ../etc/** ..로 이동 후에 /etc/**로 이동
pwd : print Working Directory
pwd : 현재 작업 중인 디렉토리의 경로 출력

rm : remove
rm hod: hod를 삭제 (보통 rm -rf로 많이 사용 )
rm -i hod : hod를 삭제할 지 메시지가 나옴
rm -f hod : hod를 바로 삭제 ( 강제로 )
rm -r hod : hod 디렉토리와 하위 디렉토리를 전부 삭제함

cp : copy

cp a b : a를 b로 바꿔서 복사
cp -r a b : a 디렉토리를 b 디렉토리로 복사

touch : 크기가 0인 새 파일을 생성하거나, 이미 파일이 존재한다면
파일의 최종 수정 시간을 변경
touch hod.txt : 파일이 없다면 hod.txt 생성 / 있으면 현재 시각으로 최종 수정 시간변경

mv : move
mv a /b : a를 b 디렉토리로 이동
mv hod hod1 hod2 kkk : kkk로 hod, hod1 ,hod2로 이동
mv hod skhod : hod를 skhod로 변경하여 이동

mkdir : 새로운 디렉토리 생성
mkdir bbb : bbb라는 디렉토리 생성
mkdir -p /hod/hodek : /hod/hodek을 생성하는데 , hod가 없다면 hod는 자동 생성

rmdir : remove Directory

rmdir hod : '/hod' 디렉토리 삭제

cat : conCATenate
cat a b : a와 b를 연결해서 파일의 내용을 화면에 보여줌

head,tail : 텍스트 형식으로 작성된 파일의 앞 10행 또는 뒤 10행만 화면에 출력
head /1.conf - 해당파일의 앞 10행을 화면에 출력
head -4 /1.conf - 앞 4행만 화면에 출력
tail -3 /1.conf - 마지막 3행만 화면에 출력

more : 텍스트 형식으로 작성된 파일을 페이지 단위로 화면에 출력
more /1.conf
more +9 /1.conf : 9행부터 출력

less : more 보다 기능이 확장됨

file : 해당파일이 어떤 종류의 파일인지 표시

file /1 : 1은 텍스트 파일이므로 아스키 파일로 표시됨
file /1/gzip : gzip은 실행 파일이므로 'ELF 64-bit LSB executable' 파일로 표시됨

clear : 터미널 화면을 꺠끗히 지워줌  
```
