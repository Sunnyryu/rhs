## Basic7

#### python Django 7


```
Follow 사람과 사람과 N:M 관계

User 모델 정의된 것을 수정할 수 없어서 
장고에서 제공하는 abstractuser 라는 친구를 상속받아서 새로 정의 ..

AbstractBaseUser ..
- password / last_login
- 커스텀의 자유도가 높지만 수정하거나 추가할 것들이 많아서 pass
- AUTH_USER_MODEL 재설정 필요가 없음 !


AbstractUser
- setting.AUTH_USER_MODEL 꼭 재설정 필요 !
- AUTH_USER_MODEL = "앱이름.클래스이름"


all.auth 설치 및 setting을 해줌!
```
