import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from player import playerData
from flask_paginate import Pagination, get_page_args
from playersearch import playerSearch
from playerid import playerId
from nba_api.stats.endpoints import playercareerstats, playerawards, commonplayerinfo, shotchartdetail, leagueleaders
import json
import pandas as pd
from playeriddata import playeridData
import requests
from playergraph import playerGraph
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib._cm_listed import cmaps as cmaps_listed
from matplotlib import colors
from IPython.display import display
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import OffsetImage
from datetime import date, datetime, timedelta
from ts30 import TS30
import os
from mvp import PredMVP
app = Flask(__name__)
app.debug = True
rows = playerData()
ts30s = TS30()
predrows = PredMVP()
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['new'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

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
    pagination_searchrows = get_searchrows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('search.html',
                            searchrows=pagination_searchrows,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )


@app.route('/newpage', methods=['GET','POST'])
def newpage():
    playerid = request.args.get('playerid')
    playeridrows= playeridData(playerid)
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
    return render_template('newpage.html', careertables=careertables,
    careertables1=careertables1,  careertables2=careertables2,
    playeridrows=playeridrows, playerid=playerid, awardstables=awardstables,
    infotables=infotables, infotables1 = infotables1, playergraph=playergraph)

@app.route('/explain')
def explain():
    return render_template('explain.html')

def get_ts30s(offset, per_page):
    return ts30s[offset: offset + per_page]


@app.route('/newpage2', methods=['GET', 'POST'])
def newpage2():
    playerid2 = request.args.get('playerid')
    playeridrows= playeridData(playerid2)
    preparets = playercareerstats.PlayerCareerStats(player_id=playerid2)
    tsframe = preparets.get_data_frames()
    tsextract = int(tsframe[1].FGA[0])
    tsextract2 = int(tsframe[1].FTA[0])
    tsextract3 = int(tsframe[1].PTS[0])
    FGPCT = float(tsframe[1].FG_PCT[0]*100)
    TSA = 2*(tsextract+0.44*tsextract2)
    TS = round((tsextract3*100/(2*(tsextract+0.44*tsextract2))),1)
    page = int(request.args.get('page', 1))
    per_page = 10
    offset = (page - 1) * per_page
    total = len(ts30s)
    pagination_ts30s = get_ts30s(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    shoter = shotchartdetail.ShotChartDetail(league_id="00",team_id="0", player_id=playerid2, season_nullable="")
    # season_nullable을 ""로 하는 것은 전체 커리어를 보기 위해서 임
    shotframe = shoter.get_data_frames()
    shotdata = shotframe[0]
    with pd.option_context('display.max_columns', None):
        display(shotdata.head())

    sns.set_style("white")
    sns.set_color_codes()
    plt.figure(figsize=(12,11))
    plt.scatter(shotdata.LOC_X, shotdata.LOC_Y)
    def draw_court(ax=None, color='black', lw=2, outer_lines=False):
        # 코트를 그리기 위한 함수
        if ax is None:
            ax = plt.gca()
        hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

        outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                              fill=False)
        inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                              fill=False)

        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                             linewidth=lw, color=color, fill=False)
        bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                                linewidth=lw, color=color, linestyle='dashed')
        restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                         color=color)
        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                                   color=color)
        corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)

        three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                        color=color)
        center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                               linewidth=lw, color=color)
        center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                               linewidth=lw, color=color)
        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                          bottom_free_throw, restricted, corner_three_a,
                          corner_three_b, three_arc, center_outer_arc,
                          center_inner_arc]

        if outer_lines:
            outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                    color=color, fill=False)
            court_elements.append(outer_lines)
        for element in court_elements:
            ax.add_patch(element)

        return ax
    plt.figure(figsize=(12,11))
    draw_court(outer_lines=True)
    plt.xlim(-300,300)
    plt.ylim(-100,500)

    plt.figure(figsize=(12,11))
    plt.scatter(shotdata.LOC_X, shotdata.LOC_Y)
    draw_court(outer_lines=True)
    plt.xlim(300,-300)
    draw_court()
    plt.figure(figsize=(12,11))
    plt.scatter(shotdata.LOC_X, shotdata.LOC_Y)
    plt.xlim(-250,250)
    plt.ylim(422.5, -47.5)
    joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                     kind='scatter', space=0, alpha=0.5)

    joint_shot_chart.fig.set_size_inches(12,11)
    ax = joint_shot_chart.ax_joint
    draw_court(ax)

    ax.set_xlim(-250,250)
    ax.set_ylim(422.5, -47.5)

    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')

    # 차트 위에 타이틀 추가
    ax.set_title('career shot graph',
                 y=1.2, fontsize=14)
    # 차트에 내용 추가
    ax.text(-250,445,'Data Source: nba'
            ,
            fontsize=12)
    fig = plt.gcf()
    plt.savefig('./static/img/graph1.png')
    cmap=plt.cm.YlOrRd_r
    joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                     kind='kde', space=0, color=cmap(0.1),
                                     cmap=cmap, n_levels=50)

    joint_shot_chart.fig.set_size_inches(12,11)
    ax = joint_shot_chart.ax_joint
    draw_court(ax)
    ax.set_xlim(-250,250)
    ax.set_ylim(422.5, -47.5)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')
    ax.set_title('career shot graph',
                 y=1.2, fontsize=18)

    ax.text(-250,445,'Data Source: nba'
            ,
            fontsize=12)
    fig2 = plt.gcf()
    plt.savefig('./static/img/graph2.png')

    cmap=plt.cm.gist_heat_r
    try:
        joint_shot_chart = sns.jointplot(shotdata.LOC_X, shotdata.LOC_Y, stat_func=None,
                                         kind='hex', space=0, color=cmap(.2), cmap=cmap)

        joint_shot_chart.fig.set_size_inches(12,11)

        ax = joint_shot_chart.ax_joint
        draw_court(ax)

        ax.set_xlim(-250,250)
        ax.set_ylim(422.5, -47.5)

        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(labelbottom='off', labelleft='off')


        ax.set_title('career shotchart', y=1.2, fontsize=14)

        ax.text(-250,445,'Data Source: nba', fontsize=12)


    except:
        print("선수의 슛데이터가 없습니다.")


    return render_template('newpage2.html',TS=TS, FGPCT=FGPCT, playerid2=playerid2, playeridrows=playeridrows, ts30s=pagination_ts30s, page=page, per_page=per_page, pagination=pagination,)

def get_predrows(offset, per_page):

    return predrows[offset: offset + per_page]

@app.route('/etc')
def etc():
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(predrows)
    pagination_predrows = get_predrows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('etc.html', predrows=pagination_predrows,
    page=page,
    per_page=per_page,
    pagination=pagination,)






if __name__ =='__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
