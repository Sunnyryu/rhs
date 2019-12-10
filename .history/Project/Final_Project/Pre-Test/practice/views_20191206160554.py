from django.shortcuts import render
from pytrends.request import TrendReq
from datetime import datetime, time, timedelta
from .harvesta import harvesta
from .preproca import preproca
#from django.http import JsonResponse
import pandas as pd
import json
import requests
import sys 
import subprocess
#from dateutil.parser import parse


# Create your views here.

def index(request):
    return render(request, 'practice/index.html')

def graph(request):
    word1 = request.GET.get('word1')
    word2 = request.GET.get('word2')
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    #print(word1)
    #print(date1)
    #print(type(date1))
    pytrends = TrendReq()

    list1 = [word1, word2]
    pytrends.build_payload(list1, cat=0, timeframe= 'today 5-y', geo='', gprop='')
    # pytrends.build_payload(list1, cat=0, timeframe= '20190201 20191125', geo='', gprop='')
    # timeframe : now 7-d , now 1-d, now 1-H, now 4-H, today (1,2,3)-m => today 3-m , today 5-y ,all
    value = pytrends.interest_over_time()
    del value['isPartial']
    value = value.reset_index()
    value2 = value.to_json(force_ascii=False, orient='split', date_format='iso', date_unit='s')
    #value3 = value.to_json(force_ascii=False, orient='records', date_format='iso')
    #value4 = value.to_json(force_ascii=False, orient='index', date_format='iso')
    #value5 = value.to_json(force_ascii=False, orient='columns', date_format='iso')
    #value5 = value.to_json(force_ascii=False, orient='values', date_format='iso')
    #for value5 range in (0,5):
    abc = json.loads(value2)
    
    ab = []
    cd = []
    ef = []
    for a in abc['data']:
        k = {}
        z = {}
        u = {}
        
        print(type(a[0]))
        print(a[0])
        h = datetime.strptime(a[0],'%Y-%m-%dT%H:%M:%SZ')
        print(f'{h} : {type(h)}')
        h2 = h.strftime('%Y-%m-%d %H:%M:%S')
        print(h2)
        k['label'] = h2
        k['y'] = a[1]
        k['link'] = '/anal'
        ab.append(k)
        z['label'] = h2
        z['y'] = a[2]
        z['link'] = '/anal'
        cd.append(z)
        #u['y'] = a[1]
        #ef.append(u)
    

    
    #value7 = value.to_json(force_ascii=False, orient='table')
    
    #value2 = value.to_csv(encoding="utf-8")
    #value2 = value.to_json(force_ascii=False)
    #value2 = value.to_json(force_ascii=False, orient='records')
    context = {'ab':ab, 'cd':cd, 'word1':word1, 'word2':word2 }
    return render(request, 'practice/graph.html', context)
def anal(request):
    date = request.GET.get('date')
    keyword = request.GET.get('keyword')
    datebf7 = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    date = datebf7.stftime('%Y%m%d %H:%M:%S')
    datebf8 = datebf7 + timedelta(days=-7)
    datebf8 = datebf8.strftime('%Y%m%d %H:%M:%S')
    date = date[0:10]
    datebf8 = datebf8[0:10]
    startpath = './'
    print(datebf7)
    print(date) 
    print(keyword)
    keyword_source_dic = {'ENTERPRISE':[keyword]}
    outPath = harvesta.harvest(startpath, datebf7, date, keyword_source_dic)
    preproca.preproc(outPath)
    p = subprocess.Popen(['./practice/analyzas/analyza.py',outPath])
    p.wait()
    print("finish")

    return render(request, 'practice/anal.html')
