import soccerdata as sd
import pandas as pd
import os

def create_directories():
    base_path = 'data/Team/Preimer League'
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_types = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    for season in seasons:
        for stat_type in stat_types:
            dir_path = os.path.join(base_path, f"{season}", stat_type)
            os.makedirs(dir_path, exist_ok=True)

def fetch_and_process_data(leagues, seasons, stat_type):
    all_data = []

    for season in seasons:
        fbref = sd.FBref(leagues=leagues, seasons=[season])
        data = fbref.read_team_season_stats(stat_type=stat_type.lower())

        # Columns to keep
        columns_to_keep = [col for col in data.columns if col not in ['Per 90 Minutes', 'Progression', 'url']]

        # Select only the columns to keep
        data = data[columns_to_keep]

        # Insert team names
        data.insert(0, 'Team', [
            'Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
            'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United',
            'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
            'Newcastle Utd', "Nott'ham Forest", 'Southampton', 'Tottenham',
            'West Ham', 'Wolves'
        ])
        all_data.append((season, pd.DataFrame(data)))
    
    return all_data

def save_data_to_csv(data, stat_type):
    base_path = 'data/Team/Preimer League'
    for season, df in data:
        dir_path = os.path.join(base_path, f"{season}", stat_type)
        file_path = os.path.join(dir_path, f'{stat_type.lower()}.csv')
        df.to_csv(file_path, index=False)

if __name__ == "__main__":
    create_directories()

    leagues = ['ENG-Premier League']
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_types = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    for stat_type in stat_types:
        data = fetch_and_process_data(leagues, seasons, stat_type)
        save_data_to_csv(data, stat_type)

