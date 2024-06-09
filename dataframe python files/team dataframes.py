import soccerdata as sd
import pandas as pd
import os

def create_directories():
    base_path = 'data/Team'
    leagues = ['GER-Bundesliga']
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']

    for league in leagues:
        for season in seasons:
            dir_path = os.path.join(base_path, league, season)
            os.makedirs(dir_path, exist_ok=True)

def get_teams(league, season):
    teams_mapping = {
        "ENG-Premier League": {
            '23-24': ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
                      'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United',
                      'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
                      'Newcastle Utd', "Nottingham Forest", 'Southampton', 'Tottenham',
                      'West Ham', 'Wolves'],
            '22-23': ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton',
                      'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United',
                      'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
                      'Newcastle Utd', "Nottingham Forest", 'Southampton', 'Tottenham',
                      'West Ham', 'Wolves'],
            '21-22': ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton', 'Burnley',
                      'Chelsea', 'Crystal Palace', 'Everton', 'Leeds United', 'Leicester City',
                      'Liverpool', 'Manchester City', 'Manchester Utd', 'Newcastle Utd',
                      'Norwich City', 'Southampton', 'Tottenham', 'Watford', 'West Ham', 'Wolves'],
            '20-21': ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea',
                      'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 'Leicester City',
                      'Liverpool', 'Manchester City', 'Manchester Utd', 'Newcastle Utd',
                      'Sheffield Utd', 'Southampton', 'Tottenham', 'West Brom', 'West Ham', 'Wolves'],
            '19-20': ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brighton', 'Burnley',
                      'Chelsea', 'Crystal Palace', 'Everton', 'Leicester City', 'Liverpool',
                      'Manchester City', 'Manchester Utd', 'Newcastle Utd', 'Norwich City',
                      'Sheffield Utd', 'Southampton', 'Tottenham', 'Watford', 'West Ham', 'Wolves'],
            '18-19': ['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Cardiff City',
                      'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield',
                      'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd',
                      'Newcastle Utd', 'Southampton', 'Tottenham', 'Watford', 'West Ham', 'Wolves']
        },
        "ESP-La Liga": {
            '23-24': ['Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                      'Celta Vigo', 'Elche', 'Espanyol', 'Getafe', 'Granada', 'Levante',
                      'Mallorca', 'Osasuna', 'Rayo Vallecano', 'Real Betis', 'Real Madrid',
                      'Real Sociedad', 'Sevilla', 'Valencia', 'Villarreal'],
            '22-23': ['Almería', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                      'Celta Vigo', 'Elche', 'Espanyol', 'Getafe', 'Girona', 'Mallorca',
                      'Osasuna', 'Rayo Vallecano', 'Real Betis', 'Real Madrid', 'Real Sociedad',
                      'Sevilla', 'Valencia', 'Valladolid', 'Villarreal'],
            '21-22': ['Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                      'Celta Vigo', 'Elche', 'Espanyol', 'Getafe', 'Granada', 'Levante',
                      'Mallorca', 'Osasuna', 'Rayo Vallecano', 'Real Betis', 'Real Madrid',
                      'Real Sociedad', 'Sevilla', 'Valencia', 'Villarreal'],
            '20-21': ['Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                      'Celta Vigo', 'Eibar', 'Elche', 'Getafe', 'Granada', 'Huesca',
                      'Levante', 'Osasuna', 'Real Betis', 'Real Madrid', 'Real Sociedad',
                      'Sevilla', 'Valencia', 'Valladolid', 'Villarreal'],
            '19-20': ['Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Cádiz',
                      'Celta Vigo', 'Eibar', 'Espanyol', 'Getafe', 'Granada', 'Leganés',
                      'Levante', 'Mallorca', 'Osasuna', 'Real Betis', 'Real Madrid', 'Real Sociedad',
                      'Sevilla', 'Valencia', 'Villarreal'],
            '18-19': ['Alavés', 'Athletic Club', 'Atlético Madrid', 'Barcelona', 'Celta Vigo',
                      'Eibar', 'Espanyol', 'Getafe', 'Girona', 'Huesca', 'Leganés',
                      'Levante', 'Rayo Vallecano', 'Real Betis', 'Real Madrid', 'Real Sociedad',
                      'Sevilla', 'Valencia', 'Valladolid', 'Villarreal']
        },
        "ITA-Serie A": {
            '23-24': ['Atalanta', 'Bologna', 'Cagliari', 'Empoli', 'Fiorentina', 'Frosinone',
                      'Genoa', 'Inter Milan', 'Juventus', 'Lazio', 'Lecce', 'AC Milan',
                      'Monza', 'Napoli', 'Roma', 'Salernitana', 'Sassuolo', 'Torino',
                      'Udinese', 'Verona'],
            '22-23': ['Atalanta', 'Bologna', 'Cremonese', 'Empoli', 'Fiorentina', 'Inter Milan',
                      'Juventus', 'Lazio', 'Lecce', 'AC Milan', 'Monza', 'Napoli',
                      'Roma', 'Salernitana', 'Sampdoria', 'Sassuolo', 'Spezia', 'Torino',
                      'Udinese', 'Verona'],
            '21-22': ['Atalanta', 'Bologna', 'Cagliari', 'Empoli', 'Fiorentina', 'Genoa',
                      'Inter Milan', 'Juventus', 'Lazio', 'AC Milan', 'Napoli', 'Roma',
                      'Salernitana', 'Sampdoria', 'Sassuolo', 'Spezia', 'Torino', 'Udinese',
                      'Venezia', 'Verona'],
            '20-21': ['Atalanta', 'Benevento', 'Bologna', 'Cagliari', 'Crotone', 'Fiorentina',
                      'Genoa', 'Inter Milan', 'Juventus', 'Lazio', 'AC Milan', 'Napoli',
                      'Parma', 'Roma', 'Sampdoria', 'Sassuolo', 'Spezia', 'Torino',
                      'Udinese', 'Verona'],
            '19-20': ['Atalanta', 'Bologna', 'Brescia', 'Cagliari', 'Fiorentina', 'Genoa',
                      'Inter Milan', 'Juventus', 'Lazio', 'AC Milan', 'Napoli', 'Parma',
                      'Roma', 'Sampdoria', 'Sassuolo', 'SPAL', 'Torino', 'Udinese',
                      'Verona', 'Lecce'],
            '18-19': ['Atalanta', 'Bologna', 'Cagliari', 'Chievo Verona', 'Empoli', 'Fiorentina',
                      'Frosinone', 'Genoa', 'Inter Milan', 'Juventus', 'Lazio', 'AC Milan',
                      'Napoli', 'Parma', 'Roma', 'Sampdoria', 'Sassuolo', 'SPAL',
                      'Torino', 'Udinese']
        },
        "FRA-Ligue 1": {
            "23-24": ['Brest', 'Clermont Foot', 'Le Havre', 'Lens', 'Lille',
                    'Lorient', 'Lyon', 'Marseille', 'Metz', 'Monaco',
                    'Montpellier', 'Nantes', 'Nice', 'Paris S-G', 'Reims',
                    'Rennes', 'Strasbourg', 'Toulouse'],
            "22-23": ['Ajaccio', 'Angers', 'Auxerre', 'Brest', 'Clermont Foot',
                    'Lens', 'Lille', 'Lorient', 'Lyon', 'Marseille',
                    'Monaco', 'Montpellier', 'Nantes', 'Nice', 'ParisSG',
                    'Reims', 'Rennes', 'Strasbourg', 'Toulouse', 'Troyes'],
            "21-22": ['Angers', 'Bordeaux', 'Brest', 'Clermont Foot', 'Lens',
                    'Lille', 'Lorient', 'Lyon', 'Marseille', 'Metz',
                    'Monaco', 'Montpellier', 'Nantes', 'Nice', 'ParisSG',
                    'Reims', 'Rennes','Saint-Étienne', 'Strasbourg', 'Troyes'],
            "20-21": ['Angers', 'Bordeaux', 'Brest', 'Dijon', 'Lens',
                    'Lille', 'Lorient', 'Lyon', 'Marseille', 'Metz',
                    'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Nîmes',
                    'ParisSG', 'Reims', 'Rennes','Saint-Étienne', 'Strasbourg'],
            "19-20": ['Amiens', 'Angers', 'Bordeaux', 'Brest', 'Dijon',
                    'Lille', 'Lyon', 'Marseille', 'Metz',
                    'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Nîmes',
                    'ParisSG', 'Reims', 'Rennes','Saint-Étienne','Strasbourg','Toulouse'],
            "18-19": ['Amiens', 'Angers', 'Bordeaux', 'Caen', 'Dijon',
                    'Guingamp', 'Lille', 'Lyon', 'Marseille', 'Monaco',
                    'Montpellier', 'Nantes', 'Nice', 'Nîmes', 'ParisSG',
                    'Reims', 'Rennes', 'St Etienne', 'Strasbourg','Toulouse']
        },
        "GER-Bundesliga": {
            "23-24": [
'Augsburg', 'Bayern Munich', 'Bochum', 'Darmstadt 98', 'Dortmund', 
                    'Eintracht Frankfurt', 'Freiburg', 'Gladbach', 'Heidenheim', 'Hoffenheim', 
                    'Köln', 'Leverkusen', 'Mainz 05', 'RB Leipzig', 'Stuttgart', 
                    'Union Berlin', 'Werder Bremen', 'Wolfsburg'],
            "22-23": ['Augsburg', 'Bayern Munich', 'Bochum', 'Dortmund', 'Eintracht Frankfurt', 
                    'Freiburg', 'Gladbach', 'Hertha BSC', 'Hoffenheim', 'Köln', 
                    'Leverkusen', 'Mainz 05', 'RB Leipzig', 'Schalke 04', 'Stuttgart', 
                    'Union Berlin', 'Werder Bremen', 'Wolfsburg'],
            "21-22": ['Arminia', 'Augsburg', 'Bayern Munich', 'Bochum', 'Dortmund', 
                    'Eintracht Frankfurt', 'Freiburg', 'Gladbach', 'Greuther Fürth', 'Hertha BSC', 
                    'Hoffenheim', 'Köln', 'Leverkusen', 'Mainz 05', 'RB Leipzig', 
                    'Stuttgart', 'Union Berlin', 'Wolfsburg'],
            "20-21": ['Arminia', 'Augsburg', 'Bayern Munich', 'Dortmund', 'Eintracht Frankfurt', 
                    'Freiburg', 'Gladbach', 'Hertha BSC', 'Hoffenheim', 'Köln', 
                    'Leverkusen', 'Mainz 05', 'RB Leipzig', 'Schalke 04', 'Stuttgart', 
                    'Union Berlin', 'Werder Bremen', 'Wolfsburg'],
            "19-20": ['Augsburg', 'Bayern Munich', 'Dortmund', 'Düsseldorf', 'Eintracht Frankfurt', 
                    'Freiburg', 'Gladbach', 'Hertha BSC', 'Hoffenheim', 'Köln', 
                    'Leverkusen', 'Mainz 05', 'Paderborn 07', 'RB Leipzig', 'Schalke 04', 
                    'Union Berlin', 'Werder Bremen', 'Wolfsburg'],
            "18-19": ['Augsburg', 'Bayern Munich', 'Dortmund', 'Düsseldorf', 'Eintracht Frankfurt', 
                    'Freiburg', 'Gladbach', 'Hannover 96', 'Hertha BSC', 'Hoffenheim', 
                    'Leverkusen', 'Mainz 05', 'Nürnberg', 'RB Leipzig', 'Schalke 04', 
                    'Stuttgart', 'Werder Bremen', 'Wolfsburg']
        }
    }
    
    return teams_mapping.get(league, {}).get(season, [])

def fetch_and_process_data_teams(leagues, seasons, stat_type):
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

                # Insert team names based on the league and season
                teams = get_teams(league, season)
                if teams:
                    data.insert(0, 'Team', teams)
                    all_data.append((league, season, pd.DataFrame(data)))
                else:
                    print(f"Teams not found for {league} {season}")

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

    leagues = ["GER-Bundesliga"]
    seasons = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_types = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    for stat_type in stat_types:
        data = fetch_and_process_data_teams(leagues, seasons, stat_type)
        save_data_to_pickle(data, stat_type)
