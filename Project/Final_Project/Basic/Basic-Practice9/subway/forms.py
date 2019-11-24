from .models import Subway
from django import forms


MENU = [
    ('햄', "햄"),
    ('치킨데리야끼', "치킨데리야끼"),
    ('터키', "터키"),
    ('로스트 치킨', "로스트 치킨"),
    ('스파이시 이탈리안', "스파이시 이탈리안")

]

BREAD = [
    ('위트', "위트"),
    ('허니오트', "허니오트"),
    ('하티', "하티"),
    ('파마산 오레카노', "파마산 오레카노")
]

SAUCE = [
    ('마요네즈', "마요네즈"),
    ('스윗 칠리',"스윗 칠리"),
    ('사우스 웨스트', "사우스 웨스트"),
    ('사우전 아일랜드', "사우전 아일랜드")
]

VEG = [
    ('피망', "피망"),
    ('양파', "양파"),
    ('피클', "피클"),
    ('올리브', "올리브")


]

DRINK = [
    ('사이다', "사이다"),
    ('콜라', "콜라"),
    ('환타', "환타"),
]
class subwayForm(forms.ModelForm):
    class Meta:
        model = Subway
        fields = ['name', 'address', 'menu', 'bread', 'vegetable', 'sauce', 'drink']
        widgets = { 
            'menu' : forms.Select(choices=MENU),
            'bread' : forms.RadioSelect(choices=BREAD),
            'sauce' : forms.CheckboxSelectMultiple(choices=SAUCE),
            'vegetable' : forms.CheckboxSelectMultiple(choices=VEG),
            'drink' : forms.RadioSelect(choices=DRINK)
        }
