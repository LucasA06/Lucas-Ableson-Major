from tkinter import ttk
import customtkinter as ctk
import pandas as pd
from PIL import ImageTk, Image
import os
import random
import tkinter as tk
import sys
import plotly.graph_objects as go

def agree_clicked():
    with open('agreement_status', 'w') as f:
        f.write('agreed')
    root.destroy()

def disagree_clicked():
    root.destroy()
    sys.exit()

# Check if the user has already agreed
try:
    with open('agreement_status', 'r') as f:
        agreement_status = f.read().strip()
except FileNotFoundError:
    agreement_status = ''

if agreement_status == 'agreed':
    pass
else:
    root = ctk.CTk()
    root.title("Terms and Conditions")
    root.geometry('500x600')
    root.resizable(False, False)
    root.configure(bg='white')

    def disable_event():
        pass
    root.protocol("WM_DELETE_WINDOW", disable_event)

    terms_label = ctk.CTkTextbox(root, font=('Gill Sans MT', 15), width=490, height=500)
    terms_label.pack(padx=10, pady=10)
    with open('Term and Service') as file:
        data = file.read()
    terms_label.insert('1.0', data)
    terms_label.configure(state='disabled')

    label = ctk.CTkLabel(root, font=('Gill Sans MT', 15), text='Do you agree to the Terms and Conditions?')
    label.place(relx=0.25, rely=0.865)

    agree_button = ctk.CTkButton(root, text="Agree", command=agree_clicked)
    agree_button.place(relx=0.1, rely=0.925)

    disagree_button = ctk.CTkButton(root, text="Disagree", command=disagree_clicked)
    disagree_button.place(relx=0.65, rely=0.925)

    root.mainloop()

app = ctk.CTk()
app.geometry("675x700")
app.title("Football Database App")
app.resizable(False, False)

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')
current_theme = 'Light'

# All the code used to open the different pages
def open_league_tables():
    app.withdraw()
    create_league_tables()

def open_teams():
    app.withdraw()
    create_teams()

def open_players():
    app.withdraw()
    create_players()

def open_about():
    app.withdraw()
    create_about()

def open_settings():
    app.withdraw()
    create_settings()

def open_matches():
    app.withdraw()
    create_matches()

