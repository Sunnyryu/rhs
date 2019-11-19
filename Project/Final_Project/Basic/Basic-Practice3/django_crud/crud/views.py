from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    # python에서 정렬된  차순 변경 !
    #articles = Article.obejcts.all()[::-1]
    # objects 문에서 order by를 줘서 정렬된 차순을 변경!
    # articles = Article.objects.order_by('-id')
    context = {
            'articles':articles

            }
    return render(request, 'crud/index.html', context)
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
def detail(request, pk):
    article = Article.objects.get(pk=pk) # 인스턴스 방식에서는 오더바이를 사용할 수 없어서 filter방식으로 사용해서 filter(pk=pk).order_by('id') 이런 식으로 사용하면 가능! 그리고 받아주는 html에서 query set 값으로 해주면 쌉가능 
    # pk => id_exact = pk 랑 같으므로 사용가능 !! 
    context = {
            "article":article
            }
    return render(request, 'crud/detail.html', context)
def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    context = {

            "article":article


            }
    return render(request, 'crud/update.html', context)
def revise(request, pk):
    article = Article.objects.get(pk=pk)

    title= request.POST.get('title')
    content = request.POST.get('content')
    article.title= title
    article.content = content
    article.save()

    return redirect(f'/crud/{article.id}/article/')
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.delete()
    return redirect('/crud/')

