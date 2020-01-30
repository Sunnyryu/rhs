##flask 

#### rest_api 

```python

# 구문 분석 !
# Look only in the POST body
parser.add_argument('name', type=int, location='form')

# Look only in the querystring
parser.add_argument('PageSize', type=int, location='args')

# From the request headers
parser.add_argument('User-Agent', location='headers')

# From http cookies
parser.add_argument('session_id', location='cookies')

# From file uploads
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')


parser.add_argument('text', location=['headers', 'values'])# 다양한 위치를 할 떄는 list로 가능 !!

#  상속을 위한 구문 

parser = reqparse.RequestParser()
parser.add_argument('foo', type=int)

parser_copy = parser.copy()
parser_copy.add_argument('bar', type=int)

# parser_copy has both 'foo' and 'bar'

parser_copy.replace_argument('foo', required=True, location='json')
# 'foo' is now a required str located in json, not an int as defined
#  by original parser

parser_copy.remove_argument('foo')
# parser_copy no longer has 'foo' argument

# 오류 처리 구문 

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('foo', type=int, required=True)
parser.add_argument('bar', type=int, required=True)

# If a request comes in not containing both 'foo' and 'bar', the error that
# will come back will look something like this.

{
    "message":  {
        "foo": "foo error message",
        "bar": "bar error message"
    }
}

# The default behavior would only return the first error

parser = RequestParser()
parser.add_argument('foo', type=int, required=True)
parser.add_argument('bar', type=int, required=True)

{
    "message":  {
        "foo": "foo error message"
    }
}

app.config['BUNDLE_ERRORS'] = True # 글로벌 설정을 재 정의 /

# 오류 메세지 
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument(
    'foo',
    choices=('one', 'two'),
    help='Bad choice: {error_msg}'
)

# If a request comes in with a value of "three" for `foo`:

{
    "message":  {
        "foo": "Bad choice: three is not a valid choice",
    }
}
```

```python 

# output field 

from flask_restful import Resource, fields, marshal_with
# 2개는 str  / 1 개는 datetime 타입으로 가능 
resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

class Todo(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        return db_get_todo()  # Some function that queries the db

# _with는 실제로 데이터 객체를 취해 필드 필터링을 적용하는 것입니다. / Marshalling은 단일 객체, 지시 또는 객체 목록에 대해 작동할 수 있습니다

class Todo(Resource):
    def get(self, **kwargs):
        return marshal(db_get_todo(), resource_fields), 200

fields = {
    'name': fields.String(attribute='private_name'),
    'address': fields.String,
}
# 람다식이나 중첩된 식으로도 사용 가능 . lambda x : x._private_name 이나 list.0.dictionary.name 등으로도 대체가능 

fields = {
    'name': fields.String(default='Anonymous User'),
    'address': fields.String,
}
# default를 이용한 기본값 사용 가능 


class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"

fields = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}
# 비트 1은 노말 , 비트 2는 리드, 언리드로 나타낼수 있음 !! .flagsattribute는 "Normal"또는"Urgent"항목을 나타내고, 비트 2는 "Read"또는"Unread"를 나타냅니다. 이러한 항목은 bitfield에 저장하기 쉬울 수 있지만 사용자가 읽을 수 있는 출력을 위해 해당 항목을 별도의 문자열 필드로 변환하는 것이 좋음 

class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random.random()

fields = {
    'name': fields.String,
    # todo_resource is the endpoint name when you called api.add_resource()
    'uri': fields.Url('todo_resource'),
    'random': RandomNumber,
}

fields = {
    'uri': fields.Url('todo_resource', absolute=True)
    'https_uri': fields.Url('todo_resource', absolute=True, scheme='https')
} # absolute=True =. 기본 체계 재정의  / scheme 인수 가능 


resource_fields = {'name': fields.String}
resource_fields['address'] = {}
resource_fields['address']['line 1'] = fields.String(attribute='addr1')
resource_fields['address']['line 2'] = fields.String(attribute='addr2')
resource_fields['address']['city'] = fields.String
resource_fields['address']['state'] = fields.String
resource_fields['address']['zip'] = fields.String
data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
json.dumps(marshal(data, resource_fields))'{"name": "bob", "address": {"line 1": "123 fake street", "line 2": "", "state": "NY", "zip": "10468", "city": "New York"}}'

# json 형태나 list 형태로도 가능함 !!/  list로 필드를 정렬 해제도 가능함 / dict를 안쓰고 nest field로 대체할 수도 있음 !!


```
