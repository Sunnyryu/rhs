# celery와 redis를 연동하여 django를 이용해보기!
# pip install 'celery[redis]'로 celery와 redis 연동을 위한 디펜던시를 한번에 설치 
# redis를 설치하고 redis 서버를 실행 후 Django Project 만들기
# settings.py에 아래의 문구 추가 
#BROKER_URL = 'redis://localhost:6379/0'
#CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' 

# celery -A config worker --loglevel=info로 celery 실행 !
# shell을 이용해서 tasks.py에 있는 add를 임포트 후 함수에 정의한 것을 실행하면  celery에 추가가 됨 !


