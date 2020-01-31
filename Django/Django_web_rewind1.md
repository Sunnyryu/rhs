## Django 

#### Web 

```
일반적으로 웹 클라이언트가 요청하면 http/https 프로토콜으 이용해 웹서버에 닿고 
웹서버는 응답해주는 역할을 함 !

리눅스에서 curl을 사용해서 인자로 넘어온 url로 http 요청을 보내는 방식이 있고, 
telnet을 사용하는 방식 

HTTP 프로토콜 
웹 서버와 웹 클라이언트 사이에서 데이터를 주고 받기 위해 사용하는 통신방식으로 TCP/IP 프로토콜 위에서 동작함 !

HTTP 메세지 구조
스타트 라인 (요청라인OR 상태라인) / 헤더 / 빈줄 / 바디 등으로 이루어짐 
(GET, POST, PUT , DELETE ,HEAD , OPTIONS, TRACE, CONNECT 등이 쓰이며, )
CRUD의 Read는 get / Create는 post / Update는 put / Delete는 delete와 각각 매칭 되옵니다.

파이썬에서는 정규표현식을 이용한 url 식을 씀 !!

웹 어플리케이션 서버( 웹 클라이언트 요청 을 받아 요청 처리 / 웹 클라이언트에게 응답 / 정적인 페이지 HTML, 이미지, CSS, JS 파일을 웹
클라이언트에 제공할 때 웹 서버 사용 !! )

웹 어플리케이션 서버 ( 웹 서버로부터 동적 페이지 요청을 받아서 요청을 처리하고 그결 과를 웹서버에 반환 / 주로 동적 페이지 생성을 위한 프로그램 실행과 DB 연동 기능 !)

정적 페이지란 누가 언제 요구하더라도 항상 같은 내용을 표시하는 웹 페이지 

동적 페이지는 누가 언제, 어떻게 요구 했는지에 따라 각각 다른 내용을 반환함 !!


웹 라이브러리(파이썬) 

사용자 프로그램 -> 웹 프로그래밍(urllib 패키지) -> http(패키지, http.client, http.cookiejar)
사용자 프로그램 -> 웹 서버 프로그래밍 -> 웹 프레임워크(Django, FLask, Tornado) -> http(패키지, http.cookie, http.server)

urllib(고수준 api), http(저수준 api)

urllib => URL의 분해, 조립, 변경 및 URL 문자 인코딩, 디코딩을 처리하는 함수 ! 

urlparse() url 파싱한 결과 ParseResult 인스턴스 반환 
(scheme => URL에 사용된 프로토콜 의미 / netloc => 네트워크 위치 / path => 파일이나 어플리케이션 경로 의미 
/ params => 어플리케이션에 전달될 매개변수 의미 / query => 질의 문자열 또는 매개변수로 앰퍼샌드(&)로 구분된 이름 = 값 쌍 형식으로 표시
, fragment 문서 내의 앵커 등 조각을 지정)

urllib.request => URL에서 데이터를 가져오는 기능을 제공 / urlopen() 형식 사용
urlopen(url, data=None, [timeout])
URL로 GET/POST 방식의 간단처리. PUT,HEAD 메소드등 헤더 조작이 필요한 경우에는 Request 클래스 같이 사용, 인증/쿠키/프록시 해당 핸들러 클래스와 같이 사용 

http.client => 연결객체생성 -> 요청을 보냄 -> 응답 객체 생성-> 응답데이터를 읽음 -> 연결을 닫음 

HTTPSever ( 웹 서버를 만들기위한 클래스, 서버 ip와 port로 바인딩함 / 핸들러 클래스 반드시 필요)
BaseHTTPRequestHandler ( 핸들럴르 만들기 위해 기반 클래스, HTTP 프로토콜 처리로직이 들어있음 / 클래스 상속받아 자신의 로직 처리를 담당하는 핸들러 클래스 만듬)
SimpleHTTPReqeustHandler(BaseHTTPRequestHandler 클래스를 상속받아 만든 클래스 , GET, HEAD 메소드 처리가 가능)
CGIHTTPReqeustHandler(SimpleHTTPReqeustHandler클래스를 상속받아 만든 클래스, Post, cgi 처리가 가능한 핸들러 클래스)

WSGI => GCI 방식의 단점을 보완하고.. 웹서버와 웹 어플리케이션 간에 연동 규격을 정의한 것이.. WSGI 규격 ..

Request ->(웹서버) -> 파라미터 전달 -> (wsgi 서버) -> call -> (application) -> return ->(wsgi) -> 처리결과 -> (웹서버) -> 응답

개발에 필요한 어플리케이션을 함수 또는 클래스 메소드 정의 (environ => HTTP_HOST, HTTP_USER_AGENT, SERVER_PROTOCOL 과 같은 HTTP 환경변수 포함 / start_response : 어플리케이션 내에서 응답을 시작하기 위해 반드시 호출해야하는 함수) ->>
start_response 함수 인자 정해져있음(status, headers 사용 ) -> 어플리케이션 함수의 리턴값은 응답 바디에 해당하는 내용으로 리스트나 제너레이터와 같은 iterable 타입이여야함 ! 

Django 웹 프레임워크 

pip install Django로 설치함 !!

개발 방식 

모듈화된 단위 프로그램 => 어플리케이션 .. 

MVT 패턴 

기존 MVC(Model-View-Controller) 패턴이란 데이터 , 사용자 인터페이스 데이터를 처리하는 로직을 구분해서 한 요소가 다른 요소들에 영향을 주지 않도록 설계하는 방식 ..

MVT는 Model-View-Templete 패턴으로 사용 => 모델은 db에 저장되는 데이터를 의미 / 템플릿은 ui 부분 / 뷰는 실직적으로 프로그램 로직 동작하여 구성하는 부분 !

웹 클라이언트 -> REQUEST (URLconf) -> view -> CRUD(MODEL<-> DB) -> view -> template ..

URLconf - url 정의 .. 요청에 들어있는 URL이 urls.py 파일에 정의된 URL 패턴과 매칭되는 지를 분석 !
(URL/뷰 매핑을 URLconf 라고함 ! )
ex) path('', views.a_b), ''이 url, views.a_b가 뷰(처리함수) 입니다.

setttings.py => 프로젝트 전반적인 사항을 설정해주는 곳.. 

admin 사이트 꾸미기 ..

데이터 입력 및 수정 => add or change 버튼 눌러 questions 테이블 제목 클릭 / 입력 수정 가능 

필드 순서 변경 -> ModelAdmin class를 상속 받아 새로운 클래스 정의.. 2번째 인자로 등록해주면 순서가 변경된 것으로 볼 수 있음 
필드셋을 이용하여 각각 튜플, dict 타입으로 묶어주면 다른 필드로 분리 가능 .. 
필드에 'classes': ['collapse'] 식으로 작성하면 필드를 접을 수 있음 !

한 화면에 띄우기 위해서는 클래스를 하나 만들고 원래 클래스에 그것과 같다는 리스트로 묶으면 한 화면에 띄울 수 있음 

테이블 형식으로 띄우려면 TabularInline을 이용하면 가능 

리스트를 만들어서 컬럼을 지정하면 레코드 리스트에 보여지는 컬럼 항목으로 지정가능 

list_filter 를 추가하면 필터 사이드바를 추가한 것과 같음 

search_fields => 검색박스가 추가됨 !!

Create 
q = Question(question_text="hi what`s your name", pub_date=timezone.now())
q.save()

