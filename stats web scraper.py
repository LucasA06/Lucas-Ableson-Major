import requests
from bs4 import BeautifulSoup
import pandas as pd

import requests

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.transfermarkt.com/fc-chelsea/startseite/verein/631/saison_id/2023"
pageTree = requests.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

Players = pageSoup.find_all("a", {"class": "sort-link"})

Players[0].text

PlayersList = []


for i in range(0,3):
    PlayersList.append(Players[i].text)
    
df = pd.DataFrame({"Players":PlayersList})