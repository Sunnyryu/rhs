## setup2

1. 우분투에서 KVM, virt-manager(가상머신) 설치

```
sudo apt install virt-manager 로만 설치를 하려다보니 lvm2 에러가 계속 발생했다.
그래서 방법을 찾았는데 아래와 같다.

sudo apt install qemu-kvm libvirt-bin bridge-utils ubuntu-vm-builder
의 패키지들을 먼저 설치한 후에 sudo apt install virt-manager를 진행하였다. 그 후에 lvm2 에러는
나오지 않고 완료됨!
```
