## Basic6

#### python Django 3


```
1. Project setting

django-admin startproject config(설정 폴더명으로 만들어짐) . => 해당 파일에 프로젝트와 config를 구성하겠습니다. (.은 현재 위치!)

config로 들어가서 setting.py에 언어를 수정해줌

ko-kr / Asia/seoul

Project 안에 앱만들기 - python manage.py startapp boards(앱 명)
앱을 만들고 ./config/setting.py에 가서 installed_app에 해당 앱 폴더를 추가 !

url.py에 앱에 대한 path를 설정 해줍니다.
앱 별로 구별하기 위해서 ... => ex) path('board/', include('boards.urls')),
와 함꼐 위에 path가 import 되어 있는 부분에 path, include를 import 시킴

해당 앱에 들에 urls.py를 만듬..

from django.urls import path
from . import views // .은 현재 위치 / views는 파일명 이라고 생각하면 아주 이지함
ex)
urlpatterns = [
        path('', views.index),

        ]
view.py에 index 함수를 만들고 html로 리턴을 시켜준다.
그런데 render를 이용하기 위해서 .. templates를 파일을 만들고.. 이 안에 앱 파일명과 같은 폴더를 만들어준다.(중복을 피하기 위해서) => html 파일을 만든다.

그리고 타이틀을 상속 받기 위해서 ..

config => settings.py
추가 예쩡
```

```
2. ORM

MTV (MVC와 비슷)
모델 (모델) / 템플릿(뷰) / 뷰(컨트롤러)

DB 기본 구조
query : 데이터를 질의 하는 명렁어??

db : 체계화된 데이터(들))의 모임
스키마 : db 자료의 구조, 표현방법, 관계 등을 정의한 구조

테이블
- 필드 : column
- 레코드 : data

database / sql 문을 던져야 .. 받는 아이!!? ddoit

Django 에서는 DB ORM을 Mapping을 해놓음
ORM 장점 : SQL 몰라도 DB 접근 및 사용 가능 / SQL 문이 아니기에, 코드의 가독성이 좋아짐! /
매핑 정보가 확실하며, ERD 의존도를 낮춰줌!! / MVC 패턴을 보다 잘맞춰줄 수 있음! / 객체 지향 적인 접근으로 생산성 증가 / 독립적으로 작성 , 해당객체 재활용 가능
단점 : 프로젝트 규모가 커질 때, 관계 복잡성이 올라가면 ORM 구현 시 문제점이 발생할 수 있어, 설계를 보다 잘해야한다는 점이 있음. orm으로 모든 것을 구현하기 힘듬.

python manage.py shell 쉘로 연동

ex는 사진으로 붙어넣음
```
![justin](https://i.imgur.com/aB7GC05.png)
![justin2](https://i.imgur.com/jIz7gzt.png)
```
Model
모델은 단일 데이터에 대한 정보를 가지고 있음!

필수적인 필드(컬럼)과 데이터(레코드)에 대한 정보를 포함
각각의 모델은 단일 DB와 매핑이 되옵니다.
사용자가 저장하는 데이터들의 필수적인 필드(컬럼) 동작을 포함

python manage.py makemigrations => models.py를 만들고 나서 마이그레이션을 위한 명렁어라고 생각하자!(명세서를 만들었다고 생각하자)
python manage.py makemigrations 앱이름(ex)boards) => boards에만 makemigrations파일을 만들어줌!!
python manage.py sqlmigrate 앱이름(ex)boards) 0001(보고 싶은 파일의 숫자명!)  
python manage.py showmigrations => 전체를 확인해줌!!(앞의 빈칸은 적용이 되지 않은 거임)
python manage.py showmigrations 앱이름(ex)boards) => boards가 들어가있는 것을 확인 해줌!
python manage.py migrate => migration 파일과 python에서 만든 migration 파일이 생성되어 적용시킴!
적용이 되면 앞의 빈칸에 x 표시가 됨!

변경순서
model.py 작성 => makemigrations : 명세서를 생성! => 위에 있는 명령어들을 수행 => db에 저장!

db.sqllite3를 보는 법
sqlite db.sqlite3
.tables = 테이블 확인
.schema 확인하고 싶은 스키마 명 => 스키마가 제대로 설치되었는지 확인할 수 있음

Board.objects.*** (objects는 db와 인터페이스를 연결해주는 아이!)
ex)
from orders.models import Subway
board = Board()
board.title = "first"
board.content = "django !!!!"

ex2) board = Board(title="second", content="django")
board.save() => db에 저장시켜주는 명령어 !
ex3)board.save()가 필요없는 방법
board = Board.objects.create(title="값", content="값")
a = Board.objects.get(id=id)

tip : import os
os.system('clear') = > python console clear !

나머지는 밑의 그림을 참조하기!!

filter vs get(get은 1개만 filter는 queryset으로 2중 데이터도 받을 수 있음!! - filter는 1개라도 받으면 queryset임)
```
![board1](https://i.imgur.com/wsZfxqK.png)
![board2](https://i.imgur.com/9mJbnce.png)
![newboard](https://i.imgur.com/hjBjtEu.png)
![newboard2](https://i.imgur.com/8Zrh0z3.png)
![newboard3](https://i.imgur.com/vE5JaHm.png)
![newboard4](https://i.imgur.com/Du4pyvU.png)
![newboard5](https://i.imgur.com/vyUeeUv.png)
```
3. python admin

python manage.py createsuperuser => admin 계정 생성 방법
id/ 이메일(생략 가능) / 비밀번호
```
