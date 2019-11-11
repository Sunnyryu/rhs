## Basic4

#### python Django


```
Django

Framework => 기본적인 구조나 필요한 코드들을 알아서 제공!..

Python : Free , Open source

web service (요청 / 응답)

xxx를 요청 -> 서버에서 요청을 받은 것을 사용자에게 보내줌

MTV Pattern (MVC와 비슷!)

MODEL / TEMPLATE / VIEW
(모델 / 뷰  / 컨트롤러와 비슷한 역할 ~~)

URLs(Parsing) -> VIEW(Logic 처리) -> TEMPLATE(사용자에게 보여줌)

DJango : Project 단위 / app 단위

ex) app은 프로젝트의 하위 기능 단위라고 생각하면 됌.
인스타그램이 Project 단위라면, app 단위는 글을 쓰거나 등등의 기능임.

python manage.py runserver => 개발 서버 관리
python manage.py runserver 8080 => python manage.py runserver 0:8000
(port 변경)

setting.py

Secret 키는 보안 관련

allowed_hosts = [] (실제 사용하는 도메인 사용 권장(배포) / 개발 시에는 비워두거나 전체 도메인이 접촉 가능 하게끔 해두기 !)

Installed_APPS => 사용되는 앱을 기록( 추가할 것은 기록하여 저장하여야 반영이 됩니다.)

middleware => framework(보안, 세션 등... 여러 미들웨어가 있으며, 필요한 미들웨어가 있다면 작성하면 됌.)

Root_URLCONF => 기준이 되는 URL 파일 위치를 나타냄

TEMPLATES -> 템플릿 관련해서 설정을 해주는 것...

DATABASES => DB에 관련된 것을 작성해줌

PassWord Validator => 비밀번호가 어떤 지에 대해서 체크를 해줌.. ( 짧거나 비슷하거나 길거나 등등..)

language code & time zone은 필요에 따라 수정을 해줌..!

urls.py

@app.route와 비슷한 기능 (파일로 만들어서 보관)
url Pattern에 따라 어떤 기능을 하는 지 나눈 것이라고 생각하길!

app 설정 ..

python manage.py startapp pages

admin.py => database admin management (커스텀마이징도 할 수 있고 admin.py가 없다면 쿼리문을 이용해서... 확인을 해야함... )

apps.py => 앱의 정보가 있는 곳!!

models.py

class와 모델명을 구현해 놓으면 되옵니다.

tests.py => 작성된 것이 잘 되었는지 확인해볼 수 있는 py

views.py => MVC 구조에서는 controller / django MTV에서는 View 역할이라고 할 수 있음 ( 많이 수정할 것임)

@app.route('/index') [Flask] => urls.py [Django]

def index(): return render_template('x.html') [Flask] => view.py [Django]

urls.py / view.py / template.py를 수정을 많이함!!

```
