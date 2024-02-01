import pandas as pd
url = 'https://xvalue.ai/stats/en/league/premier_league/players/stat/Goals?season=2022'
all_tables = pd.read_html(url)

all_tables[0]
all_tables[1]

table = all_tables[0]
table.to_csv(r'C:\Users\lucas\OneDrive\Documents\GitHub\Lucas-Repository\Scraped .csv files\22\Players\PL Player Goals.csv')
#print(len(all_tables))