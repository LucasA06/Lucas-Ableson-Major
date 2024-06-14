<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./documentation_images/icon.png">
    <img src="./documentation_images/icon.png">
  </picture>
</p>

# Football Database App
*By Lucas Ableson*
## Project Description
The Football Database App is a dynamic application designed to provide comprehensive statistics and insights into football leagues, teams, and players. The app leverages a robust database to offer users a detailed overview of matches, player performance, team standings, and more. Users can easily query the database to retrieve specific information, making it an essential tool for football enthusiasts, analysts, and statisticians.

## How to Install and Run the Project
Prerequisites
* Ensure you have Python installed (version 3.7 or higher recommended).
* Install the required dependencies listed in requirements.txt.

### Installation Steps
Clone the Repository:

```bash
git clone https://github.com/LucasA06/Lucas-Ableson-Major.git
```

Install Dependencies:

```bash
pip install -r requirements.txt
```
Setup the Database:

Ensure your database server is running.
Update the database configuration in config.py with your database credentials.
Run the database migration script to set up the necessary tables.
```bash
python manage.py migrate
```
Run the Application:

bash
Copy code
python manage.py runserver
### Important Note:
To ensure the application displays correctly, set your computer's display scale to 100%. On Windows, you can do this by navigating to Settings > System > Display and adjusting the scale and layout settings to 100%. On macOS, go to System Preferences > Displays and select Default for display.

## How to Use the Project
Accessing the App:

1. Open your web browser.
Navigate to http://127.0.0.1:8000 to access the Football Database App interface.
Navigating the Interface:

2. Home Page: Provides an overview of the latest matches and updates.
Teams: Browse through a list of football teams, view team details, and standings.
Players: Search for players, view player statistics, and performance metrics.
Matches: Explore match schedules, results, and detailed match reports.
Statistics: Access comprehensive statistics and analytics for teams and players.
Querying the Database:

3. Use the search bar and filters to query the database for specific information.
Generate custom reports and visualizations based on the data available.
User Settings:

4. Customize your profile and preferences through the user settings page.
Manage notifications and alerts for your favorite teams and players.
The Football Database App is designed to be intuitive and user-friendly, making it easy for anyone to delve into the rich world of football data. Enjoy exploring and analyzing the beautiful game with our app!