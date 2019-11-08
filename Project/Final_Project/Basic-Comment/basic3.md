## Basic3

#### python


```
https://api.telegram.org/bot<token>/METHOD_NAME => telegram api 기본 연동 확인
ex 1) https://api.telegram.org/bot<token>/METHOD_NAME/getMe => 내꺼 확인
ex 2) https://api.telegram.org/bot<token>/METHOD_NAME/getUpdates => 업데이트 한 것 확인(어떤 걸 보냈니..)

ex 3) send message
https://api.telegram.org/bot<token>/METHOD_NAME/sendMessage?chat_id=911709013&text=안녕하쎼요

.env 파일을 띄우고 싶다면 python-decouple pip를 설치하거나 python-dotenv를 설치
pprint => 이쁘게 나옴.. ! 

```
