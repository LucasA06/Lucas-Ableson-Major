from tkinter import *
import customtkinter
import csv
import soccerdata as sd
import pandas as pd
import seaborn as sns
import matplotlib as plt
from pandastable import Table, TableModel
from PIL import ImageTk, Image
import os
import random

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.geometry("600x665")
app.minsize(600,665)
app.maxsize(600,665)
app.title("Football Database App")
app.resizable(False,False)

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

def create_home():
    sidebar = customtkinter.CTkFrame(master=app,width=100,height=700,corner_radius=0)
    sidebar.grid()
    sidebar_button1 = customtkinter.CTkButton(sidebar,width=85,text='Rankings',command=open_rankings, font=('Gill Sans MT', 15))
    sidebar_button1.grid(row=1, column=0,padx=10,pady=5)
    sidebar_button2 = customtkinter.CTkButton(sidebar,width=85,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    sidebar_button2.grid(row=2, column=0,padx=10,pady=5)
    sidebar_button3 = customtkinter.CTkButton(sidebar,width=85,text='Players',command=open_players, font=('Gill Sans MT', 15))
    sidebar_button3.grid(row=3, column=0,padx=10,pady=5)
    sidebar_button4 = customtkinter.CTkButton(sidebar,width=85,text='Leagues',command=open_leagues, font=('Gill Sans MT', 15))
    sidebar_button4.grid(row=4, column=0,padx=10,pady=5)
    sidebar_button6 = customtkinter.CTkButton(sidebar,width=85,text='Favourites',command=open_favs, font=('Gill Sans MT', 15))
    sidebar_button6.grid(row=5, column=0,padx=10,pady=5)
    sidebar_button7 = customtkinter.CTkButton(sidebar,width=85,text='Years',command=open_years, font=('Gill Sans MT', 15))
    sidebar_button7.grid(row=6, column=0,padx=10,pady=5)
    sidebar_button11 = customtkinter.CTkButton(sidebar,width=85,text='',fg_color='',hover=False)
    sidebar_button11.grid(row=9, column=0,padx=10,pady=125)
    sidebar_button8 = customtkinter.CTkButton(sidebar,width=85,text='Tools',command=open_tools, font=('Gill Sans MT', 15))
    sidebar_button8.grid(row=8, column=0,padx=10,pady=5)
    sidebar_button9 = customtkinter.CTkButton(sidebar,width=85,text='About',command=open_about, font=('Gill Sans MT', 15))
    sidebar_button9.grid(row=10, column=0,padx=10,pady=5)
    sidebar_button10 = customtkinter.CTkButton(sidebar,width=85,text='Settings',command=open_settings, font=('Gill Sans MT', 15))
    sidebar_button10.grid(row=11, column=0,padx=10,pady=5)
    exit_button = customtkinter.CTkButton(sidebar,width=85,text='Exit',command=app.withdraw, fg_color='red', font=('Gill Sans MT', 15))
    exit_button.grid(row=12, column=0,padx=10,pady=5)

    button1 = customtkinter.CTkButton(master=app, text="Leagues", command=open_leagues, font=('Gill Sans MT', 15))
    button1.place(relx=0.2, rely=0.1)
    button2 =customtkinter.CTkButton(master=app,text='Players',command=open_players, font=('Gill Sans MT', 15))
    button2.place(relx=0.475,rely=0.1)
    button3 =customtkinter.CTkButton(master=app,text='Teams',command=open_teams, font=('Gill Sans MT', 15))
    button3.place(relx=0.75,rely=0.1)
    entry = customtkinter.CTkEntry(master=app, placeholder_text='Search', width=475, font=('Gill Sans MT', 15))
    entry.place(relx=0.2,rely=0.025)

    league_text = customtkinter.CTkLabel(master=app,text='League Ladder',font=('Gill Sans MT', 22))
    league_text.place(relx=0.4,rely=0.21, anchor='w')
    player_text = customtkinter.CTkLabel(master=app,text='Player Card',font=('Gill Sans MT', 22))
    player_text.place(relx=0.25,rely=0.57)
    team_text = customtkinter.CTkLabel(master=app,text='Team Card',font=('Gill Sans MT', 22))
    team_text.place(relx=0.655,rely=0.57)

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

    screen_width_mm = app.winfo_screenmmwidth()
    screen_height_mm = app.winfo_screenmmheight()

    league_width = int(screen_width_mm * 0.3)
    league_height = int(league_width * 265 / 700)
    player_width = int(screen_width_mm * 0.15)
    player_height = int(player_width * 200 / 300)
    team_width = int(screen_width_mm * 0.175)
    team_height = int(team_width * 200 / 350)

    league_width = int(league_width * (app.winfo_screenwidth() / screen_width_mm))
    league_height = int(league_height * (app.winfo_screenheight() / screen_height_mm))
    player_width = int(player_width * (app.winfo_screenwidth() / screen_width_mm))
    player_height = int(player_height * (app.winfo_screenheight() / screen_height_mm))
    team_width = int(team_width * (app.winfo_screenwidth() / screen_width_mm))
    team_height = int(team_height * (app.winfo_screenheight() / screen_height_mm))

    league_frame = customtkinter.CTkFrame(master=app, width=league_width, height=league_height, corner_radius=0)
    league_frame.place(relx=0.6, rely=0.375)
    league_image = Image.open(picture_path)
    league_image = league_image.resize((league_width, league_height))
    league_photo = ImageTk.PhotoImage(league_image)
    league_image_label = customtkinter.CTkLabel(league_frame, image=league_photo, text='')
    league_image_label.place(relx=0.5, rely=0.5, anchor='center')

    player_frame = customtkinter.CTkFrame(master=app, width=player_width, height=player_height, corner_radius=0)
    player_frame.place(relx=0.375, rely=0.8)
    player_image = Image.open(picture_path2)
    player_image = player_image.resize((player_width, player_height))
    player_photo = ImageTk.PhotoImage(player_image)
    player_image_label = customtkinter.CTkLabel(player_frame, image=player_photo, text='')
    player_image_label.place(relx=0.5, rely=0.5, anchor='center')

    team_frame = customtkinter.CTkFrame(master=app,width=team_width,height=team_height)
    team_frame.place(relx=0.785, rely=0.8)
    team_image = Image.open(picture_path3)
    team_image = team_image.resize((team_width, team_height))
    team_photo = ImageTk.PhotoImage(team_image)
    team_image_label = customtkinter.CTkLabel(app, image=team_photo, text='')
    team_image_label.place(relx=0.5,rely=0.5, anchor='center')

    league_text.configure(text=f'League Ladder - {os.path.splitext(os.path.basename(random_pic1))[0]}')
    player_text.configure(text=f'Player Card \n {os.path.splitext(os.path.basename(random_pic2))[0]}')
    team_text.configure(text=f'Team Card \n {os.path.splitext(os.path.basename(random_pic3))[0]}')

create_home()

def create_teams():
    tl3 = Tk()
    tl3.geometry("1800x1000")
    tl3.title("Teams")
    tl3.resizable(False, False)

    fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['2223'])
    team_stats = fbref.read_team_season_stats(stat_type='standard')
    df = pd.DataFrame(team_stats)
    txt = Text(tl3, width=180,height=100)
    txt.place(x=0, y=0)          
    txt.insert(END, df)

    menu_button = customtkinter.CTkButton(master=tl3, text='Menu', height=40, width=150, command=lambda: main_menu(tl3), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.95, anchor='center')

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

