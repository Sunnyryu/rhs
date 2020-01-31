from django.contrib import admin
from .models import Question, Choice

#class ChoiceInline(admin.StackedInline): # Question 및 choice 한화면 변경
class ChoiceInline(admin.TabularInline): # 테이블 형식 보여주는 것
    model = Choice
    extra = 2

class QustionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] # 필드 순서 변경
    fieldsets = [ # 각 필드 분리해서 보여주기
            ('Qustion Statement', {'fields': ['question_text']}),
            #('Date Information', {'fields': ['pub_date']}),
            ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 필드 접기..
    ]
    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date') # 레코드 리스트 컬럼 항목 지정
    list_filter = ['pub_date'] # 필터 사이드 바 추가
    search_fields = ['question_text'] # 검색 박스 추가 
            
            

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
