## My Ubuntu

#### 편하게 정리해 !

```
파일 압축 / 묶기
xz ( xz로 압축하거나 풀어줌)
xz a : a를 a.xz로 만듦 (기존파일 삭제)
xz -d a.xz : 압축 풀어줌 a로 만들어짐
xz -l a.xz : a.xz 압축 파일에 포함된 파일 목록과 압축률 등을 출력
xz -k a : 압축 후에 기존 파일 삭제하지 않고 그대로 둠

bzip2 (bz2로 압축하거나 풀어줌)
bzip a : a를 a.bz2로 만듦
bzip2 -d a.bz2 == bunzip2 a.bz2  : 압축 풀어줌 a로 만들어짐
bizp2 -k a : 압축 후에 기존 파일 삭제하지 않고 그대로 둠

gzip (gz로 압축하거나 풀어줌)

gzip a (a를 압축 파일인 a.gz로 만듦)

gzip -d a.gz (압축을 풀어줌. 즉, a.gz의 압축을 풀어서 a로 만듬)

zip / unzip
zip b.zip a : a를 b.zip으로 만듦
unzip a.zip : a로 만듦

tar
c(새로운 묶음을 만듬), x(묶인 파일을 품), t(묶음을 풀기전에 묶인 경로를 보여줌), C(묶음을 풀 때 지정된 디렉토리에 압축을 품, 지정을 않하면 묶을 때와 동일한 디렉토리에 묶음이 풀림)
f(묶음 파일 이름 지정), v(visual의 의미로 파일을 묶거나 풀리는 과정을 보여줌)
J(대문자 = tar + xz ), z(tar + gzip), j(tar+bzip2)
tar cvf a.tar /a 묶기
tar cvfJ a.tar.xz /a 묶기 + xz 압축
tar cvfz a.tar.gz /a 묶기 + gzip 압축
tar cvfj a.tar.bz2 /a 묶기 + bzip2 압축
tar tvf a.tar 파일확인
tar xvf a.tar tar 풀기
tar Cxvf adir a.tar adir에 tar 풀기
tar xfJ a.tar.xz xz 압축 해제 + tar 풀기
tar xfz a.tar.gz gzip 압축 해제 + tar 풀기
tar xfj a.tar.bunzip2 bzip2 압축 해제 + tar 풀기
```

```
파일 위치 검색은 find를 이용함
(-name, -user, -newer, -perm, -size 등)

find /etc -name "1.conf" - /etc 디렉토리 하위의 1.conf 파일 검색
find -perm 644 ( 644인 파일 검색 - 혀내 사용자의 홈 디렉토리 하위에 허가권)
find /abc/def -size -10k -size 100k
- abc/def 하위에 있는 파일 크기가 10kb~100kb인 파일 검색
which, whereis, locate 등도 사용함

시스템 설정
unity-control-center 명령어를 사용
nmtui = 네트워크 설정
ufw = 방화벽 설정

cron 과 at

네트워크 관련 설정과 명령어
```
