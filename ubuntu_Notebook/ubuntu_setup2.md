## setup2

1. 우분투에서 KVM, virt-manager(가상머신) 설치

```
sudo apt install virt-manager 로만 설치를 하려다보니 lvm2 에러가 계속 발생했다.
그래서 방법을 찾았는데 아래와 같다.

sudo apt install qemu-kvm libvirt-bin bridge-utils ubuntu-vm-builder
의 패키지들을 먼저 설치한 후에 sudo apt install virt-manager를 진행하였다. 그 후에 lvm2 에러는
나오지 않고 완료됨!
```
![Deepin스크린샷_select-area_20190903110531](https://i.imgur.com/dNtVno0.png)
```
가상머신 생성
```
![Deepin스크린샷_select-area_20190903110921](https://i.imgur.com/I3CFemY.png)
```
메모리 설정
```
![Deepin스크린샷_select-area_20190903110943](https://i.imgur.com/7A4sEdz.png)
```
저장소 용량 설정
```
![Deepin스크린샷_select-area_20190903111000](https://i.imgur.com/CozpsBe.png)
```
완료전 화면
```
2. R 설치


R을 설치하는 방법은 R의 홈페이지에 들어가서 운영체제에 맞는 것을 누르면 설치법이 나옴.
```
https://ftp.harukasan.org/CRAN/ (EX)

apt-get update
apt-get install r-base r-base-dev

apt-get install libopenblas-base or apt-get install libopenblas-base

이거만 해주면 R은 구동이 됩니다.

apt-cache rdepends r-base-core ()

```


R studio를 사용하면 r을 유용하게 설치할 수 있기 떄문에 설치해주장 ..

```
https://www.rstudio.com/products/rstudio/download/

r studio는 server / desktop으로 나뉨
```
```
방법 1.(서버)
$ sudo apt-get install gdebi-core (gdebi-core가 있다면 바로 wget으로 넘어가면 됌)
$ wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.1335-amd64.deb
$ sudo gdebi rstudio-server-1.2.1335-amd64.deb
```
```
방법 2. desktop의 경우에는 deb파일로 설치를 할 수 있음
deb 파일 설치후 install 도우미로 설치해주면 바로 사용 가능!!
```


R package 설치 시 에러 발생 !! - 해결법

오늘 r을 사용하다가 패키지를 설치하지 못하는 사고가 났다.?
```
ERROR: configuration failed for package ‘curl’
* removing ‘/usr/local/lib/R/site-library/curl’
ERROR: dependency ‘curl’ is not available for package ‘httr’
* removing ‘/usr/local/lib/R/site-library/httr’

다운로드한 소스 패키지들은 다음의 위치에 있습니다
	‘/tmp/Rtmpx43u2v/downloaded_packages’
경고메시지(들):
1: In install.packages("httr") :
  패키지 ‘curl’의 설치가 0이 아닌 종료상태를 가졌습니다
2: In install.packages("httr") :
  패키지 ‘httr’의 설치가 0이 아닌 종료상태를 가졌습니다
```

```
그래서 다른 방법을 사용하여 설치하였다.
(cu)
apt-get install r-cran-http

xml의 경우에도 에러가 발생하여 설치하였음..

apt-get install-r-cran-xml

관련된 패키지 및 curl도 생성이 되었다.
안되면 당황하지말고 터미널에서 r-cran-*을 이용해서 설치하자 ~~~~
```
