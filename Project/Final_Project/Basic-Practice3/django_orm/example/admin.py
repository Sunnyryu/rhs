from django.contrib import admin
from .models import Example
# Register your models here.



class ExampleAdmin(admin.ModelAdmin):
    fields = ['content', 'title'] # 필드 순서를 조정할 수 있음 
    list_display = ['title', 'updated_at'] # 업데이트 날짜가 나옴
    list_filter = ['updated_at'] # 필터 사이드 메뉴
    search_fields = ['title', 'content'] # 검색창을 만들 수 있음



admin.site.register(Example, ExampleAdmin) admin 사이트 등록!

