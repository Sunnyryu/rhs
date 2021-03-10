from django.shortcuts import render, redirect
from pytrends.request import TrendReq
from datetime import datetime, time, timedelta
from .harvesta import harvesta
from .preproca import preproca
import json
import requests
import sys
import subprocess
import os
import DateTime
from math import log10
from konlpy.tag import Mecab
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import shutil
import nltk
import re
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from konlpy.tag import Mecab
#from nltk.corpus import treebank
from .models import Keyword
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import csv
import os.path
from dotenv import load_dotenv
load_dotenv()
# Create your views here.
def index(request):

    return render(request, 'tot/index.html')

def graph(request):
    print(os.getcwd())
    words = request.GET.get('q')
    if not words:
        return redirect('tot:index')
    date = request.GET.get('y')
    a = ','
    pytrends = TrendReq(timeout=(5,35))
    #pytrends = TrendReq(hl='ko', tz=540, timeout=(5, 35))
    print(pytrends)
    try:
        if a not in words:
            if request.GET.get('y')=='year':
                date = 'today 12-m'
            elif request.GET.get('y')=='month':
                date = 'today 1-m'
            else:
                date = 'now 7-d'
            word1 = words
            list1 = [word1]
            pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='')
            #pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='youtube')
            value = pytrends.interest_over_time()
            #print(value)
            del value['isPartial']
            value = value.reset_index()
            value2 = value.to_json(force_ascii=False, orient='split', date_format='iso', date_unit='s')
            value_dict = json.loads(value2)
            value_word1 = []
            for a in value_dict['data']:
                k = {}
                h = datetime.strptime(a[0],'%Y-%m-%dT%H:%M:%SZ')
                h2 = h.strftime('%Y-%m-%d %H:%M:%S')
                k['label'] = h2
                k['y'] = a[1]
                #k['link'] = '/anal'
                value_word1.append(k)
            dict1 = pytrends.related_queries()
            dict2 = dict1[f'{word1}']
            newdict1 = {}
            if len(dict2['top']['value']) > 10:
                newdict1 = dict2['top'][0:10]
                newdict1 = newdict1.to_dict()
            else:
                newdict1 = dict2['top']
                newdict1 = newdict1.to_dict()
            context = {'vw1':value_word1, 'word1':word1, 'newdict1': newdict1, 'date':date}
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
            pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='US', gprop='')
            value = pytrends.interest_over_time()
            del value['isPartial']
            value = value.reset_index()
            value2 = value.to_json(force_ascii=False, orient='split', date_format='iso', date_unit='s')
            value_dict = json.loads(value2)
            value_word1 = []
            value_word2 = []
            for a in value_dict['data']:
                k = {}
                z = {}
                h = datetime.strptime(a[0],'%Y-%m-%dT%H:%M:%SZ')
                h2 = h.strftime('%Y-%m-%d %H:%M:%S')
                k['label'] = h2
                k['y'] = a[1]
                #k['link'] = '/anal'
                value_word1.append(k)
                z['label'] = h2
                z['y'] = a[2]
                #z['link'] = '/anal'
                value_word2.append(z)
            dict1 = pytrends.related_queries()
            dict2 = dict1[f'{word1}']
            dict3 = dict1[f'{word2}']
            newdict1 = {}
            newdict2 = {}
            if len(dict2['top']['value']) > 10:
                newdict1 = dict2['top'][0:10]
                newdict1 = newdict1.to_dict()
            else:
                newdict1 = dict2['top']
                newdict1 = newdict1.to_dict()
            if len(dict3['top']['value']) > 10:
                newdict2 = dict3['top'][0:10]
                newdict2 = newdict2.to_dict()
            else:
                newdict2 = dict3['top']
                newdict2 = newdict2.to_dict()


            context = {'vw1':value_word1, 'vw2':value_word2, 'word1':word1, 'word2':word2, 'newdict2':newdict2, 'newdict1':newdict1, 'date':date}
            return render(request, 'tot/graph.html', context)
    except:
        return redirect('tot:index')


