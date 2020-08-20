##flask 

#### rest_api 

```python 

# 기본적으로 flask_restful api는 json을 지원함 !
# 에 Flask-RESTful은 Python표준 라이브러리에서 json모듈을 사용 (flask json 기능에는 파이썬 json에 없는 직렬화 기능이 있기에!!)
app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

class MyConfig(object):
    RESTFUL_JSON = {'separators': (', ', ': '),
                    'indent': 2,
                    'cls': MyCustomEncoder}
# If the application is running in debug mode (app.debug = True) and either sort_keys or indent are not declared in the RESTFUL_JSON configuration setting, Flask-RESTful will provide defaults of True and 4 respectively.

class AllCapsString(fields.Raw):
    def format(self, value):
        return value.upper()


# example usage
fields = {
    'name': fields.String,
    'all_caps_name': AllCapsString(attribute=name),
}
#사용자 정의 출력 필드를 사용하면 내부 개체를 직접 수정하지 않고도 사용자 고유의 출력 형식을 수행할 수 있음
def odd_number(value):
    if value % 2 == 0:
        raise ValueError("Value is not odd")

    return value
# 구문 분석 인수의 경우 사용자 지정 검증을 수행할 수 있으며, 고유의 입력 유형을 생성하면 요청 구문 분석 쉽게 확장 가능 !
# format을 사용해서 에러메세지에 변수 사용 가능 !

api = Api(app)

@api.representation('text/csv')
def output_csv(data, code, headers=None):
    pass
    # implement csv output!
# text, csv, html도 지원 가능 !!

def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp
# data리소스 방법에서 반환하는 개체, 코드는 예상되는 HTTP상태 코드, 헤더는 응답에서 설정할 HTTP헤더임 !

class Api(restful.Api):
    def __init__(self, *args, **kwargs):
        super(Api, self).__init__(*args, **kwargs)
        self.representations = {
            'application/xml': output_xml,
            'text/html': output_html,
            'text/csv': output_csv,
            'application/json': output_json,
        }
#
app = Flask(__name__)
api = flask_restful.Api(app, catch_all_404s=True)
# 사용자가 오류 지정 처리가 가능 !

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
} 
# 상태 코드도 지원 가능 !!

```

```python 

myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
# 디렉토리 구조의 예!

# blueprint를 사용해서 어플리케이션 라우팅이 가능함 !! /

```
