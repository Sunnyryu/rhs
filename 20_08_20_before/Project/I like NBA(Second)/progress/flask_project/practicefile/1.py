import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from player import playerData
from flask_paginate import Pagination, get_page_args
from playersearch import playerSearch
from playerid import playerId
from nba_api.stats.endpoints import playercareerstats, playerawards, commonplayerinfo, shotchartdetail
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
import os

for i in range(1, 10000) :
        a = playercareerstats.PlayerCareerStats(i)
        a1= a.get_data_frames()
        tsextract = int(a1[1].FGA[0])
        tsextract2 = int(a1[1].FTA[0])
        tsextract3 = int(a1[1].PTS[0])
        TS = round((tsextract3/(2*(tsextract+0.44*tsextract2))),2)
        print(TS)
