## setup2

1. 우분투에서 KVM, virt-manager(가상머신) 설치

```
sudo apt install virt-manager 로만 설치를 하려다보니 lvm2 에러가 계속 발생했다.
그래서 방법을 찾았는데 아래와 같다.

sudo apt install qemu-kvm libvirt-bin bridge-utils ubuntu-vm-builder
의 패키지들을 먼저 설치한 후에 sudo apt install virt-manager를 진행하였다. 그 후에 lvm2 에러는
나오지 않고 완료됨!
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
