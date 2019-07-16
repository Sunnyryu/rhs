## My Ubuntu

#### 편하게 정리해 !


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

- 커널 관련 용어
  - update
    - sudo apt-get update / apt update
  - upgrade
    - sudo apt-get upgrade / apt upgrade
  - install
    - sudo apt install [패키지명]
  - autoremove
    - sudo apt autoremove / apt-get autoremove
  - autoclean
    - sudo apt autoclean / apt-get autoclean
    - 
