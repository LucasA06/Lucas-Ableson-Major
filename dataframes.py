import soccerdata as sd
import pandas as pd

fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref1 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref2 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref3 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref4 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])
fbref5 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1718']) 

fbref6 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref7 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref8 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref9 =  sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref10 =sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])
fbref11 =sd.FBref(leagues=['ENG-Premier League'], seasons=['1718'])

team_stats = fbref.read_team_season_stats(stat_type='standard')
df = pd.DataFrame(team_stats)
df.to_csv('team_stats.csv', index=False)

player_stats = 

