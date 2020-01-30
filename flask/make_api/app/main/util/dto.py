from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

# user라는 Namespace를 만들고 api 변수에 할당함
# 그리고 api.model을 이용해 user 데이터를 담을 필드를 만들어 줌
# Flask 안에서 User 데이터를 담에 전달할 수 있음

# User 데이터를 http로 처리할 controller를 만들어 줌
# controller 폴더 안에 user_controller.py 파일을 만들어 줌

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

