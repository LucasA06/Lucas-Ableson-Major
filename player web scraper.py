import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    all_tables = soup.find('table',{'class': 'stats_table''le2'})

    if all_tables:
        # Create a CSV file to store the data
        with open(r'C:\Users\lucas\OneDrive\Documents\GitHub\Lucas-Repository\Scraped .csv files\Pl Player Standard Stats.csv', 'w', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # Extract table headers
            headers = [header.text.strip() for header in all_tables.findAll('th')]
            csv_writer.writerow(headers)

            # Iterate through the rows of the table (skip the header row)
            for row in all_tables.find_all('tr')[1:]:
                # Extract data from each cell in the row
                cells = row.find_all('td')
                if len(cells) > 0:
                    player_stats = [cell.text.strip() for cell in cells]
                    csv_writer.writerow(player_stats)

        print("Data has been saved to 'player_stats.csv'.")
    else:
        print("No data found.")