from django.shortcuts import render
from .models import Example

# Create your views here.
def index(request):
    return render(request, 'example/index.html')
def new(request):
    return render(request, 'example/new.html')
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    example = Example()
    example.title = title
    example.content = content
    example.save()
    return render(request, 'example/create.html')
    