# All the code used to create the home gui page
def create_home():
    # Creates a grid to easily place the buttons in the sidebar frame
    sidebar = ctk.CTkFrame(master=app,width=1,height=700,corner_radius=0)
    sidebar.grid()
    sidebar_button1 = ctk.CTkButton(sidebar,width=100,text='Matches',command=open_matches, font=('Gill Sans MT', 15))
    sidebar_button1.grid(row=1, column=0,padx=5,pady=5)
    sidebar_button2 = ctk.CTkButton(sidebar,width=100,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    sidebar_button2.grid(row=2, column=0,padx=5,pady=5)
    sidebar_button3 = ctk.CTkButton(sidebar,width=100,text='Players',command=open_players, font=('Gill Sans MT', 15))
    sidebar_button3.grid(row=3, column=0,padx=5,pady=5)
    sidebar_button4 = ctk.CTkButton(sidebar,width=100,text='League Tables',command=open_league_tables, font=('Gill Sans MT', 15))
    sidebar_button4.grid(row=4, column=0,padx=5,pady=5)
    sidebar_button11 = ctk.CTkButton(sidebar,width=100,text='',fg_color='',hover=False)
    sidebar_button11.grid(row=6, column=0,padx=5,pady=205)
    sidebar_button9 = ctk.CTkButton(sidebar,width=100,text='About',command=open_about, font=('Gill Sans MT', 15))
    sidebar_button9.grid(row=7, column=0,padx=5,pady=5)
    sidebar_button10 = ctk.CTkButton(sidebar,width=100,text='Settings',command=open_settings, font=('Gill Sans MT', 15))
    sidebar_button10.grid(row=8, column=0,padx=5,pady=5)
    exit_button = ctk.CTkButton(sidebar,width=100,text='Exit',command=app.withdraw, fg_color='red', font=('Gill Sans MT', 15))
    exit_button.grid(row=9, column=0,padx=5,pady=5)

    # Create the buttons for the home screen
    button1 = ctk.CTkButton(master=app, text="League Tables", command=open_league_tables, font=('Gill Sans MT', 15))
    button1.place(relx=0.2, rely=0.1)
    button2 = ctk.CTkButton(master=app,text='Players',command=open_players, font=('Gill Sans MT', 15))
    button2.place(relx=0.475,rely=0.1)
    button3 = ctk.CTkButton(master=app,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    button3.place(relx=0.75,rely=0.1)
    entry = ctk.CTkEntry(master=app, placeholder_text='Search', width=525, font=('Gill Sans MT', 15))
    entry.place(relx=0.2,rely=0.025)

    def display_code(event=None):
        if entry.get().lower() == 'Eggy':
            win = ctk.CTk()
            win.title("Skills Chart")
            win.geometry("700x450")
            win.resizable(False, False)

            def create_radar_chart(player_name, data_values, title):
                fig = go.Figure(data=go.Scatterpolar(
                    r=data_values,
                    theta=['Shooting', 'Dribbling', 'Passing', 'Defending', 'Height', 'Agility', 'Finishing', 'Strength', 'Stamina', 'Rebounding', 'Vertical'],
                    fill='toself'
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            range=[0, 10],
                        ),
                    ),
                    showlegend=False
                )
                
                return fig

            Finn = create_radar_chart('Finn', [6, 6, 4, 7, 2, 3, 5, 7, 4, 3, 3], 'Finn')
            fig1 = create_radar_chart('Andrew', [5,6,2,2,1,5,3,1,6,1,2], 'Andrew')
            fig2 = create_radar_chart('Noah', [8,9,8,8,9,9,10,7,9,9,10], 'Noah')
            fig3 = create_radar_chart('Lucca', [9,10,7,9,9,9,9,10,8,9,9], 'Lucca')
            fig4 = create_radar_chart('Talon', [10,8,9,8,9,8,10,9,8,8,7], 'Talon')
            fig5 = create_radar_chart('Will', [7,6,8,7,9,7,8,6,6,8,6], 'Will')
            fig6 = create_radar_chart('Lucas', [7,4,8,8,8,9,6,7,8,8,6], 'Lucas')
            fig7 = create_radar_chart('Daniel', [8,7,6,6,5,6,7,6,6,5,7], 'Daniel')
            fig8 = create_radar_chart('Zac', [6,5,4,8,6,6,8,10,7,7,4], 'Zac')
            fig9 = create_radar_chart('Bowie', [4,6,6,4,3,8,2,4,9,4,3], 'Bowie')
            fig10 = create_radar_chart('Henri', [4,6,3,5,3,8,4,6,10,4,3], 'Henri')
            fig11 = create_radar_chart('Fraser', [2,3,5,4,5,6,4,6,7,6,3], 'Fraser')
            fig12 = create_radar_chart('Jacko', [8,7,4,6,9,6,8,6,6,7,4], 'Jacko')
            fig13 = create_radar_chart('Tom', [7,4,9,7,8,6,7,5,7,8,4], 'Tom')
            fig14 = create_radar_chart('Kohi', [5,4,4,3,6,5,4,8,6,6,4], 'Kohi')
            fig15 = create_radar_chart('Leo', [4,6,5,6,6,5,6,5,7,9,5], 'Leo')
            fig16 = create_radar_chart('Riley', [3,2,4,4,10,3,4,2,3,5,4], 'Riley')
            fig17 = create_radar_chart('CJ', [3,2,6,9,9,8,4,9,8,6,5], 'CJ')

            def open_Finn():
                Finn.show()

            def open_Andrew():
                fig1.show()

            def open_Noah():
                fig2.show()

            def open_Lucca():
                fig3.show()

            def open_Talon():
                fig4.show()

            def open_Will():
                fig5.show()

            def open_Lucas():
                fig6.show()

            def open_Daniel():
                fig7.show()

            def open_Zac():
                fig8.show()

            def open_Bowie():
                fig9.show()

            def open_Henri():
                fig10.show()

            def open_Fraser():
                fig11.show()

            def open_Jacko():
                fig12.show()

            def open_Tom():
                fig13.show()

            def open_Kohi():
                fig14.show()

            def open_Leo():
                fig15.show()

            def open_Riley():
                fig16.show()

            def open_Chris():
                fig17.show()

            def create_button(win, command, text, x, y):
                button = ctk.CTkButton(win, command=command, text=text, width=75)
                button.place(x=x, y=y)

            create_button(win, open_Finn, "Finn", 50, 100)
            create_button(win, open_Andrew, "Andrew", 250, 100)
            create_button(win, open_Noah, "Noah", 350, 100)
            create_button(win, open_Lucca, "Lucca", 450, 100)
            create_button(win, open_Talon, "Talon", 550, 100)
            create_button(win, open_Will, "Will", 50, 300)
            create_button(win, open_Lucas, "Lucas", 50, 200)
            create_button(win, open_Daniel, "Daniel", 150, 200)
            create_button(win, open_Zac, "Zac", 250, 200)
            create_button(win, open_Bowie, "Bowie", 350, 200)
            create_button(win, open_Henri, "Henri", 450, 200)
            create_button(win, open_Fraser, "Fraser", 550, 200)
            create_button(win, open_Jacko, "Jacko", 150, 300)
            create_button(win, open_Tom, "Tom", 250, 300)
            create_button(win, open_Kohi, "Khoi", 350, 300)
            create_button(win, open_Leo, "Leo", 450, 300)
            create_button(win, open_Riley, "Riley", 550, 300)
            create_button(win, open_Chris, "CJ", 150, 100)

            exit_b = ctk.CTkButton(win, command=win.destroy, text="Exit", width=75,fg_color='red')
            exit_b.place(x=300, y=400)

            win.mainloop()
    entry.bind('<Return>',display_code)

    # Titles the league, team and player cards
    league_text = ctk.CTkLabel(master=app,text='League Ladder',font=('Gill Sans MT', 22))
    league_text.place(relx=0.375,rely=0.21, anchor='w')
    player_text = ctk.CTkLabel(master=app,text='Player Card',font=('Gill Sans MT', 22))
    player_text.place(x=175,rely=0.59)
    team_text = ctk.CTkLabel(master=app,text='Team Card',font=('Gill Sans MT', 22))
    team_text.place(x=450,rely=0.59)

    # Set the width and height of the home screen pictures
    league_width = 525
    league_height = int(league_width * 265/700)
    player_width = 250
    player_height = int(player_width * 200/300)
    team_width = 275
    team_height = int(team_width * 200/350)

    # Get the pictures from their respective directories and randomly select one to present
    picture_dir1 = r'Ladder Pictures'
    picture_files = [f for f in os.listdir(picture_dir1)]
    pic_dir2 = r'Player Pictures'
    pic_files2 = [f for f in os.listdir(pic_dir2)]
    pic_dir3 = r'Team Pictures'
    pic_files3 = [f for f in os.listdir(pic_dir3)]
    random_pic1 = random.choice(picture_files)
    random_pic2 = random.choice(pic_files2)
    random_pic3 = random.choice(pic_files3)
    picture_path = os.path.join(picture_dir1, random_pic1)
    picture_path2 = os.path.join(pic_dir2, random_pic2)
    picture_path3 = os.path.join(pic_dir3, random_pic3)

    league_mapping = {
    'Bundesliga.png': 'GER-Bundesliga',
    'La Liga.png': 'ESP-La Liga',
    'Serie A.png': 'ITA-Serie A',
    'Premier League.png': 'ENG-Premier League',
    'Ligue 1.png': 'FRA-Ligue 1'
}
    
    player_league_mapping = {
    'Alexandre Lacazette.png': 'FRA-Ligue 1',
    'Cole Palmer.png': 'ENG-Premier League',
    'Dusan Vlahovic.png': 'ITA-Serie A',
    'Erling Haaland.png': 'ENG-Premier League',
    'Harry Kane.png': 'GER-Bundesliga',
    'Jude Bellingham.PNG':'ESP-La Liga',
    'Kylian Mbappé.png':'FRA-Ligue 1',
    'Lautaro Martínez.png':'ITA-Serie A',
    'Loïs Openda.png':'GER-Bundesliga',
    'Robert Lewandowski.PNG':'ESP-La Liga'
    }

    team_mapping = {
    'Arsenal.png': 'ENG-Premier League',
    'AS Monaco.png': 'FRA-Ligue 1',
    'Bayer 04 Leverkusen.png': 'GER-Bundesliga',
    'FC Bayern Munchen.png': 'GER-Bundesliga',
    'Manchester City.png': 'ENG-Premier League',
    'PSG.png': 'FRA-Ligue 1'
}
    
    # Opens the pictures, resizes them and displays them in the home screen
    league_image = Image.open(picture_path)
    new_photo1 = league_image.resize((league_width, league_height))
    league_photo = ImageTk.PhotoImage(new_photo1)
    league_image_label = ctk.CTkLabel(app, image=league_photo, text='')
    league_image_label.place(relx=0.575, rely=0.4, anchor='center')
    league_image_label.image= league_photo
    league_image_label.bind("<Button-1>", lambda e:(app.withdraw(),create_league_tables(league_mapping.get(random_pic1, 'ENG-Premier League'))))

    player_image = Image.open(picture_path2)
    new_photo2 = player_image.resize((player_width, player_height))
    player_photo = ImageTk.PhotoImage(new_photo2)
    player_image_label = ctk.CTkLabel(app, image=player_photo, text='')
    player_image_label.place(relx=0.375, rely=0.825, anchor='center')
    player_image_label.image = player_photo
    player_image_label.bind("<Button-1>", lambda e:(app.withdraw(),create_players(player_league_mapping.get(random_pic2, 'ENG-Premier League'), os.path.splitext(random_pic2)[0])))

    team_image = Image.open(picture_path3)
    new_photo3 = team_image.resize((team_width, team_height))
    team_photo = ImageTk.PhotoImage(new_photo3)
    team_image_label = ctk.CTkLabel(app, image=team_photo, text='')
    team_image_label.place(relx=0.785, rely=0.825, anchor='center')
    team_image_label.image = team_photo
    team_image_label.bind("<Button-1>", lambda e:(app.withdraw(),create_teams(team_mapping.get(random_pic3, 'ENG-Premier League'))))

    # Configures the card titles so that they are displaying the team, league and player names
    league_text.configure(text=f'League Ladder - {os.path.splitext(os.path.basename(random_pic1))[0]}')
    player_text.configure(text=f'Player Card \n {os.path.splitext(os.path.basename(random_pic2))[0]}')
    team_text.configure(text=f'Team Card \n {os.path.splitext(os.path.basename(random_pic3))[0]}')

create_home()

def treeview_sort_column(tree, col, reverse):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse)
    
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)
    
    tree.heading(col, command=lambda _col=col: treeview_sort_column(tree, _col, not reverse))

