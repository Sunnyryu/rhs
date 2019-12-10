from django import forms
from .models import Book

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'preface']


class BookForm(forms.Form):
    name = forms.CharField(max_length=20)
    preface = forms.CharField(max_length=100)

    # 일반 Form 에서도 ModelForm 처럼 form.save() 동작이 가능하게~
    def save(self, commit=True):
        self.instance = Book(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance

