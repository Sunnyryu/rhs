from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from email_validator import validate_email, EmailNotValidError


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired("제목 작성 필수")])
    content = TextAreaField('내용', validators=[DataRequired("내용 작성 필수")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired("아이디를 적어주십시요."), Length(min=3, max=25, message="3~25자로 만들어주세요.")])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired("비밀번호를 적어주세요.."), EqualTo('password2', '비밀번호가 일치하지 않습니다'), Length(min=4, max=12, message="암호는 4~12자로 만들어주세요."), ])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired("이메일은 필수입니다."), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])