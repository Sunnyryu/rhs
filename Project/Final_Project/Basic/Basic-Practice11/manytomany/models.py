from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}번 술꾼 {self.name}'

class Alcohol(models.Model):
    name = models.CharField(max_length=20)
    #people = models.ManyToManyField(Person, through='Sales', related_name="alcohols")  # 어떤 테이블이랑 n:m인지 첫번쨰에 명시해주고 , 두 번째는 중개목록을 나타내주면 되옵니다. 
    people = models.ManyToManyField(Person, related_name="alcohols")
    def __str__(self):
        return f'주류 no.{self.id} : {self.name}'

#class Sales(models.Model):
#    person = models.ForeignKey(Person, on_delete=models.CASCADE)
#    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
#    판매시간 = models.DateTimeField()
#    def __str__(self):
#        return f'{self.person}이 마시는 {self.alcohol}'