def search(request):
    if request.GET.get('word2'):
        word1 = request.GET.get('word1')
        word2 = request.GET.get('word2')
        word3 = request.GET.get('cd')
        date = request.GET.get('date')
        list1 = [word1, word2]
        pytrends = TrendReq(hl='ko', tz=540, timeout=(7, 35))
        pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='youtube')
        dict1 = pytrends.related_queries()
        dict2= dict1[f'{word3}']
        bubble = []
        if len(dict2['top']['value'])>10:
            for n in range(0,10):
                bbw1 = {}
                bbw1['text'] = dict2['top']['query'][n]
                bbw1['count'] = dict2['top']['value'][n]
                bubble.append(bbw1)
        else:
            for n in range(0, len(dict2['top']['value'])):
                bbw1 = {}
                bbw1['text'] = dict2['top']['query'][n]
                bbw1['count'] = dict2['top']['value'][n]
                bubble.append(bbw1)
        context = {'bubble':bubble, 'date':date}

        return render(request, 'tot/search.html', context)
    else:
        word1 = request.GET.get('word1')
        word3 = request.GET.get('cd')
        date = request.GET.get('date')
        list1 = [word1]
        pytrends = TrendReq()
        pytrends.build_payload(list1, cat=0, timeframe= f'{date}', geo='', gprop='youtube')
        dict1 = pytrends.related_queries()
        dict2= dict1[f'{word3}']
        bubble = []

        if len(dict2['top']['value'])>10:
            for n in range(0,10):
                bbw1 = {}
                bbw1['text'] = dict2['top']['query'][n]
                bbw1['count'] = dict2['top']['value'][n]
                bubble.append(bbw1)
        else:
            for n in range(0, len(dict2['top']['value'])):
                bbw1 = {}
                bbw1['text'] = dict2['top']['query'][n]
                bbw1['count'] = dict2['top']['value'][n]
                bubble.append(bbw1)
        context = {'bubble':bubble, 'date':date}
        return render(request, 'tot/search.html', context)

def youtube(request):
    date = request.GET.get('date')
    text = request.GET.get('text')
    return render(request, 'tot/youtube.html')

