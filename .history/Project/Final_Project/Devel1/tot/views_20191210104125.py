from django.shortcuts import render, redirect
from pytrends.request import TrendReq
from datetime import datetime, time, timedelta
import json
# Create your views here.
def index(request):
    
    return render(request, 'tot/index.html') 

def graph(request):
    words = request.GET.get('q')
    if not words:
        return redirect('tot:index')
    date = request.GET.get('y')
    a = ','
    pytrends = TrendReq()
    #pytrends = TrendReq(hl='ko', tz=540)
    if a not in words:
        if request.GET.get('y')=='year':
            date = 'today 12-m'
        elif request.GET.get('y')=='month':
            date = 'today 1-m'
        else:
            date = 'now 7-d'
        word1 = words
        list1 = word1
        print(f'{date}')
        pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='')
        print('2222222222222222')
        value = pytrends.interest_over_time()
        del value['isPartial']
        value = value.reset_index()
        value2 = value.to_json(force_ascii=False, orient='split', date_format='iso', date_unit='s')
        abc = json.loads(value2)
        ab = []
        cd = []
        for a in abc['data']:
            k = {}
            h = datetime.strptime(a[0],'%Y-%m-%dT%H:%M:%SZ')
            h2 = h.strftime('%Y-%m-%d %H:%M:%S')
            k['label'] = h2
            k['y'] = a[1]
            k['link'] = '/anal'
            ab.append(k)
        
        context = {'ab':ab, 'word1':word1}
        return render(request, 'tot/graph.html', context)
    elif a in words:
        pass
        words = words.split(',')
        word1 = words[0]
        word2 = words[1]
        if request.GET.get('y')== 'year':
            date = 'today 12-m'
        elif request.GET.get('y') == 'month':
            date = 'today 1-m'
        else:
            date = 'now 7-d'
        list1 = [word1, word2]
        pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='')
        value = pytrends.interest_over_time()
        del value['isPartial']
        value = value.reset_index()
        value2 = value.to_json(force_ascii=False, orient='split', date_format='iso', date_unit='s')
        abc = json.loads(value2)
        ab = []
        cd = []
        for a in abc['data']:
            k = {}
            z = {}
            h = datetime.strptime(a[0],'%Y-%m-%dT%H:%M:%SZ')
            h2 = h.strftime('%Y-%m-%d %H:%M:%S')
            k['label'] = h2
            k['y'] = a[1]
            k['link'] = '/anal'
            ab.append(k)
            z['label'] = h2
            z['y'] = a[2]
            z['link'] = '/anal'
            cd.append(z)
        context = {'ab':ab, 'cd':cd, 'word1':word1, 'word2':word2}
        return render(request, 'tot/graph.html', context)



    