'''if not os.path.exists('data'):
    os.makedirs('data\Team\#2024-2023\Standard')
    os.makedirs('data\Team\#2023-2022\Standard')
    os.makedirs('data\Team\#2022-2021\Standard')
    os.makedirs('data\Team\#2021-2020\Standard')
    os.makedirs('data\Team\#2020-2019\Standard')
    os.makedirs('data\Team\#2019-2018\Standard')
    os.makedirs('data\Team\#2024-2023\Keeper')
    os.makedirs('data\Team\#2023-2022\Keeper')
    os.makedirs('data\Team\#2022-2021\Keeper')
    os.makedirs('data\Team\#2021-2020\Keeper')
    os.makedirs('data\Team\#2020-2019\Keeper')
    os.makedirs('data\Team\#2019-2018\Keeper')
    os.makedirs('data\Team\#2024-2023\Shooting')
    os.makedirs('data\Team\#2023-2022\Shooting')
    os.makedirs('data\Team\#2022-2021\Shooting')
    os.makedirs('data\Team\#2021-2020\Shooting')
    os.makedirs('data\Team\#2020-2019\Shooting')
    os.makedirs('data\Team\#2019-2018\Shooting')
    os.makedirs('data\Team\#2024-2023\Passing')
    os.makedirs('data\Team\#2023-2022\Passing')
    os.makedirs('data\Team\#2022-2021\Passing')
    os.makedirs('data\Team\#2021-2020\Passing')
    os.makedirs('data\Team\#2020-2019\Passing')
    os.makedirs('data\Team\#2019-2018\Passing')
    os.makedirs('data\Team\#2024-2023\Defense')
    os.makedirs('data\Team\#2023-2022\Defense')
    os.makedirs('data\Team\#2022-2021\Defense')
    os.makedirs('data\Team\#2021-2020\Defense')
    os.makedirs('data\Team\#2020-2019\Defense')
    os.makedirs('data\Team\#2019-2018\Defense')
    os.makedirs('data\Team\#2024-2023\Miscellaneous')
    os.makedirs('data\Team\#2023-2022\Miscellaneous')
    os.makedirs('data\Team\#2022-2021\Miscellaneous')
    os.makedirs('data\Team\#2021-2020\Miscellaneous')
    os.makedirs('data\Team\#2020-2019\Miscellaneous')
    os.makedirs('data\Team\#2019-2018\Miscellaneous')
else:
    print('Data file already exists')

# Standard League Statistics
fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref0 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref1 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref2 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref3 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref4 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819']) 

# Keeper League Statistics
fbref5 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref6 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref7 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref8 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref9 =  sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref10 =sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])

# Shooting League Statistics
fbref11 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref12 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref13 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref14 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref15 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref16 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])

# Passing League Statistics
fbref17 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref18 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref19 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref20 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref21 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref22 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])

# Defence League Statistics
fbref23 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref24 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref25 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref26 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref27 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref28 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])

# Miscellaneous League Statistics
fbref29 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2324'])
fbref30 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
fbref31 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2122'])
fbref32 = sd.FBref(leagues=['ENG-Premier League'], seasons=['2021'])
fbref33 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1920'])
fbref34 = sd.FBref(leagues=['ENG-Premier League'], seasons=['1819'])

def add_teams(fbref_data):
    teams = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
             'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United',
             'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
             'Newcastle Utd', "Nott'ham Forest", 'Southampton', 'Tottenham',
             'West Ham', 'Wolves']
    fbref_data.insert(0, 'Team', teams)
    return fbref_data

def convert_to_dataframe(fbref_data):
    return pd.DataFrame(fbref_data)

fbref_data = fbref.read_team_season_stats(stat_type='standard')
fbref0_data = fbref0.read_team_season_stats(stat_type='standard')
fbref1_data = fbref1.read_team_season_stats(stat_type='standard')
fbref2_data = fbref2.read_team_season_stats(stat_type='standard')
fbref3_data = fbref3.read_team_season_stats(stat_type='standard')
fbref4_data = fbref4.read_team_season_stats(stat_type='standard')

fbref_data = add_teams(fbref_data)
fbref0_data = add_teams(fbref0_data)
fbref1_data = add_teams(fbref1_data)
fbref2_data = add_teams(fbref2_data)
fbref3_data = add_teams(fbref3_data)
fbref4_data = add_teams(fbref4_data)

fbref_data = convert_to_dataframe(fbref_data)
fbref0_data = convert_to_dataframe(fbref0_data)
fbref1_data = convert_to_dataframe(fbref1_data)
fbref2_data = convert_to_dataframe(fbref2_data)
fbref3_data = convert_to_dataframe(fbref3_data)
fbref4_data = convert_to_dataframe(fbref4_data)

fbref5_data = fbref5.read_team_season_stats(stat_type='keeper')
fbref6_data = fbref6.read_team_season_stats(stat_type='keeper')
fbref7_data = fbref7.read_team_season_stats(stat_type='keeper')
fbref8_data = fbref8.read_team_season_stats(stat_type='keeper')
fbref9_data = fbref9.read_team_season_stats(stat_type='keeper')
fbref10_data = fbref10.read_team_season_stats(stat_type='keeper')

fbref5_data = add_teams(fbref5_data)
fbref6_data = add_teams(fbref6_data)
fbref7_data = add_teams(fbref7_data)
fbref8_data = add_teams(fbref8_data)
fbref9_data = add_teams(fbref9_data)
fbref10_data = add_teams(fbref10_data)

fbref5_data = convert_to_dataframe(fbref5_data)
fbref6_data = convert_to_dataframe(fbref6_data)
fbref7_data = convert_to_dataframe(fbref7_data)
fbref8_data = convert_to_dataframe(fbref8_data)
fbref9_data = convert_to_dataframe(fbref9_data)
fbref10_data = convert_to_dataframe(fbref10_data)

fbref11_data = fbref11.read_team_season_stats(stat_type='shooting')
fbref12_data = fbref12.read_team_season_stats(stat_type='shooting')
fbref13_data = fbref13.read_team_season_stats(stat_type='shooting')
fbref14_data = fbref14.read_team_season_stats(stat_type='shooting')
fbref15_data = fbref15.read_team_season_stats(stat_type='shooting')
fbref16_data = fbref16.read_team_season_stats(stat_type='shooting')

fbref11_data = add_teams(fbref11_data)
fbref12_data = add_teams(fbref12_data)
fbref13_data = add_teams(fbref13_data)
fbref14_data = add_teams(fbref14_data)
fbref15_data = add_teams(fbref15_data)
fbref16_data = add_teams(fbref16_data)

fbref11_data = convert_to_dataframe(fbref11_data)
fbref12_data = convert_to_dataframe(fbref12_data)
fbref13_data = convert_to_dataframe(fbref13_data)
fbref14_data = convert_to_dataframe(fbref14_data)
fbref15_data = convert_to_dataframe(fbref15_data)
fbref16_data = convert_to_dataframe(fbref16_data)

fbref17_data = fbref17.read_team_season_stats(stat_type='passing')
fbref18_data = fbref18.read_team_season_stats(stat_type='passing')
fbref19_data = fbref19.read_team_season_stats(stat_type='passing')
fbref20_data = fbref20.read_team_season_stats(stat_type='passing')
fbref21_data = fbref21.read_team_season_stats(stat_type='passing')
fbref22_data = fbref22.read_team_season_stats(stat_type='passing')

fbref17_data = add_teams(fbref17_data)
fbref18_data = add_teams(fbref18_data)
fbref19_data = add_teams(fbref19_data)
fbref20_data = add_teams(fbref20_data)
fbref21_data = add_teams(fbref21_data)
fbref22_data = add_teams(fbref22_data)

fbref17_data = convert_to_dataframe(fbref17_data)
fbref18_data = convert_to_dataframe(fbref18_data)
fbref19_data = convert_to_dataframe(fbref19_data)
fbref20_data = convert_to_dataframe(fbref20_data)
fbref21_data = convert_to_dataframe(fbref21_data)
fbref22_data = convert_to_dataframe(fbref22_data)

fbref23_data = fbref23.read_team_season_stats(stat_type='defense')
fbref24_data = fbref24.read_team_season_stats(stat_type='defense')
fbref25_data = fbref25.read_team_season_stats(stat_type='defense')
fbref26_data = fbref26.read_team_season_stats(stat_type='defense')
fbref27_data = fbref27.read_team_season_stats(stat_type='defense')
fbref28_data = fbref28.read_team_season_stats(stat_type='defense')

fbref23_data = add_teams(fbref23_data)
fbref24_data = add_teams(fbref24_data)
fbref25_data = add_teams(fbref25_data)
fbref26_data = add_teams(fbref26_data)
fbref27_data = add_teams(fbref27_data)
fbref28_data = add_teams(fbref28_data)

fbref23_data = convert_to_dataframe(fbref23_data)
fbref24_data = convert_to_dataframe(fbref24_data)
fbref25_data = convert_to_dataframe(fbref25_data)
fbref26_data = convert_to_dataframe(fbref26_data)
fbref27_data = convert_to_dataframe(fbref27_data)
fbref28_data = convert_to_dataframe(fbref28_data)

fbref29_data = fbref29.read_team_season_stats(stat_type='misc')
fbref30_data = fbref30.read_team_season_stats(stat_type='misc')
fbref31_data = fbref31.read_team_season_stats(stat_type='misc')
fbref32_data = fbref32.read_team_season_stats(stat_type='misc')
fbref33_data = fbref33.read_team_season_stats(stat_type='misc')
fbref34_data = fbref34.read_team_season_stats(stat_type='misc')

fbref29_data = add_teams(fbref29_data)
fbref30_data = add_teams(fbref30_data)
fbref31_data = add_teams(fbref31_data)
fbref32_data = add_teams(fbref32_data)
fbref33_data = add_teams(fbref33_data)
fbref34_data = add_teams(fbref34_data)

fbref29_data = convert_to_dataframe(fbref29_data)
fbref30_data = convert_to_dataframe(fbref30_data)
fbref31_data = convert_to_dataframe(fbref31_data)
fbref32_data = convert_to_dataframe(fbref32_data)
fbref33_data = convert_to_dataframe(fbref33_data)
fbref34_data = convert_to_dataframe(fbref34_data)

with open('data\Team\#2023-2024\Standard'):
    fbref_data.to_csv()
with open('data\Team\#2022-2023\Standard'):
    fbref0_data.to_csv()
with open('data\Team\#2021-2022\Standard'):
    fbref1_data.to_csv()
with open('data\Team\#2020-2021\Standard'):
    fbref2_data.to_csv()
with open('data\Team\#2019-2020\Standard'):
    fbref3_data.to_csv()
with open('data\Team\#2018-2019\Standard'):
    fbref4_data.to_csv()
with open('data\Team\#2023-2024\Keeper'):
    fbref5_data.to_csv()
with open('data\Team\#2022-2023\Keeper'):
    fbref6_data.to_csv()
with open('data\Team\#2021-2022\Keeper'):
    fbref7_data.to_csv()
with open('data\Team\#2020-2021\Keeper'):
    fbref8_data.to_csv()
with open('data\Team\#2019-2020\Keeper'):
    fbref9_data.to_csv()
with open('data\Team\#2018-2019\Keeper'):
    fbref10_data.to_csv()
with open('data\Team\#2023-2024\Shooting'):
    fbref11_data.to_csv()
with open('data\Team\#2022-2023\Shooting'):
    fbref12_data.to_csv()
with open('data\Team\#2021-2022\Shooting'):
    fbref13_data.to_csv()
with open('data\Team\#2020-2021\Shooting'):
    fbref14_data.to_csv()
with open('data\Team\#2019-2020\Shooting'):
    fbref15_data.to_csv()
with open('data\Team\#2018-2019\Shooting'):
    fbref16_data.to_csv()
with open('data\Team\#2023-2024\Passing'):
    fbref17_data.to_csv()
with open('data\Team\#2022-2023\Passing'):
    fbref18_data.to_csv()
with open('data\Team\#2021-2022\Passing'):
    fbref19_data.to_csv()
with open('data\Team\#2020-2021\Passing'):
    fbref20_data.to_csv()
with open('data\Team\#2019-2020\Passing'):
    fbref21_data.to_csv()
with open('data\Team\#2018-2019\Passing'):
    fbref22_data.to_csv()
with open('data\Team\#2023-2024\Defense'):
    fbref23_data.to_csv()
with open('data\Team\#2022-2023\Defense'):
    fbref24_data.to_csv()
with open('data\Team\#2021-2022\Defense'):
    fbref25_data.to_csv()
with open('data\Team\#2020-2021\Defense'):
    fbref26_data.to_csv()
with open('data\Team\#2019-2020\Defense'):
    fbref27_data.to_csv()
with open('data\Team\#2018-2019\Defense'):
    fbref28_data.to_csv()
with open('data\Team\#2023-2024\Misc'):
    fbref29_data.to_csv()
with open('data\Team\#2022-2023\Misc'):
    fbref30_data.to_csv()
with open('data\Team\#2021-2022\Misc'):
    fbref31_data.to_csv()
with open('data\Team\#2020-2021\Misc'):
    fbref32_data.to_csv()
with open('data\Team\#2019-2020\Misc'):
    fbref33_data.to_csv()
with open('data\Team\#2018-2019\Misc'):
    fbref34_data.to_csv()'''