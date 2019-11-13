## Basic5

#### python Django 2


```
Django
form
- form : action - 데이터가 전송될 URL, method - GET/POST
- input : name : key /value : value
- label : for 옵션 input 에 id값이랑 매치

GET
- data가 body 통한게 아니라 쿼리스트링
- 데이터 조회할 때

POST
- DB를 생성 / 변경 할 때 주로 사용 / html body 정보를 담아 전송
- 원칙적으로 Post 요청은 html 파일로 응답하면 아니되요.
- post 요청이 오면 get 요청 받는 페이지로 redirect를 시켜야함 .. (RESTful)
- Django는 post를 csrf_token과 함께 보냄..
(csrf = Cross Site Request Forgery = CSRF => 사이트 위조 방지를 위해..)
- 토큰을 보내지 않으면 403 Forbidden error가 발생!

Static File

{% load static %} 라고 html 최상단에 추가
{% static '파일경로 '%} 파일 경로는 app폴더 아래 static 폴더로 관리가 됨.
(templates와 비슷)

템플릿 상속
templates name space

템플릿 상속(확장))

앱 안에 있는 템플릿만 ....
TEMPLATES 설정 안에
DIRS : [os.path.join(BASE_DIR, "프로젝트 셋팅즈가 있는 폴더명","templates")]

ex) 프로젝트 셋팅즈 폴더명/templates/base.html
{%block (블럭이름) %} {% endblock %}을 html 파일 안 원하는 곳에 둠

만들어진 base.html을 상속하려면
html 상단에
{% extends 'base.html' %}
{% extends '상속하는 html' %}
{% block (블럭이름) %}
내용을 기술하면 됨.
{% endblock %}
```
