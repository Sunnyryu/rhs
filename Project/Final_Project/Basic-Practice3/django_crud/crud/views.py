from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'crud/index.html')
def new(request):
    return render(request, 'crud/new.html')
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title)
    print(content)
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return render(request, 'crud/create.html')
