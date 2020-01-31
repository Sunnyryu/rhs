from django.shortcuts import render

# Create your views here.
def index():
    return render(request, 'iced/index.html')