def anal(request):
    date = request.GET.get('date')
    keyword = request.GET.get('keyword')
    datebf7 = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    date1 = datebf7.strftime('%Y-%m-%d %H:%M:%S')
    date1 = date1[0:10]
    date1 = str(date1)
    print(date1,"힘내라 친구여")
    keyword3 = Keyword.objects.filter(word=keyword, date=date1).values().exists()
    print(keyword3, "키워드3")
    if keyword3:
        keyword2 = Keyword.objects.filter(word=keyword, date=date1).values()
        keyword_word = keyword2[0]['word']
        keyword_date = keyword2[0]['date']
        keyword_hwf = keyword2[0]['high_word_frequency']
        print(keyword_hwf)
        print(type(keyword_hwf))
        keyword_hwf_1 = json.loads(keyword_hwf, encoding='utf-8')
        print(keyword_hwf_1)
        print(type(keyword_hwf_1))
        keyword_hwf_2 = keyword_hwf_1
        print(keyword_hwf_2, "키워트hwf2")
        hwf_values = [i for i in keyword_hwf_2.values()]
        hwf_keys = [i for i in keyword_hwf_2.keys()]
        #print(hwf_values[0])
        #print(hwf_values)
        #print()
        #print(keyword_hwf_2)
        #print(keyword_hwf_2[f'{hwf_keys[2]}'])
        hwf_list = []
        for key in keyword_hwf_2.keys():
            st = {}
            st['text'] = key
            st['frequency'] = keyword_hwf_2[key]
            hwf_list.append(st)
        #print(hwf_list)
        #print(hwf_list)
        #print(hwf_keys[0])
        a = hwf_keys[0]
        b = hwf_keys[1]
        c = hwf_keys[7]
        print(hwf_list,"테스트")
        created = keyword2[0]['created'].strftime('%Y%m%d%H%M%S')
        urls, titles = read_csv(created)
        title_urls = zip(urls, titles)
        context = {'keyword_word':keyword_word, 'title_urls':title_urls, 'hwf_list':hwf_list, 'a':a, 'b':b, 'c':c}
        return render(request, 'tot/anal.html', context)
    else:
        #date = request.GET.get('date')
        #keyword = request.GET.get('keyword')
        #datebf7 = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        datebf8 = datebf7 + timedelta(days=-7)
        datebf8 = datebf8.strftime('%Y%m%d %H:%M:%S')
        date = datebf7.strftime('%Y%m%d %H:%M:%S')
        #date1 = datebf7.strftime('%Y-%m-%d %H:%M:%S')
        #date1 = date1[0:10]
        date = date[0:8]
        datebf7 = datebf8[0:8]
        startpath ='./'
        keyword_source_dic = {'ENTERPRISE':[f'{keyword}']}
        print(keyword_source_dic,"나는 어제가 좋아")
        outPath = harvesta.harvest(startpath, datebf7, date, keyword_source_dic)
        print(outPath,"나는 오늘이 좋아")
        preproca.preproc(outPath)
        current_time = datetime.today().strftime("%Y%m%d%H%M%S")
        print(current_time)
        #current_ymd = current_time[2:8]
        #current_time0 = current_time[8:10]
        #current_time2 = current_time[10:12]
        current_ymd = outPath[2:8]
        current_time0 = outPath[9:11]
        current_time2 = outPath[11:13]
        print(current_ymd, current_time0, current_time2)

        #print(os.path.isdir(f'/home/sunny/1919/test-tot/{current_ymd}/{current_time0}/'))
        #print(os.path.dirname(os.path.realpath(__file__)) )
        my_address = os.getcwd()
        my_direct =os.path.join(my_address, f'{current_ymd}/{current_time0+current_time2}/')
        print(my_direct)
        directory =f'{my_direct}/E_K_01/'
        outfile_name = "text.txt"
        out_file = open(outfile_name, 'w')
        files= os.listdir(directory)
        if os.path.isdir(f'{my_direct}'):
            for filename in files:
                if ".txt" not in filename:
                    continue
                file = open(directory + filename)
                for line in file:
                    out_file.write(line)
                out_file.write("\n")
                file.close()
            out_file.close()

        else:
            pass
        txtfile = open(f'{my_address}/text.txt', 'r',encoding="utf-8")
        readtxt = txtfile.read()
        txtfile.close()

        #corpus = [readtxt]
        #vectorizer = TfidfVectorizer()
        #sp_matrix = vectorizer.fit_transform(corpus)
        #word2id = defaultdict(lambda: 0)
        #for idx, feature in enumerate(vectorizer.get_feature_names()):
        #    word2id[feature] = idx

        #for i, sent in enumerate(corpus):
        #    #print('====== document[%d] ======' % i)
        #    print([(token, sp_matrix[i, word2id[token]]) for token in sent.split()])

        # POS tag a sentence
        kolaw_file = os.getenv("FILE_WHERE")
        shutil.copy('text.txt', kolaw_file)
        s = kolaw.open('a.txt').read()  # 한국 법률 말뭉치
        print(s)
        words = Mecab().pos(s)
        print(words,"000")

        # Define a chunk grammar, or chunking rules, then chunk # Noun phrase
        grammar = """
        NP: {<N.*>*<Suffix>?}   # Noun phrase
        VP: {<V.*>*}            # Verb phrase
        AP: {<A.*>*}            # Adjective phrase
        """
        parser = nltk.RegexpParser(grammar)
        print(parser,"123")
        chunks = parser.parse(words)
        print(chunks,"234")
        chunks = [chunk.leaves() for chunk in chunks if type(chunk) != tuple]

        # chunk를 본문과 같이 만들고 빈도 수 카운팅
        result = set()
        for chunk in chunks:
            seq = [w for w, t in chunk]
            pattern = '[ ]?'.join(seq)
            if len(pattern) < 2:
                continue
            seq_pattern = re.compile(pattern)
            founds = re.findall(seq_pattern, s)
            len_founds = len(founds)
            if not len_founds:
                continue
            ele = (founds[0], len_founds)
            #if len(set(founds)) > 1:
            #    ele = (tuple(set(founds)), len_founds)
            result.add(ele)

        result = sorted(list(result), key=lambda x: x[1], reverse=True)
        #pprint(result[0:10])  # print chunks and counting
        result2 = result[0:15]

        result3 = dict(result2)
        result4 = json.dumps(result3, ensure_ascii=False)
        print(result4,"테스트")
        #result2 = dict(result[0:10])
        #result2 = json.dumps(result2, ensure_ascii=False)
        keyword_db = Keyword.objects.create(word=keyword, date=date1, high_word_frequency=result4)
        print(keyword_db.created)
        created = keyword_db.created.strftime('%Y%m%d%H%M%S')
        #print(created,"값을 확인하기",date1)
        if current_time2 == created[10:12]:
            urls,titles=read_csv(created)
        else:
            urls,titles=read_csv2(outPath)
        title_urls = zip(urls,titles)
        #print(title_urls)
        # print(urls)
        # print(titles)
        #print(result2)
        context = {'result2': result2, 'readtxt': readtxt, 'title_urls': title_urls}
        print(context)
        #print(keyword_read_db)
        #print(keyword2)
        hwf_list = []
        #for mecab_word in result2:
        #    mecab_dict = {}
        #    mecab_dict['text'] = mecab_word[0]
        #    mecab_dict['frequency'] = mecab_word[1]
        #    hwf_list.append(mecab_dict)
        #print(hwf_list)

        return render(request, 'tot/anal.html', context)#, hwf_list)


