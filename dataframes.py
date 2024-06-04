import soccerdata as sd
import pandas as pd
import os
import time
import random

def create_directories():
    base_path = 'data/Team'
    leagues = ['ENG-Premier League', 'ESP-La Liga']
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']

    for league in leagues:
        for season in seasons:
            dir_path = os.path.join(base_path, league, season)
            os.makedirs(dir_path, exist_ok=True)

def fetch_and_process_data(leagues, seasons, stat_type):
    all_data = []

    for league in leagues:
        for season in seasons:
            try:
                fbref = sd.FBref(leagues=[league], seasons=[season])
                data = fbref.read_team_season_stats(stat_type=stat_type.lower())

                # Columns to drop
                columns_to_drop = ['Per 90 Minutes', 'Progression', 'url', 'Playing Time']

                # Drop specified columns
                data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

                # Insert team names (adjusted for league, defaulting to ENG-Premier League teams for simplicity)
                if league == 'ENG-Premier League':
                    teams = [
                        'Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
                        'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United',
                        'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
                        'Newcastle Utd', "Nott'ham Forest", 'Southampton', 'Tottenham',
                        'West Ham', 'Wolves'
                    ]
                elif league == 'ESP-La Liga':
                    teams = [
                        'Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                        'Celta Vigo', 'Elche', 'Espanyol', 'Getafe', 'Granada', 'Levante',
                        'Mallorca', 'Osasuna', 'Rayo Vallecano', 'Real Betis', 'Real Madrid',
                        'Real Sociedad', 'Sevilla', 'Valencia', 'Villarreal'
                    ]

                data.insert(0, 'Team', teams)
                all_data.append((league, season, pd.DataFrame(data)))

                # Add a delay to prevent hitting rate limits
                time.sleep(random.uniform(1, 3))

            except Exception as e:
                print(f"Error fetching data for {league} {season} {stat_type}: {e}")

    return all_data

def save_data_to_pickle(data, stat_type):
    base_path = 'data/Team'
    for league, season, df in data:
        dir_path = os.path.join(base_path, league, season)
        file_path = os.path.join(dir_path, f'{stat_type.lower()}.pkl')
        df.to_pickle(file_path)

if __name__ == "__main__":
    create_directories()

    leagues = ['ENG-Premier League', 'ESP-La Liga']
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_types = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    for stat_type in stat_types:
        data = fetch_and_process_data(leagues, seasons, stat_type)
        save_data_to_pickle(data, stat_type)
