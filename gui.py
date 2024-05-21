# Import required libaries
from tkinter import *
from tkinter import ttk
import customtkinter
import soccerdata as sd
import pandas as pd
from PIL import ImageTk, Image
import os
import random
from CTkTable import *

# Create the main app window
app = customtkinter.CTk()
app.geometry("675x700")
app.title("Football Database App")
app.resizable(False,False)

# Set the appearance mode for default color theme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
current_theme = 'Dark'

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

def open_rankings():
    app.withdraw()
    create_rankings()

# All the code used to create the home gui page
def create_home():
    # Creates a grid to easily place the buttons in the sidebar frame
    sidebar = customtkinter.CTkFrame(master=app,width=1,height=700,corner_radius=0)
    sidebar.grid()
    sidebar_button1 = customtkinter.CTkButton(sidebar,width=100,text='Rankings',command=open_rankings, font=('Gill Sans MT', 15))
    sidebar_button1.grid(row=1, column=0,padx=5,pady=5)
    sidebar_button2 = customtkinter.CTkButton(sidebar,width=100,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    sidebar_button2.grid(row=2, column=0,padx=5,pady=5)
    sidebar_button3 = customtkinter.CTkButton(sidebar,width=100,text='Players',command=open_players, font=('Gill Sans MT', 15))
    sidebar_button3.grid(row=3, column=0,padx=5,pady=5)
    sidebar_button4 = customtkinter.CTkButton(sidebar,width=100,text='Leagues',command=open_leagues, font=('Gill Sans MT', 15))
    sidebar_button4.grid(row=4, column=0,padx=5,pady=5)
    sidebar_button6 = customtkinter.CTkButton(sidebar,width=100,text='Favourites',command=open_favs, font=('Gill Sans MT', 15))
    sidebar_button6.grid(row=5, column=0,padx=5,pady=5)
    sidebar_button7 = customtkinter.CTkButton(sidebar,width=100,text='Years',command=open_years, font=('Gill Sans MT', 15))
    sidebar_button7.grid(row=6, column=0,padx=5,pady=5)
    sidebar_button11 = customtkinter.CTkButton(sidebar,width=100,text='',fg_color='',hover=False)
    sidebar_button11.grid(row=9, column=0,padx=5,pady=145)
    sidebar_button8 = customtkinter.CTkButton(sidebar,width=100,text='Tools',command=open_tools, font=('Gill Sans MT', 15))
    sidebar_button8.grid(row=8, column=0,padx=5,pady=5)
    sidebar_button9 = customtkinter.CTkButton(sidebar,width=100,text='About',command=open_about, font=('Gill Sans MT', 15))
    sidebar_button9.grid(row=10, column=0,padx=5,pady=5)
    sidebar_button10 = customtkinter.CTkButton(sidebar,width=100,text='Settings',command=open_settings, font=('Gill Sans MT', 15))
    sidebar_button10.grid(row=11, column=0,padx=5,pady=5)
    exit_button = customtkinter.CTkButton(sidebar,width=100,text='Exit',command=app.withdraw, fg_color='red', font=('Gill Sans MT', 15))
    exit_button.grid(row=12, column=0,padx=5,pady=5)

    # Create the buttons for the home screen
    button1 = customtkinter.CTkButton(master=app, text="Leagues", command=open_leagues, font=('Gill Sans MT', 15))
    button1.place(relx=0.2, rely=0.1)
    button2 =customtkinter.CTkButton(master=app,text='Players',command=open_players, font=('Gill Sans MT', 15))
    button2.place(relx=0.475,rely=0.1)
    button3 =customtkinter.CTkButton(master=app,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    button3.place(relx=0.75,rely=0.1)
    entry = customtkinter.CTkEntry(master=app, placeholder_text='Search', width=525, font=('Gill Sans MT', 15))
    entry.place(relx=0.2,rely=0.025)

    # Titles the league, team and player cards
    league_text = customtkinter.CTkLabel(master=app,text='League Ladder',font=('Gill Sans MT', 22))
    league_text.place(relx=0.375,rely=0.21, anchor='w')
    player_text = customtkinter.CTkLabel(master=app,text='Player Card',font=('Gill Sans MT', 22))
    player_text.place(x=175,rely=0.59)
    team_text = customtkinter.CTkLabel(master=app,text='Team Card',font=('Gill Sans MT', 22))
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
    league_image_label = customtkinter.CTkLabel(app, image=league_photo, text='')
    league_image_label.place(relx=0.575, rely=0.4, anchor='center')
    league_image_label.image= league_photo
    player_image = Image.open(picture_path2)
    new_photo2 = player_image.resize((player_width, player_height))
    player_photo = ImageTk.PhotoImage(new_photo2)
    player_image_label = customtkinter.CTkLabel(app, image=player_photo, text='')
    player_image_label.place(relx=0.375, rely=0.825, anchor='center')
    player_image_label.image = player_photo
    team_image = Image.open(picture_path3)
    new_photo3 = team_image.resize((team_width, team_height))
    team_photo = ImageTk.PhotoImage(new_photo3)
    team_image_label = customtkinter.CTkLabel(app, image=team_photo, text='')
    team_image_label.place(relx=0.785, rely=0.825, anchor='center')
    team_image_label.image = team_photo

    # Configures the card titles so that they are displaying the team, league and player names
    league_text.configure(text=f'League Ladder - {os.path.splitext(os.path.basename(random_pic1))[0]}')
    player_text.configure(text=f'Player Card \n {os.path.splitext(os.path.basename(random_pic2))[0]}')
    team_text.configure(text=f'Team Card \n {os.path.splitext(os.path.basename(random_pic3))[0]}')

create_home()

# Code used to create and display team statistics
def create_teams():
    tl3 = customtkinter.CTk()
    tl3.geometry("900x700")
    tl3.resizable(True,False)
    tl3.title("Teams")

    style = ttk.Style(tl3)
    style.configure("Treeview", background="#242424", foreground="white")

    title = customtkinter.CTkLabel(tl3, text='Team Statistics',font=('Gill Sans MT', 30))
    title.place(relx=0.5, rely=0.05, anchor='center')

    frame = customtkinter.CTkScrollableFrame(tl3,height=550,width=900,orientation='horizontal',fg_color='transparent')
    frame.place(rely=0.1)

    # Get the team statistics from the fbref module
    fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
    team_stats = fbref.read_team_season_stats(stat_type='standard')
    df = pd.DataFrame(team_stats)

    # Remove unwanted columns and add teams column to the table
    df = df.drop(columns=['Per 90 Minutes', 'Progression', 'url','Playing Time'])
    teams = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton', 
             'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Leeds United', 
             'Leicester City', 'Liverpool', 'Manchester City', 'Manchester Utd', 
             'Newcastle Utd', "Nott'ham Forest", 'Southampton', 'Tottenham', 
             'West Ham', 'Wolves']
    df.insert(0, 'Team', teams)
    
    # Create Treeview widget
    tree = ttk.Treeview(frame)
    tree["columns"] = df.columns.tolist()
    tree["show"] = "headings"

    # Add columns
    for column in df.columns:
        tree.heading(column, text=column)

    # Add data to the treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=tuple(row))

    # Add the treeview to the window
    tree.pack(expand=True, fill="both",pady=(100,0))

    menu_button = customtkinter.CTkButton(master=tl3, text='Menu', width=100, command=lambda: main_menu(tl3), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.925, anchor='center')

    tl3.mainloop()

def create_players():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("Players")
    tl8.resizable(False,False)

def create_favs():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("Favourites")
    tl8.resizable(False,False)

def create_years():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("Years")
    tl8.resizable(False,False)

def create_tools():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("Tools")
    tl8.resizable(False,False)

def create_rankings():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("Rankings")
    tl8.resizable(False,False)

def create_leagues():
    tl4 = customtkinter.CTk()
    tl4.geometry("500x600")
    tl4.title("League Statistics")
    tl4.resizable(False, False)

    fbref = sd.FBref(leagues = ['ENG-Premier League'], seasons = ['2223'])
    season_stats = fbref.read_team_season_stats(stat_type='')
    league_frame = customtkinter.CTkFrame(master=tl4, width=490, height=500, corner_radius=0)
    league_frame.place(relx=0.01, rely=0.075)

    table_text = customtkinter.CTkTextbox(master=league_frame, font=('Gill Sans MT', 12),width=480, height = 490)
    table_text.place(relx=0.01, rely=0.01)
    table_text.insert('1.0', season_stats)

    tl4.mainloop()

# Code used to create the about page
def create_about():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("About")
    tl8.resizable(False,False)

    label = customtkinter.CTkLabel(master=tl8,text='About',font=('Gill Sans MT', 30))
    label.place(relx=0.425,rely=0.01)

    # Opens up the about text file and displays it in a textbox
    textbox = customtkinter.CTkTextbox(master=tl8, width=475, height=450, font =('Gill Sans MT', 15))
    textbox.place(relx=0.025,rely=0.1)
    with open (r'about.txt') as file:
        data = file.read()
    textbox.insert('1.0',data)
    textbox.configure(state='disabled')

    menu_button = customtkinter.CTkButton(master=tl8, text='Menu', height=50, width=200, command=lambda: main_menu(tl8), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5,rely=0.9,anchor='center')
    tl8.mainloop()

# Code used to create the settings page
def create_settings():
    tl9 = customtkinter.CTk()
    tl9.geometry("500x600")
    tl9.title("Settings")
    tl9.resizable(False, False)

    settings_label = customtkinter.CTkLabel(master=tl9, text='Settings', font=('Gill Sans MT', 30))
    settings_label.place(relx=0.5, rely=0.05, anchor='center')
    apperance_label = customtkinter.CTkLabel(master=tl9, text='Appearance', font=('Gill Sans MT', 20))
    apperance_label.place(relx=0.5, rely=0.2, anchor='center')

    # Option menu to change the appearance to light, dark and system colours
    appearance_menu = customtkinter.CTkOptionMenu(master=tl9, values=['Dark', 'Light', 'System'], font=('Gill Sans MT', 15), command=lambda mode: appearance_change(mode))
    appearance_menu.place(relx=0.5, rely=0.3, anchor='center')
    appearance_menu.set(current_theme)

    menu_button = customtkinter.CTkButton(master=tl9, text='Menu', height=50, width=200, command=lambda: main_menu(tl9), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.9, anchor='center')

    tl9.mainloop()

# Command for changing the apperance of the window
def appearance_change(mode: str):
    global current_theme, appearance_change
    current_theme = mode
    customtkinter.set_appearance_mode(mode)

# Command for the main menu button
def main_menu(root):
    root.withdraw()
    app.deiconify()

app.mainloop()