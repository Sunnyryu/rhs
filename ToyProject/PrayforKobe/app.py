from flask import Flask, request, render_template, url_for
from nba_api.stats.endpoints import *
from career_reg import Career_reg
from career_post import Career_post
from total_post import Total_post
from total_reg import Total_reg
from awards import Awards
from ts import Ts
import os

app = Flask(__name__)
app.debug = True
career_rows = Career_reg()
career_post_rows = Career_post()
total_post_rows = Total_post()
total_rows = Total_reg()
awards_rows = Awards()
ts_rows = Ts()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record')
def record():
    kobe_record = career_rows
    kobe_post_record = career_post_rows
    kobe_total_post_record = total_post_rows
    kobe_total_record = total_rows
    return render_template('record.html', kobe_record=kobe_record, 
    kobe_post_record=kobe_post_record, kobe_total_post_record=kobe_total_post_record, kobe_total_record=kobe_total_record)

@app.route('/award')
def award():
    kobe_award = awards_rows
    return render_template('award.html',kobe_award=kobe_award)

@app.route('/analysis')
def analysis():
    kobe_TS = ts_rows
    PTS = int(ts_rows[0]['PTS'])
    FTA = int(ts_rows[0]['FTA'])
    FGA = int(ts_rows[0]['FGA'])
    FGPCT = float(ts_rows[0]['FG_PCT']*100)
    TSA = 2*(FGA+0.44*FTA)
    TS = round((PTS*100/(2*(FGA+0.44*FTA))),1)
    print(TS)
    return render_template('analysis.html',TS=TS)










if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)

