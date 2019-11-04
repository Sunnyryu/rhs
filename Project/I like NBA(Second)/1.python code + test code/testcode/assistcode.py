from nba_api.stats.endpoints import assistleaders
a = assistleaders.AssistLeaders(league_id="00",season="2018-19")
b = a.get_data_frames()
print(b)
