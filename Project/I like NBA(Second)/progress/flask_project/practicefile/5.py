for i in range (0, 403):
   predMVP = (int(startframe[0].PTS[i])+1.1*int(startframe[0].OREB[i])+0.8*int(startframe[0].DREB[i])+1.05*int(startframe[0].AST[i])+1.1*int(startframe[0].STL[i])
   +1.05*int(startframe[0].BLK[i])-0.7*int(startframe[0].PTS[i])-0.9*int(startframe[0].TOV[i])-0.35*int(startframe[0].PF[i]))/float(startframe[0].GP[i])

   print(predMVP)


for i in range (0, 403):
   predName = startframe[0].PLAYER[i]
   a = {predName}
   print(a)

start = leagueleaders.LeagueLeaders()
startframe = start.get_data_frames()
df = pd.DataFrame(columns=['no', 'fullname', 'predmvppoint'])
for no in range(0, 403):
    fullname = startframe[0].PLAYER[no]
    predmvppoint =  (int(startframe[0].PTS[no])+1.1*int(startframe[0].OREB[no])+0.8*int(startframe[0].DREB[no])+1.05*int(startframe[0].AST[no])+1.1*int(startframe[0].STL[no])
    +1.05*int(startframe[0].BLK[no])-0.7*int(startframe[0].PTS[no])-0.9*int(startframe[0].TOV[no])-0.35*int(startframe[0].PF[no]))/float(startframe[0].GP[no])
    df = df.append(pd.DataFrame([[no, fullname, predmvppoint]], columns=['no', 'fullname', 'predmvppoint']), ignore_index= True)
df.set_index('no', inplace=True)
print(df)
