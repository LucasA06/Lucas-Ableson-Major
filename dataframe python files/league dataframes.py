import soccerdata as sd
import pandas as pd
import os

def create_directories():
    base_path = 'data/Leagues'
    leagues = ['GER-Bundesliga','ENG-Premier League','ESP-La Liga']
    seasons = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

    for league in leagues:
        for season in seasons:
            dir_path = os.path.join(base_path,league,season)
            os.makedirs(dir_path, exist_ok=True)

def fetch_and_process_data_teams(leagues, seasons):
    all_data = []

    for league in leagues:
        for season in seasons:
            try:
                fotmob = sd.FotMob(leagues=[league], seasons=[season])
                data = fotmob.read_league_table()

                if not data.empty:
                    all_data.append((league, season, data))

            except Exception as e:
                print(f"Error fetching data for {league} {season}: {e}")

    return all_data

def save_data_to_pickle(data):
    base_path = 'data/Leagues'
    for league, season, df in data:
        dir_path = os.path.join(base_path, league, season)
        file_path = os.path.join(dir_path, f'{league.replace(" ", "_")}.pkl')
        df.to_pickle(file_path)

if __name__ == "__main__":
    create_directories()

    leagues = ['GER-Bundesliga','ENG-Premier League','ESP-La Liga']
    seasons = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

    data = fetch_and_process_data_teams(leagues, seasons)
    save_data_to_pickle(data)