Read
Question.objects.all()
Question.objects.filter(question_text__starswith="What').exclude(pub_date__get=datetime.date.today()).
filter(pub_date__gte=datetime(2019, 1,30))

one = Question.objects.get(pk=1)

Question.objects.all()[:5]
Question.objects.all()[:10:2]

update

q.question_next = "What is your favorite color?"
q.save()
Question.objects.filter(pub_date__year=2007).update(question_text="Everything is same')

Delete 

Question.object.filter().delete()
Question.objects.all().delete()

템플릿 변수 ..{{ }}

템플릿 문법에서 .는 lookup 다음 순서로 찾기로 쓰임 .. 
TEMPLATE_STRING_IF_INVALID

템플릿 필터 .. {{ name|lower }}
필터란 일반적인 용어로 어떤 객체나 처리 결과에 추가적으로 명령을 적용하여 해당 명령에 맞게 최종 결과를 변경하는 것을 말함 
ex) 네임변수를 모두 소문자로 바꿔줌 ]

템플릿 테그 .. {% tag %} 꼴로 사용 ..

{% for %} 태그 /{% endfor %}

{% if %} {% elif %} {% else %} {% endif %}

{% csrf_token}
 => post 방식의 form을 사용하는 템플릿 코드를 위해 사용을 해줌!

{% url %} 태그 !!
{% with %} 태그 !! => 특정 값을 변수에 저장해두는 기능 
{% load %} 태그 => 태그는 사용자 정의 태그 및 필터를 로딩해줌

템플릿 주석 => 템플릿 안에 #를 써주거나 {% comment %} {% endcomment %}를 사용해줘야함 !

{% extends "base.html" %} => base.html을 상속받음 
{% block %}{% endblock %}을 많이 사용함 !!
form.is_valid(): => 폼 데이터가 유효한지 검사함 !!
{{form.as_table/p/ul}} => <tr>/<p>/<ul> 태그로 감싸서 랜더링 되게 해줌!!

클래스형 뷰 !! => 상속과 믹스인 기능을 사용해서 코드를 재사용할 수 있고. 뷰를 체계적으로 구성 가능 !!

ex) a.views import Aview 이런식으로 쓰면서 path('', Aview.as_view()) 이런식으로 받음 !! as_view는 클래스로 진입하기 위한 클래스 메소드임 !!
as_view는 클래스의 인스턴스 생성, 인스턴스의 dispatch() 메소드를 호출 / dispatch() 메소드는 요청을 검사해서 get, post 등의 어떤 http 메소드로 요청되었는지 읽고 메소드로 중계해줌!!

views.py에 클래스를 작성하고 안에 함수를 적으면서 뷰 로직을 작성하고 리턴을 시킴 

클래스 뷰로 만들면 효율적인 메소드 구분이 가능함 !!
get, post에서 메소드 처리 기능 시 if 함수를 사용하지 않고 메소드명으로 구분할 수 있으므로 코드 구조가 깔끔해짐
다중 상속과같은 객체 지향 기술이 가능해지므로 여러가지 클래스 등을 사용 가능 !

기존에 함수형에서는 if문으로 get을 받는 방법을 사용했는데 클래스형 뷰로 작성하면 ,제레닉 뷰에서 View를 임포트해서 받고 
def get(self, request):로 만들어서 뷰로직을 작성해주기만 하면 된다.

상속 기능 가능 .. 제네릭뷰를 사용해서 할 수 있음 .. 제네릭뷰가 단순 반복 작업을 줄여줌 .. 

뷰 개발 과정에서 공통적으로 사용할 수 있는 기능들을 추상화하고 이를 장고에서 미리 만들어서 기본적으로 제공해주는 아임!
urls에서 urlpattern에 Aboutview를 임포트 시키고 views 파일에는 generic 으로 templateView를 임포트 시킨 후에
클래스로 지정하고 teplate_name='about.html' 식으로 작성을 해주면 됨 !
아니면 urls 파일에 templateView를 임포트 시키고 Templateview.as_view(이름)을 적어도됨 !!
```