def load_data_teams(tree, league, season, stat_type, search_term_team=''):
    file_path = f'data/Team/{league}/{season}/{stat_type}.pkl'
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        if search_term_team:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term_team, case=False).any(), axis=1)]

        # Set new columns
        tree["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree["columns"]:
            tree.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree.heading(column, text=column, command=lambda _col=column: treeview_sort_column(tree, _col, False))
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def on_option_change_team(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team):
    league = league_option_menu_team.get()
    season = season_option_menu_team.get()
    stat_type = stat_type_option_menu_team.get()
    load_data_teams(tree, league, season, stat_type, search_entry_team.get())

def filter_data_teams(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team):
    on_option_change_team(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team)

def create_teams(league='ENG-Premier League'):
    tl3 = ctk.CTk()
    tl3.geometry("900x700")
    tl3.resizable(True, False)
    tl3.title("Teams")

    title = ctk.CTkLabel(tl3, text='Team Statistics', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.025, anchor='center')

    frame = ctk.CTkScrollableFrame(tl3, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree = ttk.Treeview(frame, style='Treeview')
    tree.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl3, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.25, rely=0.085, anchor='center')
    season_label = ctk.CTkLabel(tl3, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.5, rely=0.085, anchor='center')
    stat_type_label = ctk.CTkLabel(tl3, text='Stat Type', font=('Gill Sans MT', 25))
    stat_type_label.place(relx=0.75, rely=0.085, anchor='center')

    league_options = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_type_options = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    league_option_menu_team = ctk.CTkOptionMenu(tl3, width=150, height=50, values=league_options, font=('Gill Sans MT', 15))
    league_option_menu_team.place(relx=0.25, rely=0.15, anchor='center')
    league_option_menu_team.set(league)
    season_option_menu_team = ctk.CTkOptionMenu(tl3, width=150, height=50, values=season_options, font=('Gill Sans MT', 15))
    season_option_menu_team.place(relx=0.5, rely=0.15, anchor='center')
    stat_type_option_menu_team = ctk.CTkOptionMenu(tl3, width=150, height=50, values=stat_type_options, font=('Gill Sans MT', 15))
    stat_type_option_menu_team.place(relx=0.75, rely=0.15, anchor='center')

    search_entry_team = ctk.CTkEntry(tl3, placeholder_text='Search', width=400, font=('Gill Sans MT', 15))
    search_entry_team .place(relx=0.5, rely=0.225, anchor='center')
    search_entry_team .bind('<KeyRelease>', lambda event: filter_data_teams(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team))

    # Set the command to update the table based on the dropdown selections
    league_option_menu_team.configure(command=lambda _: on_option_change_team(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team))
    season_option_menu_team.configure(command=lambda _: on_option_change_team(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team))
    stat_type_option_menu_team.configure(command=lambda _: on_option_change_team(tree, league_option_menu_team, season_option_menu_team, stat_type_option_menu_team, search_entry_team))

    menu_button = ctk.CTkButton(master=tl3, text='Menu', width=100, command=lambda: main_menu(tl3), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_teams(tree, league, '23-24', 'standard')

    tl3.mainloop()

def on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players):
    league = league_option_menu_players.get()
    season = season_option_menu_players.get()
    stat_type = stat_type_option_menu_players.get()
    load_data_players(tree, league, season, stat_type, search_entry_players.get())

def load_data_players(tree, league, season, stat_type, search_term_players=''):
    file_path = f'data/Players/{league}/{season}/{stat_type}.pkl'
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        # Filter the dataframe based on the search term
        if search_term_players:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term_players, case=False).any(), axis=1)]
        
        # Set new columns
        tree["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree["columns"]:
            tree.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree.heading(column, text=column, command=lambda _col=column: treeview_sort_column(tree, _col, False))
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def filter_data_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players):
    on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players)

