import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from player import playerData
from flask_paginate import Pagination, get_page_args
from playersearch import playerSearch
from playerid import playerId
from nba_api.stats.endpoints import playercareerstats, playerawards, commonplayerinfo
import json
import pandas as pd
from playeriddata import playeridData
import requests
from playergraph import playerGraph

app = Flask(__name__)
app.debug = True
rows = playerData()


def get_rows(offset, per_page):

    return rows[offset: offset + per_page]

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(rows)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index.html',
                           rows=pagination_rows,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

def get_searchrows(offset, per_page):
    fullname = request.args.get('fullname') # get 방식
    searchrows = playerSearch(fullname)
    return searchrows[offset: offset + per_page]

@app.route('/search', methods=['GET','POST'])
def search():
    fullname = request.args.get('fullname') #검색어 받아오기
    #fullname = request.args.get('fullname') get 방식
    #fullname = request.form['fullname'] post 방식
    searchrows = playerSearch(fullname) # 쿼리 수행
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(searchrows)
    #print(searchrows)
    pagination_searchrows = get_searchrows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    print(pagination)
    return render_template('search.html',
                            searchrows=pagination_searchrows,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )


@app.route('/newpage', methods=['GET','POST'])
def newpage():
    playerid = request.args.get('playerid')
    print(playerid)
    playeridrows= playeridData(playerid)
    print(playeridrows)
    career = playercareerstats.PlayerCareerStats(player_id=playerid)
    careerframe = career.get_data_frames()
    careertables=[careerframe[0].to_html(classes='data')]
    careertables1=[careerframe[1].to_html(classes='data1')]
    careertables2=[careerframe[8].to_html(classes='data2')]
    awards = playerawards.PlayerAwards(player_id=playerid)
    awardsframe = awards.get_data_frames()
    awardstables = [awardsframe[0].to_html(classes='awards')]
    info = commonplayerinfo.CommonPlayerInfo(player_id=playerid)
    infoframe = info.get_data_frames()
    infotables = [infoframe[0].to_html(classes='info')]
    infotables1 = [infoframe[1].to_html(classes='info1')]
    playergraph = playerGraph(playerid)
    print(playergraph)
    print(type(playergraph))
    return render_template('newpage.html', careertables=careertables,
    careertables1=careertables1,  careertables2=careertables2,
    playeridrows=playeridrows, playerid=playerid, awardstables=awardstables,
    infotables=infotables, infotables1 = infotables1, playergraph=playergraph)

#@app.orute('/newpage2', methods=['GET', 'POST'])
#def newpage2():



if __name__ =='__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
