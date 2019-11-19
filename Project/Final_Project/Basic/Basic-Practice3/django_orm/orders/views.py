from django.shortcuts import render
from orders.models import Subway

# Create your views here.
def index(request):
    return render(request, 'order/index.html')

def order(request):
    return render(request, 'order/order.html')
def order_result(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    sand = request.POST.get('sand')
    size = request.POST.get('size')
    bread = request.POST.get('bread')
    check = request.POST.getlist('check')
    context = {
            'name':name,
            'date':date,
            'sand':sand,
            'size':size,
            'bread':bread,
            'check':",".join(check)
            }
    order = Subway()
    order.name = name
    order.date = date
    order.sandwitch = sand
    print(sand)
    order.size = size
    order.bread = bread
    order.check = ",".join(check)
    order.save()


    return render(request, 'order/order_result.html', context)
def neworder(request,id):
    id = str(id)
    neworder = None
    context = None
    try:
        neworder= Subway.objects.get(id=id)
        context = {
                'name':neworder.name,
                'date':neworder.datetime,
                'sand':neworder.sandwitch,
                'size':neworder.size,
                'bread':neworder.bread,
                'check':neworder.check
                }
        return render(request, 'order/neworder.html', context)
    except:
        print('id에 존재하는 값이 없음')
        return render(request, 'order/neworder2.html')
    print(context)
