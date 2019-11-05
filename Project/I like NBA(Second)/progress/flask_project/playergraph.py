import pandas as pd
from nba_api.stats.endpoints import playercareerstats
#import json

def playerGraph(playerid):
    graphdata = playercareerstats.PlayerCareerStats(player_id=playerid)
    graphframe = graphdata.get_data_frames()
    graphdata2 = graphframe[1]
    astdata = graphdata2.AST
    rebdata = graphdata2.REB
    ptsdata = graphdata2.PTS
    stldata = graphdata2.STL
    blkdata = graphdata2.BLK
    tovdata = graphdata2.TOV
    gpdata = graphdata2.GP
    pfdata = graphdata2.PF
    if stldata[0]==None:
        steal=0
    else:
        steal=int(stldata[0])

    if blkdata[0]==None:
        block=0
    else:
        block=int(blkdata[0])
    if tovdata[0]==None:
        turnover=0
    else:
        turnover=int(tovdata[0])
    if astdata[0]==None:
        assist=0
    else:
        assist=int(astdata[0])
    if rebdata[0]==None:
        rebound=0
    else:
        rebound=int(rebdata[0])
    if ptsdata[0]==None:
        ptsdata=0
    else:
        point=int(ptsdata[0])
    if gpdata[0]==None:
        gp=0
    else:
        gp=int(gpdata[0])
    if pfdata[0]==None:
        pf=0
    else:
        pf=int(pfdata[0])
    playergraph=[]
    playergraph.append(point/gp)
    playergraph.append(assist*4.67*0.8/gp)
    playergraph.append(rebound*2.73*0.8/gp)
    playergraph.append(steal*15.12*0.9/gp)
    playergraph.append(block*23.24*0.7/gp)
    playergraph.append(turnover*8.17*0.8/gp)
    playergraph.append(pf*5.5*1.1/gp)
    #playergraph = json.dumps({'PPG':point/gp, 'RPG':rebound/gp, 'APG':assist/gp, 'SPG':steal/gp, 'BPG':block/gp,
    #'TPG':turnover/gp, 'PFG':pf/gp}, indent=4)
    return playergraph
