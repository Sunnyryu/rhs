from django.shortcuts import render
from pytrends.request import TrendReq
import pandas as pd
import json


# Create your views here.

def index(request):
    return render(request, 'practice/index.html')

def graph(request):
    word1 = request.GET.get('word1')
    word2 = request.GET.get('word2')
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    print(word1)
    print(date1)
    print(type(date1))
    pytrends = TrendReq()

    list1 = [word1, word2]
    pytrends.build_payload(list1, cat=0, timeframe= 'today 5-y', geo='', gprop='')
    # timeframe : now 7-d , now 1-d, now 1-H, now 4-H, today (1,2,3)-m => today 3-m , today 5-y ,all
    value = pytrends.interest_over_time()
    del value['isPartial']
    value = value.reset_index()
    value2 = value.to_json(force_ascii=False, orient='split', date_format='iso')
    #value3 = value.to_json(force_ascii=False, orient='records', date_format='iso')
    #value4 = value.to_json(force_ascii=False, orient='index', date_format='iso')
    #value5 = value.to_json(force_ascii=False, orient='columns', date_format='iso')
    #value5 = value.to_json(force_ascii=False, orient='values', date_format='iso')
    #for value5 range in (0,5):
    abc = json.loads(value2)
    
    ab = []
    cd = []
    for a in abc['data']:
        k = {}
        z = {}
        k['x'] = a[0]
        k['y'] = a[1]
        ab.append(k)
        z['x'] = a[0]
        z['y'] = a[2]
        cd.append(z)
    

    
    #value7 = value.to_json(force_ascii=False, orient='table')
 
    
    #value2 = value.to_csv(encoding="utf-8")
    #value2 = value.to_json(force_ascii=False)
    #value2 = value.to_json(force_ascii=False, orient='records')
    context = {'ab':ab, 'cd':cd, 'word1':word1, 'word2':word2}
    return render(request, 'practice/graph.html', context)
