# -*- coding: utf-8 -*-
#daumFuncs.py

import requests
from bs4 import BeautifulSoup
import urllib.request
import re


# #--------------------------------------------------------------------------
# # 실시간 인기 검색어 cnt개 반환
# #--------------------------------------------------------------------------
# def getKeywords():
#     try:
#         html = requests.get("https://www.daum.net", timeout=10).text
#         soup=BeautifulSoup(html, 'html.parser')
#         title_list = soup.select(".list_mini .rank_cont .link_issue")

#         htmllist = []
#         for top in title_list:
#             htmllist.append(top.get_text())
#     except Exception as e:
#         print(e)
#         return []
#     else:
#         return htmllist


#--------------------------------------------------------------------------
# 검색어로 뉴스를 검색하여 cnt개 반환
#--------------------------------------------------------------------------
def get_newslist(search_words, cnt, datebf7, date):
    encText = urllib.parse.quote(search_words)
    furl = "https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q="
    surl = "&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p="
    lurl = "&sd="+datebf7+"000000&ed="+date+"235959&period=u"

    newsList = []
    oldLast = "I'm Old"
    i = 1
    while len(newsList) < cnt: # cnt개 채울 때 까지
        try:
            res = requests.get(furl + encText + surl + str(i) + lurl)
            soup = BeautifulSoup(res.content, 'html.parser')
            urlname = soup.select(".f_link_b")
            urllink = soup.select("a[class*=f_link_b]")
            urllink = [ re.sub(r"\?f=o", "", url.get('href'))
                    for url in urllink ]
            print(urlname,"888")
            # 뉴스가 모자라면 그만 둠
            if len(urlname) == 0:
                break

            # 같은 뉴스면 그만 둠
            currentLast = urllink[len(urllink)-1]
            if currentLast == oldLast:
                break
            oldLast = currentLast

            for list1, list2 in zip(urlname, urllink):
                if len(newsList) >= cnt: break # 뉴스를 다 채우면 중단
                print("daum: " + list1.text, list2)
                newsList.append({"title" : list1.text, "link" : list2})
            i += 1 # 다음 페이지

        except Exception as e:
            print(e)
    return newsList


#--------------------------------------------------------------------------
# module test code
#--------------------------------------------------------------------------
if __name__ == "__main__":
    # daumkeywords = getKeywords()
    # print(daumkeywords)
    newsList = get_newslist("삼성전자", 20,"20190210","20190211") #1 키워드
    print(newsList)
    for news in newsList:
        print(news['title'], news['link'])
