#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import random
from faker import Faker
from datetime import datetime
fake = Faker('ko_kR')
# Create your views here.
def index(request):
    #return httpResponse('Hello DJango')
    return render(request, 'index.html')
#def age(request, age):
#    context = {'age':age} #dict 방식이기에 key:value로 나타냄!
#    return render(request, 'age.html', context)

def age(request, age):
    context = {'age':age**age}
    return render(request, 'age.html', context)

def plus(request, num1, num2):
    context = {'cal':num1 + num2}
    return render(request, 'cal.html', context)
def minus(request, num1, num2):
    context = {'cal':num1 - num2}
    return render(request, 'cal2.html', context)
def multiply(request, num1, num2):
    context = {'cal':num1 * num2}
    return render(request, 'cal3.html', context)
def divide(request, num1, num2):
    context = {'cal':num1 / num2}
    return render(request, 'cal4.html', context)
def cal(request, str, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if str == 'plus':
        context = {'cal':num1 + num2}
        return render(request, 'cal.html', context)
    elif str == 'minus':
        context = {'cal':num1 - num2}
        return render(request, 'cal.html', context)
    elif str == 'multiply':
        context = {'cal':num1 * num2}
        return render(request, 'cal.html', context)
    elif str == 'divide':
        context = {'cal':num1/num2}
        return render(request, 'cal.html', context)
    else :
        return render(request, 'error.html')

def profile(request, name, age):
    list_1 = ['시끄러운', '푸른', '적색', '조용한', '웅크린', '백색', '지혜로운', '용감한', '날카로운', '욕심많은']
    list_2 = ['늑대', '태양', '양', '매', '황소', '불꽃', '나무', '달빛', '말', '돼지', '하늘', '바람']
    list_3 =['~와(과) 함께 춤을', '~의 기상','~은(는) 그림자속에', '~의 환생','~의 죽음']

    i_name= random.choice(list_1)+random.choice(list_2)+random.choice(list_3)
    lotto = random.sample(range(1,47),6)
    lotto.sort()
    i_num = [ str(i) for i in lotto]
    context = {
            'name' : name,
            'age' : age,
            'i_name' : i_name,
            'lotto' : ",".join(i_num)

    }
    return render(request, 'profile.html', context)

def job(request, name):
    job = fake.job()
    #print("job",fake.job())
    context = {
            'name' : name,
            'job' : job
    }
    return render(request, 'job.html', context)

def image(request):
    num = random.choice(range(1, 200))
    url = f"https://picsum.photos/id/{num}/200/300"
    context = {
            'url' : url
    }
    print(context)
    return render(request, 'image.html', context)
def dtl(request):
    foods = ["짜장", "탕수육", "짬뽕", "양장피", "군만두", "고추잡채", "볶음밥"]
    my_sentence = "life is short, you need python"
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now() # 실제 시간
    empty_list = []

    context = {
        "foods" : foods,
        "my_sentence": my_sentence,
        "messages": messages,
        "timenow" : datetimenow,
        "empty_list": empty_list,
    }
    return render(request, 'dtl.html', context)
def birth(request):
    today = datetime.now()
    
    if today.month == 11 and today.date == 5:
        res = True
    else :
        res = False

    birth = datetime(2020, 11, 5)
    d_day = (birth-today).days


    context = {'result': res,
               'd_day' : d_day,
    }
    
    
    return render(request, 'birth.html', context, d_day)
    
