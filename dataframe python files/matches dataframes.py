import soccerdata as sd
import pandas as pd
import os

def create_directories():
    base_path = 'data/Matches'
    leagues = ['ESP-La Liga','ENG-Premier League','GER-Bundesliga','ITA-Serie A','FRA-Ligue 1']
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
                mh = sd.Understat(leagues=[league],seasons=[season])
                data = mh.read_team_match_stats()

                # Columns to drop
                columns_to_drop = ['league_id', 'game_id','home_team_id','away_team_id','season_id','away_team_code','home_team_code','away_expected_points','away_np_xg'
                   ,'away_np_xg_difference','away_ppda','away_deep_completions','home_expected_points','home_np_xg'
                   ,'home_np_xg_difference','home_ppda','home_deep_completions']

                # Drop specified columns
                data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

                if not data.empty:
                    all_data.append((league, season, data))

            except Exception as e:
                print(f"Error fetching data for {league} {season}: {e}")

    return all_data


def save_data_to_pickle(data):
    base_path = 'data/Matches'
    for league, season, df in data:
        dir_path = os.path.join(base_path, league, season)
        file_path = os.path.join(dir_path, f'{league}.pkl')
        df.to_pickle(file_path)

if __name__ == "__main__":
    create_directories()

    leagues = ['ESP-La Liga','ENG-Premier League','GER-Bundesliga','ITA-Serie A','FRA-Ligue 1']
    seasons = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

    data = fetch_and_process_data_teams(leagues, seasons)
    save_data_to_pickle(data)