def create_players(league='ENG-Premier League', player_name=''):
    tl1 = ctk.CTk()
    tl1.geometry("900x700")
    tl1.title("Players")
    tl1.resizable(False,False)

    title = ctk.CTkLabel(tl1, text='Player Statistics', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.025, anchor='center')

    frame = ctk.CTkScrollableFrame(tl1, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree = ttk.Treeview(frame, style='Treeview')
    tree.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl1, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.25, rely=0.085, anchor='center')
    season_label = ctk.CTkLabel(tl1, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.5, rely=0.085, anchor='center')
    stat_type_label = ctk.CTkLabel(tl1, text='Stat Type', font=('Gill Sans MT', 25))
    stat_type_label.place(relx=0.75, rely=0.085, anchor='center')

    league_options = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_type_options = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    league_option_menu_players = ctk.CTkOptionMenu(tl1, width=150, height=50, values=league_options, font=('Gill Sans MT', 15))
    league_option_menu_players.place(relx=0.25, rely=0.15, anchor='center')
    league_option_menu_players.set(league)
    season_option_menu_players = ctk.CTkOptionMenu(tl1, width=150, height=50, values=season_options, font=('Gill Sans MT', 15))
    season_option_menu_players.place(relx=0.5, rely=0.15, anchor='center')
    stat_type_option_menu_players = ctk.CTkOptionMenu(tl1, width=150, height=50, values=stat_type_options, font=('Gill Sans MT', 15))
    stat_type_option_menu_players.place(relx=0.75, rely=0.15, anchor='center')

    search_entry_players = ctk.CTkEntry(tl1, placeholder_text='Search', width=400, font=('Gill Sans MT', 15))
    search_entry_players.place(relx=0.5, rely=0.225, anchor='center')
    search_entry_players.bind('<KeyRelease>', lambda event: filter_data_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players))

    # Set the search entry with the player name if provided
    if player_name:
        search_entry_players.insert(0, player_name)
        # Trigger the filter function to refine the data
        filter_data_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players)

    # Set the command to update the table based on the dropdown selections
    league_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players))
    season_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players))
    stat_type_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players, search_entry_players))

    menu_button = ctk.CTkButton(master=tl1, text='Menu', width=100, command=lambda: main_menu(tl1), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_players(tree, league, '23-24', 'standard')

    tl1.mainloop()

def load_data_matches(tree_matches, league, season, search_term=''):
    file_path = f'data/Matches/{league}/{season}/{league}.pkl'
    
    # Clear the existing data in the treeview
    tree_matches.delete(*tree_matches.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        if search_term:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

        # Set new columns
        tree_matches["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree_matches["columns"]:
            tree_matches.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree_matches.heading(column, text=column, command=lambda _col=column: treeview_sort_column(tree_matches, _col, False))

        # Add new data to the treeview
        for index, row in df.iterrows():
            tree_matches.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def filter_data_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches):
    league = league_option_menu_matches.get()
    season = season_option_menu_matches.get()
    search_term = search_entry_matches.get()
    home_team = home_entry_matches.get().strip()
    away_team = away_entry_matches.get().strip()

    file_path = f'data/Matches/{league}/{season}/{league}.pkl'
    
    # Clear the existing data in the treeview
    tree_matches.delete(*tree_matches.get_children())
    
    try:
        df = pd.read_pickle(file_path)

        if home_team:
            df = df[df['home_team'].str.contains(home_team, case=False, na=False)]
        
        if away_team:
            df = df[df['away_team'].str.contains(away_team, case=False, na=False)]

        if search_term:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

        # Set new columns
        tree_matches["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree_matches["columns"]:
            tree_matches.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree_matches.heading(column, text=column, command=lambda _col=column: treeview_sort_column(tree_matches, _col, False))
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree_matches.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def on_option_change_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches):
    filter_data_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches)

def create_matches():
    tl4 = ctk.CTk()
    tl4.geometry("900x700")
    tl4.title("Matches")
    tl4.resizable(False, False)

    title = ctk.CTkLabel(tl4, text='Matches', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.025, anchor='center')

    frame = ctk.CTkScrollableFrame(tl4, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree_matches = ttk.Treeview(frame, style='Treeview')
    tree_matches.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl4, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.15, rely=0.085, anchor='center')
    season_label = ctk.CTkLabel(tl4, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.383333, rely=0.085, anchor='center')
    home_label = ctk.CTkLabel(tl4, text='Home Team', font=('Gill Sans MT', 25))
    home_label.place(relx=0.616667, rely=0.085, anchor='center')
    away_label = ctk.CTkLabel(tl4, text='Away Team', font=('Gill Sans MT', 25))
    away_label.place(relx=0.85, rely=0.085, anchor='center')

    league_options_matches = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options_matches = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

    league_option_menu_matches = ctk.CTkOptionMenu(tl4, width=150, height=50, values=league_options_matches, font=('Gill Sans MT', 15))
    league_option_menu_matches.place(relx=0.15, rely=0.15, anchor='center')
    season_option_menu_matches = ctk.CTkOptionMenu(tl4, width=150, height=50, values=season_options_matches, font=('Gill Sans MT', 15))
    season_option_menu_matches.place(relx=0.383333, rely=0.15, anchor='center')
    
    home_entry_matches = ctk.CTkEntry(tl4, placeholder_text='Home Team', width=150, font=('Gill Sans MT', 15))
    home_entry_matches.place(relx=0.616667, rely=0.15, anchor='center')
    away_entry_matches = ctk.CTkEntry(tl4, placeholder_text='Away Team', width=150, font=('Gill Sans MT', 15))
    away_entry_matches.place(relx=0.85, rely=0.15, anchor='center')

    search_entry_matches = ctk.CTkEntry(tl4, placeholder_text='Search', width=400, font=('Gill Sans MT', 15))
    search_entry_matches .place(relx=0.5, rely=0.225, anchor='center')
    search_entry_matches.bind('<KeyRelease>', lambda event: filter_data_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches))
    home_entry_matches.bind('<KeyRelease>', lambda event: filter_data_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches))
    away_entry_matches.bind('<KeyRelease>', lambda event: filter_data_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches))

    # Set the command to update the table based on the dropdown selections
    league_option_menu_matches.configure(command=lambda _: on_option_change_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches))
    season_option_menu_matches.configure(command=lambda _: on_option_change_matches(tree_matches, league_option_menu_matches, season_option_menu_matches, search_entry_matches, home_entry_matches, away_entry_matches))

    menu_button = ctk.CTkButton(master=tl4, text='Menu', width=100, command=lambda: main_menu(tl4), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_matches(tree_matches, 'ENG-Premier League', '2023-2024')

    tl4.mainloop()

def load_data_table(tree, league, season, search_term_table=''):
    file_path = f'data/Leagues/{league}/{season}/{league}.pkl'
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        if search_term_table:
            df = df[df.apply(lambda row: row.astype(str).str.contains(search_term_table, case=False).any(), axis=1)]

        # Set new columns
        tree["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree["columns"]:
            tree.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree.heading(column, text=column, command=lambda _col=column: treeview_sort_column(tree, _col, False))
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def on_option_change_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table):
    league = league_option_menu_table.get()
    season = season_option_menu_table.get()
    load_data_table(tree, league, season, search_entry_table.get())

def filter_data_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table):
    on_option_change_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table)

