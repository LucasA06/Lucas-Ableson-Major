# Import required libaries
from tkinter import ttk
import customtkinter as ctk
import pandas as pd
from PIL import ImageTk, Image
import os
import random
import tkinter as tk
import sys

def agree_clicked():
    # Save agreement status (you can use a file, database, etc.)
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
    # User has not agreed yet, show the terms window
    root = ctk.CTk()
    root.title("Terms and Conditions")
    root.geometry('500x600')
    root.resizable(False,False)
    root.configure(bg='white')
    def disable_event():
        pass
    root.protocol("WM_DELETE_WINDOW", disable_event)

    terms_label = ctk.CTkTextbox(root,font =('Gill Sans MT', 15),width=490,height=500)  # Add your terms here
    terms_label.pack(padx=10, pady=10)
    with open (r'Term and Service') as file:
        data = file.read()
    terms_label.insert('1.0',data)
    terms_label.configure(state='disabled')

    agree_button = ctk.CTkButton(root, text="Agree", command=agree_clicked)
    agree_button.place(relx=0.1,rely=0.9)

    disagree_button = ctk.CTkButton(root, text="Disagree", command=disagree_clicked)
    disagree_button.place(relx=0.65,rely=0.9)

    root.mainloop()

# Create the main app window
app = ctk.CTk()
app.geometry("675x700")
app.title("Football Database App")
app.resizable(False,False)

# Set the appearance mode for default color theme
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')
current_theme = 'Light'

# All the code used to open the different pages
def open_leagues():
    app.withdraw()
    create_leagues()

def open_teams():
    app.withdraw()
    create_teams()

def open_players():
    app.withdraw()
    create_players()

def open_favs():
    app.withdraw()
    create_favs()

def open_years():
    app.withdraw()
    create_years()

def open_tools():
    app.withdraw()
    create_tools()

def open_about():
    app.withdraw()
    create_about()

def open_settings():
    app.withdraw()
    create_settings()

def open_top_scorers():
    app.withdraw()
    create_top_scorers()

