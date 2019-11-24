from django.shortcuts import render, redirect
from .models import Form
from IPython import embed

# Create your views here.
def index(request):
    forms = Form.objects.all()
    context = { "forms":forms }
    return render(request, 'form/index.html', context)

def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        form = Form()
        form.title = title
        form.content = content
        form.save()
        return redirect("form:index")
    else:
        return render(request, 'form/new.html')
def detail(request, form_id):
    form = Form.objects.get(id=form_id)

    context = {
            "form":form
            }

    return render(request, 'form/detail.html', context)
