from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board 
        fields= ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] # ('comment',) 튜플은 1개 일 때 ,를 찍어줘야함 
