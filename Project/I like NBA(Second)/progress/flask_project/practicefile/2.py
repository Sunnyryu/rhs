from nba_api.stats.endpoints import playercareerstats, playerawards, commonplayerinfo, shotchartdetail

for i in range (1,100):
    a = playercareerstats.PlayerCareerStats(i)
    a1= a.get_data_frames()
    tsextract = int(a1[1].FGA[0])
    tsextract2 = int(a1[1].FTA[0])
    tsextract3 = int(a1[1].PTS[0])
    TS = round((tsextract3/(2*(tsextract+0.44*tsextract2))),2)
    print(TS)