def create_about():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("About")
    tl8.resizable(False,False)

    label = customtkinter.CTkLabel(master=tl8,text='About',font=('Gill Sans MT', 30))
    label.place(relx=0.425,rely=0.01)

    textbox = customtkinter.CTkTextbox(master=tl8, width=475, height=450, font =('Gill Sans MT', 15))
    textbox.place(relx=0.025,rely=0.1)
    with open (r'about.txt') as file:
        data = file.read()
    textbox.insert('1.0',data)

    textbox.configure(state='disabled')

    menu_button = customtkinter.CTkButton(master=tl8, text='Menu', height=50, width=200, command=lambda: main_menu(tl8), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5,rely=0.9,anchor='center')
    tl8.mainloop()

current_theme = 'Dark'

def create_settings():
    tl9 = customtkinter.CTk()
    tl9.geometry("500x600")
    tl9.title("Settings")
    tl9.resizable(False, False)

    settings_label = customtkinter.CTkLabel(master=tl9, text='Settings', font=('Gill Sans MT', 30))
    settings_label.place(relx=0.5, rely=0.05, anchor='center')

    apperance_label = customtkinter.CTkLabel(master=tl9, text='Appearance', font=('Gill Sans MT', 20))
    apperance_label.place(relx=0.5, rely=0.2, anchor='center')

    appearance_menu = customtkinter.CTkOptionMenu(master=tl9, values=['Dark', 'Light', 'System'], font=('Gill Sans MT', 15), command=lambda mode: appearance_change(mode))
    appearance_menu.place(relx=0.5, rely=0.3, anchor='center')
    appearance_menu.set(current_theme)

    menu_button = customtkinter.CTkButton(master=tl9, text='Menu', height=50, width=200, command=lambda: main_menu(tl9), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.9, anchor='center')

    tl9.mainloop()

def appearance_change(mode: str):
    global current_theme, appearance_change
    current_theme = mode
    customtkinter.set_appearance_mode(mode)

def main_menu(root):
    root.withdraw()
    app.deiconify()

app.mainloop()