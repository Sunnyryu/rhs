from nba_api.stats.endpoints import playercareerstats
career = playercareerstats.PlayerCareerStats(player_id='201939')
temp = career.get_data_frames()
print(temp[0])