def create_league_tables(league='ENG-Premier League', season='2023-2024'):
    tl4 = ctk.CTk()
    tl4.geometry("900x700")
    tl4.title("League Tables")
    tl4.resizable(False, False)

    title = ctk.CTkLabel(tl4, text='League Tables', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.025, anchor='center')

    frame = ctk.CTkScrollableFrame(tl4, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree = ttk.Treeview(frame, style='Treeview')
    tree.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl4, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.3, rely=0.085, anchor='center')
    season_label = ctk.CTkLabel(tl4, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.7, rely=0.085, anchor='center')

    league_options_table = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options_table = ['2023-2024', '2022-2023', '2021-2022', '2020-2021', '2019-2020', '2018-2019']

    league_option_menu_table = ctk.CTkOptionMenu(tl4, width=150, height=50, values=league_options_table, font=('Gill Sans MT', 15))
    league_option_menu_table.place(relx=0.3, rely=0.15, anchor='center')
    league_option_menu_table.set(league)
    season_option_menu_table = ctk.CTkOptionMenu(tl4, width=150, height=50, values=season_options_table, font=('Gill Sans MT', 15))
    season_option_menu_table.place(relx=0.7, rely=0.15, anchor='center')
    season_option_menu_table.set(season)

    search_entry_table = ctk.CTkEntry(tl4, placeholder_text='Search', width=400, font=('Gill Sans MT', 15))
    search_entry_table .place(relx=0.5, rely=0.225, anchor='center')
    search_entry_table .bind('<KeyRelease>', lambda event: filter_data_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table))

    # Set the command to update the table based on the dropdown selections
    league_option_menu_table.configure(command=lambda _: on_option_change_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table))
    season_option_menu_table.configure(command=lambda _: on_option_change_table(tree, league_option_menu_table, season_option_menu_table, search_entry_table))

    menu_button = ctk.CTkButton(master=tl4, text='Menu', width=100, command=lambda: main_menu(tl4), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_table(tree, league, season)

    tl4.mainloop()

# Code used to create the about page
def create_about():
    tl6 = ctk.CTk()
    tl6.geometry("500x600")
    tl6.title("About")
    tl6.resizable(False,False)

    label = ctk.CTkLabel(master=tl6,text='About',font=('Gill Sans MT', 30))
    label.place(relx=0.425,rely=0.01)

    # Opens up the about text file and displays it in a textbox
    textbox = ctk.CTkTextbox(master=tl6, width=485, height=450, font =('Gill Sans MT', 15))
    textbox.place(relx=0.025,rely=0.1)
    with open (r'about.txt') as file:
        data = file.read()
    textbox.insert('1.0',data)
    textbox.configure(state='disabled')

    menu_button = ctk.CTkButton(master=tl6, text='Menu', height=50, width=200, command=lambda: main_menu(tl6), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5,rely=0.9,anchor='center')
    tl6.mainloop()

# Code used to create the settings page
def create_settings():
    tl7 = ctk.CTk()
    tl7.geometry("500x600")
    tl7.title("Settings")
    tl7.resizable(False, False)

    settings_label = ctk.CTkLabel(master=tl7, text='Settings', font=('Gill Sans MT', 30))
    settings_label.place(relx=0.5, rely=0.05, anchor='center')
    apperance_label = ctk.CTkLabel(master=tl7, text='Appearance', font=('Gill Sans MT', 20))
    apperance_label.place(relx=0.5, rely=0.2, anchor='center')

    # Option menu to change the appearance to light, dark and system colours
    appearance_menu = ctk.CTkOptionMenu(master=tl7, values=['Light','Dark', 'System'], font=('Gill Sans MT', 15), command=lambda mode: appearance_change(mode))
    appearance_menu.place(relx=0.5, rely=0.3, anchor='center')
    appearance_menu.set(current_theme)

    menu_button = ctk.CTkButton(master=tl7, text='Menu', height=50, width=200, command=lambda: main_menu(tl7), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.9, anchor='center')

    tl7.mainloop()

# Command for changing the apperance of the window
def appearance_change(mode: str):
    global current_theme, appearance_change
    current_theme = mode
    ctk.set_appearance_mode(mode)

# Command for the main menu button
def main_menu(root):
    root.withdraw()
    app.deiconify()

app.mainloop()