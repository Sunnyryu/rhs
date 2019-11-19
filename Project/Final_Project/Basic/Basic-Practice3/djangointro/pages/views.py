from django.shortcuts import render, redirect
import random
import requests

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
            'msg' : message,
            'msg2' : message2
    }
    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto_result(request):
    count = request.GET.get('count')
    # 현재 str로 받아오므로 int로 수정하기 위해 아래 문구 사용!
    count = int(count)
    lotto_num = []
    for i in range(count):
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
            'count': count,
            'lotto_num': lotto_num

            }
    
    #print(type(count))
    return render(request, 'result.html', context)

def comment(request):
    return render(request, 'pages/comment.html')

def text(request):
    comment = request.GET.get('comment')
    site = f'http://artii.herokuapp.com/make?text={comment}'
    
    return redirect(site)

def artii_form(request):
    return render(request, 'pages/artii_form.html')

def artii_result(request):
    text = request.GET.get('text')

    f_url = "http://artii.herokuapp.com/fonts_list"

    fonts= requests.get(f_url).text
    fonts = fonts.split('\n')
    font = random.choice(fonts)

    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    
    
    res = requests.get(url).text

    context = {
            'res' : res

            }

    return render(request, 'pages/artii_result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username= request.POST.get('name')
    password= request.POST.get('pw')
    context = {
            'username':username,
            'password':password

            }
    return render(request, 'pages/user_create.html', context)
def subway_add(request):
    return render(request, 'pages/subway_add.html')
def subway_result(request):
    name = request.POST.get('name')
    date = request.POST.get('date')
    sand = request.POST.get('sand')
    size = request.POST.get('size')
    bread = request.POST.get('bread')
    check = request.POST.getlist('check')
    print(check) 
    context = {
            'name':name,
            'date':date,
            'sand':sand,
            'size':size,
            'bread':bread,
            'check':",".join(check)
            }
    return render(request, 'pages/subway_result.html', context)
def example(request):
    return render(request, 'pages/example.html')
def index(request):
    return render(request, 'pages/index.html')

