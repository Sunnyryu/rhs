## Basic6

#### python Django 6


```
Form class

 Model class와 유사

 일반 Form
   - 항목을 일일히 지정함
 Model Form
  - 모델을 기반으로 항목이 정해져있음

일반 폼 선언하는 방법
class (모델명)Form(forms.Form)
class BoardForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

모델 폼 선언 방법
forms.py 에서 작성(파일은 만들어 줘야함)
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        field = ['title', 'content']

Form 주요역할
    - 입력 폼 html을 알아서 생성해줌.
    - 입력 폼의 값을 검증
    - 검증에 통과된 값을 Dictionary 타입으로 제공

----
IPython 설치 (쥬피터노트북..)
 - 파이썬의 기본 대화형 쉘의 기능을 향상시킨 도구.
 - 디버깅이 편리
 - tab 자동완성!!
------


form.as_p : p 태그로 내용을 감싸줌
form.as_table : trtd 태그로 내용을 감싸줌.(table 태그는 미리 써줘야함)
form.as_ul : 순서 없는 list tag로 감싸줌. (ul 태그를 미리 붙여줘야함)


- get_absolute_url

- get_object_or_404


1: N 관계

- user : board = 1:N
참조 board.user
board.user.id
board.user.name 

역참조

user.board_set.all()
for b in user.board_set.aa():
  b.title
  b.content
  
N : M 관계!?
user : board = N:M 
ex) 좋아요 버튼 누르는 관계.. 한 유저가 여러 게시글에 좋아요를 남기거나 받을 수 있기에..

1. 1번 사람이 작성한 게시글을 다가져오려면?
u1 = User.objects.get(id=1)
u1.board_set_fall()

2. 1번 사람이 작성한 모든 글의 댓글을 표시
for board in u1.board_set.all():
    for comment in board.comment_set.all():
        print(comment.content)

3. 2번째 댓글을 쓴 사람은 ?
com2 = Comment.objects.get(id=2)
com2.user

4. 2번 댓글을 쓴 사람의 이름은?
com2.user.name

5. 2번 댓글을 쓴 사람의 게시글은?
com2.user.board_set.all()

6. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
ti = Board.objects.get(id=1)
ti.comment_set.first().user.name
ti.comment_set.all()[0].user.name

6-1. 1번 글의 마지막 댓글을 쓴 사람의 이름?
ti.comment_set.last().user.name
ti.comment_set.all().reverse()[0].user.name

7. 1번 글의 2번째 부터 4번째 까지 댓글을 가져오기 !
ti.comment_set.all()[1:4]

8. 1번 글의 첫번째, 두번째 댓글을 가져오면?
ti.comment_set.all()[:2]

9. 1번 글의 두번째 댓글을 쓴 사람의 첫번째 게시물의 작성자 이름은 ?
ti.comment_set.all()[1].user.board_set.all()[0].user.name
#k = Board.objects.get(id=1)
#c =c.user.board_set.all()[0].user.name


10-1. 모든 댓글에서 content 정보만 가지고 온다면?
Comment.objects.values('content')

10-2. 1번 댓글의 content 정보를 가지고 온다면?
Comment.objects.values('content').get(id=1)

11. 2번 사람이 작성한 댓글을 content에 내림차순으로 정렬 
u2 = User.objects.get(id=2)
u2.comment_set.order_by('-content')

12. 1글 이라는 제목인 게시글
a1 = Board.objects.filter(title="1글")
Board.objects.filter(title__contains="글") - 글이라는 이름이 포함된 제목인 게시글을 보여주려면!!

1-N의 한계

N:M은 중계 모델을 가지고 함!

1. 손님 1의 입장에서 판매 정보를
p1 = Person.objects.get(pk=1)
p1.sales_set.all()

2. 주류 1 입장에서 판매정보
al = Alcohol.objects.get(pk=1)
al.sales_set.all()

3. 주류 2의 입장에서 판매정보
al2 = Alcohol.objects.get(pk=2)
al2.sales_set.all()

4. 손님 1의 주류 목록을 보고 싶다면?
손님 1 sales_set 접근가능
sales 주류로 접근가능 
for sales in p1.sales_set.all():
    print(sales.alcohol.name)
    print(sales.person.name)
    print(sales.alcohol.id)

5. 중계 모델 없이 접근을 하고 싶다면? - 장고에 알려줘!


ManyToMany(참조할 모델, through="중개 모델")

1. 소주를 마신 사람들 
alcohol1.people.all()

2. 1번 손님의 주류 목록
person1 = Person.objects.get(pk=1)
person1.alcohol_set.all()
person1.alcohols.all()


중개 테이블을 지워도 장고에서 만들어줌!

중개 테이블에 데이터를 추가하는 방법 !
person1.alcohols.add(alcohol1)
alcohol2.people.add(person1)
person1.alcohols.remove(alcohol2)

추가 에시
like_users: 좋아요를 누른 유저
like_boards : 좋아요가 눌린 게시글 

사용가능 ORM 
board.user : 게시글을 작성한 유저 
board.like_users : 게시글을 좋아요 누른 유저 
user.board_set.all() : 유저가 작성한 게시글들 
user.like.boards.all() :유저가 누른 좋아요 모음 !

쿼리셋 
person = Person.objects.filter(first_name="팽수")

if / for 문 돌릴 때 값이 필요함 ! / 지연 평가를 함 
for p in person:
    print(p)
  
for p in person:
    print(p)

 city = City.objects.filter(name=인천)
if 문 에서는 확인만 필요하고 값을 따로 쓰지 않을 떄는 exists()를 사용 
-캐시에 쿼리셋이 저장되지 않음!

대용량의 데이터를 처리할 때는 iterator()

rabbits = Rabbit.objects.all()

if rabbits.exists():
    for rabbit in rabbits.iterator():
        print(rabbit)
---------------------------
atom = Atom.objects.all()

atom_iterator = atom.iterator()

try:
    first_atom = next(atom_iterator)
except StopIteration:
    pass    
else:
    from itertool import chain
    for at in chain ([first_atom], atom):
        print(at)

```
