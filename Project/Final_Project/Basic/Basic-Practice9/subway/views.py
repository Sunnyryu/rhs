from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubwayForm
from .models import Subway

# Create your views here.
def index():
    subways = Subway.objects.all()

    context = {
        'subways' : subways
    }
    return render(request, 'subway/index.html', context)
    
def new(request):
    if request.method == "POST":
        form = SubwayForm(request.POST)
        if form.is_valid():
            subway = form.save()
            return redirect(subway)

    form = SubwayForm()
    context={
        'form':form
    }
    return render(request, 'subway/form.html', context)

def detail(request, s_id):
    subway = get_object_or_404(Subway, id=s_id)

    context = { 'subway':subway}

    return render(request, 'subway/detail.html', context)

def delete(request, s_id):
    subway = get_object_or_404(Subway, id=s_id)

    if request.method == "POST":
        subway_delete()
    return redirect('subway:index')
    
def edit(request, s_id):
    subway = get_object_or_404(Subway, id=s_id)

    if request.method == "POST":
        form = SubwayForm(request.POST, instance=subway)
        if form.is_valid():
            sub = form.save()
            return redirect(sub)
    else:
        form = SubwayForm(subway.__dict__)
    
    context = {
        "form":form 
    }

    return render(request, 'subway/form.html', context)