def read_csv(current_time):
    #print(current_time)
    current_ymd = current_time[2:8]
    current_time0 = current_time[8:10]
    current_time2 = current_time[10:12]
    titles = []
    urls = []
    my_address = os.getcwd()
    #my_parents_address = os.path.abspath(os.path.join(my_address, os.pardir))
    my_direct =os.path.join(my_address, f'{current_ymd}/{current_time0+current_time2}/')
    print(my_direct)
    try:
        with open(f'{my_direct}/output.csv', 'r', encoding='utf-8-sig') as csv_file:
            # csv 파일을 Dictionary 형식으로 읽어옴.
            csv_data = csv.DictReader(csv_file, delimiter=",")
            for i in csv_data:
                titles.append(i['title'])
                urls.append(i['url'])
        return urls,titles
    except:
        current_time2 = int(current_time2) - 1
        current_time2=str(current_time2)
        with open(f'{my_direct}/output.csv', 'r', encoding='utf-8-sig') as csv_file:
            # csv 파일을 Dictionary 형식으로 읽어옴.
            csv_data = csv.DictReader(csv_file, delimiter=",")
            for i in csv_data:
                titles.append(i['title'])
                urls.append(i['url'])
        return urls,titles


def read_csv2(current_time):
    #print(current_time)
    current_ymd = current_time[2:8]
    current_time0 = current_time[9:11]
    current_time2 = current_time[11:13]
    titles = []
    urls = []
    my_address = os.getcwd()
    #my_parents_address = os.path.abspath(os.path.join(my_address, os.pardir))
    my_direct =os.path.join(my_address, f'{current_ymd}/{current_time0+current_time2}/output.csv')
    with open(f'{my_direct}', 'r', encoding='utf-8-sig') as csv_file:
        # csv 파일을 Dictionary 형식으로 읽어옴.
        csv_data = csv.DictReader(csv_file, delimiter=",")
        for i in csv_data:
            titles.append(i['title'])
            urls.append(i['url'])
    return urls,titles
