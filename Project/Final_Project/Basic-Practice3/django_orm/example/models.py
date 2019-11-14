from django.db import models

# Create your models here.
class Example(models.Model): # 첫글자는 대문자로 !, (models.Model) => import된 models의 Model을 이용하기 위해!
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성한 시간 관리를 위해!
    updated_at = models.DateTimeField(auto_now=True) # 수정한 시간을 자동으로 하기 위해 auto_now를 통해 등록을 해줌
    
    def __str__(self): #__ = 던더?
        return f'{self.id} : {self.title}'
    # 여기서 리턴된 값이 어드민이 받는다고 생각하면 되옵니다.
    # 메소드이므로 .. 따로 마이그레이션을 안해줘도 되옵니다.! 
    # 단 커맨드에는 저장이 안되었으므로 커맨드를 다시 실행시켜줘야함!
        
