from django.db import models
from django.conf import settings 

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL을 사용하는 이유는.. 일반적으로 settings.py에서 installed app 순서대로 가져오다보니, 순서가 맞지 않는 경우에 제대로 된 결곽가 안나올 수 있는데, 이 때 import 된 settings.AUTH_USER_MODEL 을 이용하면 에러 방지 !
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_boards", blank=True) # manytomanyfield를 설정하면 추가 테이블이 설정되욤  여기서는 board_id, user_id 필드가 생김
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment