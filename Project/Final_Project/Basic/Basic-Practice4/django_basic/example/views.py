from django.shortcuts import render, redirect
from .models import Example

# Create your views here.
def index(request):
    example = Example.objects.all()
    context = {
            'example':example
            }
    return render(request, 'example/index.html', context)
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
def update(request, pk):
    example = Example.objects.get(pk=pk)
    context = {
            "example":example
            }
    return render(request, 'example/update.html', context)
def detail(request, pk):
    example = Example.objects.get(pk=pk)
    context = {
            "example":example
            }
    return render(request, 'example/detail.html', context)
def revise(request, pk):
    example = Example.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    example.title = title
    example.content = content
    example.save()

    return redirect(f'/example/{example.id}/example/')
def delete(request,pk):
    example = Example.objects.get(pk=pk)
    example.delete()
    return redirect('/example/')

    
