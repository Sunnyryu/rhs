from django.shortcuts import render, redirect
from game.models import Subway

# Create your views here.
def index(request):
    return render(request, 'game/index.html')
def detail(request):
    name= request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    menu = request.POST.get('menu')
    bread = request.POST.get('bread')
    drink = request.POST.get('drink')
    sauce = request.POST.getlist('sauce')
    context = {
            'name':name,
            'address':address,
            'phone':phone,
            'menu':menu,
            'bread':bread,
            'drink':drink,
            'sauce':",".join(sauce)
            }
    order = Subway()
    order.name = name
    order.address = address
    order.phone = phone
    order.menu = menu
    order.bread = bread
    order.drink = drink
    order.sauce = ",".join(sauce)
    order.save()
    return render(request, 'game/detail.html', context)
def new(request):
    order = Subway.objects.all()
    context = {
            'order':order
            }
    return render(request, 'game/new.html', context)
def newdetail(request, id):
    sub = Subway.objects.get(id=id)
    context = {
            "sub":sub
            }
    return render(request, 'game/newdetail.html', context)
def update(request,id):
    sub = Subway.objects.get(id=id)
    context = {
            "sub": sub
            }
    return render(request, 'game/update.html', context)
def delete(request, id):
    sub = Subway.objects.get(id=id)
    context = {
            "sub" : sub
            }
    return redirecte('/new/')
