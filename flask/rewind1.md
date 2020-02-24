## flask

#### rewind 

```
플라스크는 파이썬 웹 프레임워크중 하나이며, 마이크로 프레임워크임 ! => 가장 핵심적인 요소만 포함하고 있음 / wsgi 코어와 URL 라우팅 지원하기 위해 WERKZEUG와 JINJA2 라이브러리와 배포/
static, templates 디렉토리를 기본으로 갖춰야함 !!

python app.py 로 실행하는 편임 !!

import_name => 어플리케이션 패키지의 이름을 지정하는 인자이며, 문자열 값으로 정의함 / 보통은 __name__ 변수를 넘겨서 어플리케이션 이름을 생성 
static_url_path => 정적 파일(css, image) 등 서비스하는 static_folder 폴더를 웹에서 접근할 때 지정 
static_folder => 정적파일을 서비스하는 폴더명 취급 !!
template_folder => 뷰함수가 사용할 html 파일이 위치하는 폴더명을 지정합니다.

글로벌 객체 
어플리케이션을 작성하다보면 종종 전역적으로 데이터를 보관하거나 사용할 일이 있는데 전역 영역은 어플리케이션 전체에 걸친 
영역이 아닌 모듈 단위의 영역으로 한정함 / 전역적으로 사용하려고 할 때 쓰임 / from flask import g 

사용자 응답 객체 생성
http 응답 헤서 요소를 추가하거나 응답 메세지의 형태를 변경해서 응답할 필요가 있음 !/ 사용자 응답 객체를 정의하여 사용하는 것이 효율적 
response_class => Response 클래스(또는 자식 클래스)로부터 생성한 인스턴스 객체
str => 유니코드가 아닌 일반 문자열 / unicode => 유니코드 문자열 / WSGI 함수 => 프로그래머가 정의한 WSGI 함수는 호출되면
버퍼링된 응답 객체로 반환 
튜플 => (response, status,headers) 형식을 갖춘 튜플을 인자로 제공 받음 !!
str 을 쓸떄는 "" / unicode를 쓸떄는 u""를 씀 

튜플로는 쓸떄 ()로 묶으며, 인자를 각각 제공 .. 

HTTP 요청 전후에 대한 핸들러 관리 
before_first_request: 웹 어플리케이션 기동 이후 가장 처음에 들어오는 HTTP 요청에서만 실행 
before_request : 매 HTTP 요청이 들어올 때 마다 실행 
after_request: 매 HTTP 요청이 끝나 브라우저에 응답하기 전에 실행 
teardown_request: HTTP 요청의 결과가 브라우저에 응답한 다음 실행하게 됩니다.
teardown_appcontext: HTTP 요청이 완전히 완료되면 실행되며, 어플리케이션 컨텍스트 내에서 실행됩니다.

HTTP 요청 전후에 호출되는 데코레이터 이용할 수 있음 

사용자 정의 URL 처리 함수 관리 
FLASK는 URL의 한부분으로 취급되는 값을 뷰함수에 인자로 전달함으로써 뷰함수에서 쉽게 참조 가능 !!

미들웨어 등록을 위한 순수 WSGI 객체 접근 
미들웨어는 HTTP 통신 과정에서 다양한 일을 처리할 수 있음 
- 타깃 URL에 따른 어플리케이션 기동에 필요한 HTTP 환경 재설정과 Request Path 재설정
- 다수의 어플리케이션 또는 다른 프레임워크의 프로그램을 같은 프로세스에서 동작시키기
- 네트워크의 대역폭 분산 처리를 위해 로드 밸런싱과 원격 처리
- 콘텐츠의 전치리(XSL Stylesheet 적용 등 )

미들웨어 등록은 Logmiddleware(app.wsgi_app)으로 함 ! 

디버그 모드 
app.debug = True 

app.config.update(
  DEBUG=True
)
두가지로 가능함!!(어디서 오류가 났는지 알 수 있는 디버그 콘솔을 지원함..)

라우팅 
url 디스패치 ~~ (flask에서 url을 처리하는 방법 )

http 메서드 타입은 브라우저가 http 서버에 url을 호출하는 세부적인 방법 / 예를 들어 출입문이 url이라고 보고 방범장치는 메서드 타입이라고 보자
보통은 get , post를 많이쓰며 그 외에도 pute,delete , head , options 등이 쓰임 

웹 브라우저의 주소 줄에 입력해 데이터를 전송할 때는 항상 GET 요청만을 받음 !!
뷰 함수로 정의할 경우 처리할 HTTP 메서드를 한정할 수 있음 ! 
하나의 뷰에서 여러가지 메소드를 받으려면 methods=['GET', 'POST']로 처리할 수 있음 
뷰 함수의 이름이 길거나 적절치 않은 이름이 쓰인다면 별칭을 지정하는 편이 좋음 / route 데코레이터 or add_url_rule 함수에 endpoint 인자로 전달 
기본값을 할당할 때는 defaults={'page':'index'} 처럼 설정할 수 있음 

route 데코레이터 / add_url_rule이 받는 것 
defaults => 사용자 url 변수에 기본값을 지정하느 옵션, 사전 타입으로 전달 가능 
methods => 뷰 함수가 처리할 http 메서드를 지정하는 옵션이며, 문자열을 요소값으로 가지는 리스트 전달 
host => 라우팅 요청이 어떤 호스텡 응답할지 지정, 문자열 전달 
subdomain => 뷰 함수가 특정 서브 도메인에만 응답하도록 지정하며, 문자열 타입으로 전달 
redirect_to => 라우팅 요청을 받았을 경우 뷰함수가 처리하지 않고 다른 곳으로 요청을 전달하며 , 문자열 값 또는 리다이렉션 함수를 인자로 받으며, 
리다이렉션 함수는 변숫값을 처리할 어댑터와 변숫값을 인자로 가짐 !!

app에서 subdomain에서 app.config['SERVER_NAME'] = X를 사용할떄 'SERVER_NAME'은 반드시 문자열이여야함 ! => X는 문자열 

다수의 서브 도메인을 특정 뷰함수에 응답하도록 하려면 app.route를 각각하고 return 시에 각각 문자를 써줘야함 !!
아니면 {}.format 을이용하고 특정 도메인이 아닌 변수 도메인을 만들어서 쓰면 됨 !
redirect_to는 어떤 사이트로 넘어갈 때 설정해두며 설정된 주소로 가게 되게 유도하는 것으로
redirect_to="/a" 이런식으로 설정하면 특정사이트를 들어갔을 때 a로 이동시켜줌 !!

여러 변수를 받고 redirect_to를 사용할 떄는 {}.format(변수1, 변수2)와 redirect 함수르 이용함 !! 

get 방식으로 사용해서 데이터를 받을 때는 request.args.get("변수1","변수2",..) 를 이용하며,
form 방식을 이용할 떄는 request.form.get("변수1","변수2",..)를 이용하며, value 속성인 경우에는 request.values.get("변수1","변수2",..)이며,
value 속성은 combinedMultiDict 데이터 타입이며, MultiDict 데이터 타입들이 합쳐진 형태임 !!
multidict 타입들의 wrapper로만 동작하므로 실제로 데이터에 접근하는 메서드는 multidict 타입의 메서드로 제공 
(get, getlist,add, setlist, setdefault, setlistdefault, clear, copy, deepcopy, pop ,poplist, update 등이 쓰임 )

특정 변수가 넘어오지 않았을 떄에는 
request.values.get("question","입력하세오") 등으로 입력하세요라는 것을 만들어서 다시 물을 수 있다. 
인자명을 사용해 전달할 경우 default 인자명과 함꼐 기본값을 전달해주면 됨 !

type 인자를 사용해서 미리 특정 객체로 변환해서 반환을 받을 수 있음 
request.values.get("answer", 1, type=int)

연-월-일 타입으로 넘어올 떄에는 datetime 모듈을 사용해서 datetime.strptime 등의 변수를 이용할 수 있음 !!
multidict()는 from werkzeug.datastructures import Multidict를 사용해 불러옴 !

environ 사전에서 제공되는 표준 환경 변수 
REQEUST_METHOD => 웹 브라우저가 보낸 요청의 처리 방식에 대한 문자열이 포함되어 있음.. 일반적으로 GET / POST 메서드 타입을 동시에 처리하는 메서드에서 처리 분기
SCRIPT_NAME => 어플리케이션 처리를 요청한 URL 의 첫부분으로 PHP 등의 스크립트 언어에서 변숫값은 스크립트 파일명으로 됨 !

받을 때마다 request.endpoint / request.url_rule / request.view_args, request.get_json() 형태로 받음 !!




```