# All the code used to create the home gui page
def create_home():
    # Creates a grid to easily place the buttons in the sidebar frame
    sidebar = ctk.CTkFrame(master=app,width=1,height=700,corner_radius=0)
    sidebar.grid()
    sidebar_button1 = ctk.CTkButton(sidebar,width=100,text='Rankings',command=open_top_scorers, font=('Gill Sans MT', 15))
    sidebar_button1.grid(row=1, column=0,padx=5,pady=5)
    sidebar_button2 = ctk.CTkButton(sidebar,width=100,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    sidebar_button2.grid(row=2, column=0,padx=5,pady=5)
    sidebar_button3 = ctk.CTkButton(sidebar,width=100,text='Players',command=open_players, font=('Gill Sans MT', 15))
    sidebar_button3.grid(row=3, column=0,padx=5,pady=5)
    sidebar_button4 = ctk.CTkButton(sidebar,width=100,text='Leagues',command=open_leagues, font=('Gill Sans MT', 15))
    sidebar_button4.grid(row=4, column=0,padx=5,pady=5)
    sidebar_button6 = ctk.CTkButton(sidebar,width=100,text='Favourites',command=open_favs, font=('Gill Sans MT', 15))
    sidebar_button6.grid(row=5, column=0,padx=5,pady=5)
    sidebar_button7 = ctk.CTkButton(sidebar,width=100,text='Years',command=open_years, font=('Gill Sans MT', 15))
    sidebar_button7.grid(row=6, column=0,padx=5,pady=5)
    sidebar_button11 = ctk.CTkButton(sidebar,width=100,text='',fg_color='',hover=False)
    sidebar_button11.grid(row=9, column=0,padx=5,pady=145)
    sidebar_button8 = ctk.CTkButton(sidebar,width=100,text='Tools',command=open_tools, font=('Gill Sans MT', 15))
    sidebar_button8.grid(row=8, column=0,padx=5,pady=5)
    sidebar_button9 = ctk.CTkButton(sidebar,width=100,text='About',command=open_about, font=('Gill Sans MT', 15))
    sidebar_button9.grid(row=10, column=0,padx=5,pady=5)
    sidebar_button10 = ctk.CTkButton(sidebar,width=100,text='Settings',command=open_settings, font=('Gill Sans MT', 15))
    sidebar_button10.grid(row=11, column=0,padx=5,pady=5)
    exit_button = ctk.CTkButton(sidebar,width=100,text='Exit',command=app.withdraw, fg_color='red', font=('Gill Sans MT', 15))
    exit_button.grid(row=12, column=0,padx=5,pady=5)

    # Create the buttons for the home screen
    button1 = ctk.CTkButton(master=app, text="Leagues", command=open_leagues, font=('Gill Sans MT', 15))
    button1.place(relx=0.2, rely=0.1)
    button2 =ctk.CTkButton(master=app,text='Players',command=open_players, font=('Gill Sans MT', 15))
    button2.place(relx=0.475,rely=0.1)
    button3 =ctk.CTkButton(master=app,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    button3.place(relx=0.75,rely=0.1)
    entry = ctk.CTkEntry(master=app, placeholder_text='Search', width=525, font=('Gill Sans MT', 15))
    entry.place(relx=0.2,rely=0.025)

    # Titles the league, team and player cards
    league_text = ctk.CTkLabel(master=app,text='League Ladder',font=('Gill Sans MT', 22))
    league_text.place(relx=0.375,rely=0.21, anchor='w')
    player_text = ctk.CTkLabel(master=app,text='Player Card',font=('Gill Sans MT', 22))
    player_text.place(x=175,rely=0.59)
    team_text = ctk.CTkLabel(master=app,text='Team Card',font=('Gill Sans MT', 22))
    team_text.place(x=450,rely=0.59)

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

    # Set the width and height of the home screen pictures
    league_width = 525
    league_height = int(league_width * 265/700)
    player_width = 250
    player_height = int(player_width * 200/300)
    team_width = 275
    team_height = int(team_width * 200/350)

    # Opens the pictures, resizes them and displays them in the home screen
    league_image = Image.open(picture_path)
    new_photo1 = league_image.resize((league_width, league_height))
    league_photo = ImageTk.PhotoImage(new_photo1)
    league_image_label = ctk.CTkLabel(app, image=league_photo, text='')
    league_image_label.place(relx=0.575, rely=0.4, anchor='center')
    league_image_label.image= league_photo
    player_image = Image.open(picture_path2)
    new_photo2 = player_image.resize((player_width, player_height))
    player_photo = ImageTk.PhotoImage(new_photo2)
    player_image_label = ctk.CTkLabel(app, image=player_photo, text='')
    player_image_label.place(relx=0.375, rely=0.825, anchor='center')
    player_image_label.image = player_photo
    team_image = Image.open(picture_path3)
    new_photo3 = team_image.resize((team_width, team_height))
    team_photo = ImageTk.PhotoImage(new_photo3)
    team_image_label = ctk.CTkLabel(app, image=team_photo, text='')
    team_image_label.place(relx=0.785, rely=0.825, anchor='center')
    team_image_label.image = team_photo

    # Configures the card titles so that they are displaying the team, league and player names
    league_text.configure(text=f'League Ladder - {os.path.splitext(os.path.basename(random_pic1))[0]}')
    player_text.configure(text=f'Player Card \n {os.path.splitext(os.path.basename(random_pic2))[0]}')
    team_text.configure(text=f'Team Card \n {os.path.splitext(os.path.basename(random_pic3))[0]}')

create_home()

def load_data_teams(tree, league, season, stat_type):
    file_path = f'data/Team/{league}/{season}/{stat_type}.pkl'
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        # Set new columns
        tree["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree["columns"]:
            tree.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree.heading(column, text=column)
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def on_option_change_teams(tree, league_option_menu_teams, season_option_menu_teams, stat_type_option_menu_teams):
    league = league_option_menu_teams.get()
    season = season_option_menu_teams.get()
    stat_type = stat_type_option_menu_teams.get()
    load_data_teams(tree, league, season, stat_type)

def create_teams():
    tl3 = ctk.CTk()
    tl3.geometry("900x700")
    tl3.resizable(True, False)
    tl3.title("Teams")

    title = ctk.CTkLabel(tl3, text='Team Statistics', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.05, anchor='center')

    frame = ctk.CTkScrollableFrame(tl3, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree = ttk.Treeview(frame, style='Treeview')
    tree.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl3, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.25, rely=0.11, anchor='center')
    season_label = ctk.CTkLabel(tl3, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.5, rely=0.11, anchor='center')
    stat_type_label = ctk.CTkLabel(tl3, text='Stat Type', font=('Gill Sans MT', 25))
    stat_type_label.place(relx=0.75, rely=0.11, anchor='center')

    league_options = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_type_options = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    league_option_menu_teams = ctk.CTkOptionMenu(tl3, width=150, height=50, values=league_options, font=('Gill Sans MT', 15))
    league_option_menu_teams.place(relx=0.25, rely=0.175, anchor='center')
    season_option_menu_teams = ctk.CTkOptionMenu(tl3, width=150, height=50, values=season_options, font=('Gill Sans MT', 15))
    season_option_menu_teams.place(relx=0.5, rely=0.175, anchor='center')
    stat_type_option_menu_teams = ctk.CTkOptionMenu(tl3, width=150, height=50, values=stat_type_options, font=('Gill Sans MT', 15))
    stat_type_option_menu_teams.place(relx=0.75, rely=0.175, anchor='center')

    # Set the command to update the table based on the dropdown selections
    league_option_menu_teams.configure(command=lambda _: on_option_change_teams(tree, league_option_menu_teams, season_option_menu_teams, stat_type_option_menu_teams))
    season_option_menu_teams.configure(command=lambda _: on_option_change_teams(tree, league_option_menu_teams, season_option_menu_teams, stat_type_option_menu_teams))
    stat_type_option_menu_teams.configure(command=lambda _: on_option_change_teams(tree, league_option_menu_teams, season_option_menu_teams, stat_type_option_menu_teams))

    menu_button = ctk.CTkButton(master=tl3, text='Menu', width=100, command=lambda: main_menu(tl3), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_teams(tree, 'ENG-Premier League', '23-24', 'standard')

    tl3.mainloop()

def on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players):
    league = league_option_menu_players.get()
    season = season_option_menu_players.get()
    stat_type = stat_type_option_menu_players.get()
    load_data_players(tree, league, season, stat_type)

def load_data_players(tree, league, season, stat_type):
    file_path = f'data/Players/{league}/{season}/{stat_type}.pkl'
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    try:
        df = pd.read_pickle(file_path)
        
        # Set new columns
        tree["columns"] = df.columns.tolist()
        
        # Remove existing headings
        for column in tree["columns"]:
            tree.heading(column, text="")

        # Add new headings
        for column in df.columns:
            tree.heading(column, text=column)
        
        # Add new data to the treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=tuple(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def create_players():
    tl8 = ctk.CTk()
    tl8.geometry("900x700")
    tl8.title("Players")
    tl8.resizable(False,False)

    title = ctk.CTkLabel(tl8, text='Player Statistics', font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.05, anchor='center')

    frame = ctk.CTkScrollableFrame(tl8, height=450, width=900, orientation='horizontal', fg_color='transparent')
    frame.place(rely=0.25)

    tree = ttk.Treeview(frame, style='Treeview')
    tree.pack(expand=True, fill="both")

    league_label = ctk.CTkLabel(tl8, text='League', font=('Gill Sans MT', 25))
    league_label.place(relx=0.25, rely=0.11, anchor='center')
    season_label = ctk.CTkLabel(tl8, text='Season', font=('Gill Sans MT', 25))
    season_label.place(relx=0.5, rely=0.11, anchor='center')
    stat_type_label = ctk.CTkLabel(tl8, text='Stat Type', font=('Gill Sans MT', 25))
    stat_type_label.place(relx=0.75, rely=0.11, anchor='center')

    league_options = ['ENG-Premier League', 'ESP-La Liga', 'ITA-Serie A','GER-Bundesliga','FRA-Ligue 1']
    season_options = ['23-24', '22-23', '21-22', '20-21', '19-20', '18-19']
    stat_type_options = ['Standard', 'Keeper', 'Shooting', 'Passing', 'Defense', 'Misc']

    league_option_menu_players = ctk.CTkOptionMenu(tl8, width=150, height=50, values=league_options, font=('Gill Sans MT', 15))
    league_option_menu_players.place(relx=0.25, rely=0.175, anchor='center')
    season_option_menu_players = ctk.CTkOptionMenu(tl8, width=150, height=50, values=season_options, font=('Gill Sans MT', 15))
    season_option_menu_players.place(relx=0.5, rely=0.175, anchor='center')
    stat_type_option_menu_players = ctk.CTkOptionMenu(tl8, width=150, height=50, values=stat_type_options, font=('Gill Sans MT', 15))
    stat_type_option_menu_players.place(relx=0.75, rely=0.175, anchor='center')

    # Set the command to update the table based on the dropdown selections
    league_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players))
    season_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players))
    stat_type_option_menu_players.configure(command=lambda _: on_option_change_players(tree, league_option_menu_players, season_option_menu_players, stat_type_option_menu_players))

    menu_button = ctk.CTkButton(master=tl8, text='Menu', width=100, command=lambda: main_menu(tl8), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

    load_data_players(tree, 'ENG-Premier League', '23-24', 'standard')

    tl8.mainloop()

def create_favs():
    tl8 = ctk.CTk()
    tl8.geometry("500x600")
    tl8.title("Favourites")
    tl8.resizable(False,False)

def create_years():
    tl8 = ctk.CTk()
    tl8.geometry("500x600")
    tl8.title("Years")
    tl8.resizable(False,False)

def create_tools():
    tl8 = ctk.CTk()
    tl8.geometry("500x600")
    tl8.title("Tools")
    tl8.resizable(False,False)

def create_top_scorers():
    tl8 = ctk.CTk()
    tl8.geometry("500x600")
    tl8.title("Rankings")
    tl8.resizable(False,False)

def create_leagues():
    tl4 = ctk.CTk()
    tl4.geometry("500x600")
    tl4.title("League Statistics")
    tl4.resizable(False, False)
    tl4.mainloop()

# Code used to create the about page
def create_about():
    tl8 = ctk.CTk()
    tl8.geometry("500x600")
    tl8.title("About")
    tl8.resizable(False,False)

    label = ctk.CTkLabel(master=tl8,text='About',font=('Gill Sans MT', 30))
    label.place(relx=0.425,rely=0.01)

    # Opens up the about text file and displays it in a textbox
    textbox = ctk.CTkTextbox(master=tl8, width=485, height=450, font =('Gill Sans MT', 15))
    textbox.place(relx=0.025,rely=0.1)
    with open (r'about.txt') as file:
        data = file.read()
    textbox.insert('1.0',data)
    textbox.configure(state='disabled')

    menu_button = ctk.CTkButton(master=tl8, text='Menu', height=50, width=200, command=lambda: main_menu(tl8), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5,rely=0.9,anchor='center')
    tl8.mainloop()

# Code used to create the settings page
def create_settings():
    tl9 = ctk.CTk()
    tl9.geometry("500x600")
    tl9.title("Settings")
    tl9.resizable(False, False)

    settings_label = ctk.CTkLabel(master=tl9, text='Settings', font=('Gill Sans MT', 30))
    settings_label.place(relx=0.5, rely=0.05, anchor='center')
    apperance_label = ctk.CTkLabel(master=tl9, text='Appearance', font=('Gill Sans MT', 20))
    apperance_label.place(relx=0.5, rely=0.2, anchor='center')

    # Option menu to change the appearance to light, dark and system colours
    appearance_menu = ctk.CTkOptionMenu(master=tl9, values=['Dark', 'Light', 'System'], font=('Gill Sans MT', 15), command=lambda mode: appearance_change(mode))
    appearance_menu.place(relx=0.5, rely=0.3, anchor='center')
    appearance_menu.set(current_theme)

    menu_button = ctk.CTkButton(master=tl9, text='Menu', height=50, width=200, command=lambda: main_menu(tl9), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.9, anchor='center')

    tl9.mainloop()

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