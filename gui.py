from tkinter import *
import customtkinter
import tkinter as tk
import gettext
import csv
import soccerdata as sd
import pandas as pd

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.geometry("600x665")
app.title("Football Database App")
app.resizable(False,False)
    
def open_leagues():
    app.withdraw()
    create_leagues()

def open_teams():
    app.withdraw()
    tl3 = customtkinter.CTk()
    tl3.geometry("500x600")
    tl3.title("Teams")
    tl3.mainloop()

def open_players():
    app.withdraw()
    tl2 = customtkinter.CTk()
    tl2.geometry("500x600")
    tl2.title("Players")
    tl2.mainloop()

def open_favs():
    app.withdraw()
    tl5 = customtkinter.CTk()
    tl5.geometry("500x600")
    tl5.title("Favorites")
    tl5.mainloop()

def open_years():
    app.withdraw()
    tl6 = customtkinter.CTk()
    tl6.geometry("500x600")
    tl6.title("Years")
    tl6.mainloop()

def open_tools():
    app.withdraw()
    tl7 = customtkinter.CTk()
    tl7.geometry("500x600")
    tl7.title("Tools")
    tl7.mainloop()

def open_about():
    app.withdraw()
    create_about()

def open_settings():
    app.withdraw()
    create_settings()

def open_rankings():
    app.withdraw()
    tl10 = customtkinter.CTk()
    tl10.geometry("500x600")
    tl10.title("Rankings")
    tl10.mainloop()

def appearance_change(mode: str):
    customtkinter.set_appearance_mode(mode)

def main_menu(root):
    root.withdraw()
    app.deiconify()

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
button3 =customtkinter.CTkButton(master=app,text='Teams',command=open_players, font=('Gill Sans MT', 15))
button3.place(relx=0.75,rely=0.1)
entry = customtkinter.CTkEntry(master=app, placeholder_text='Search', width=475, font=('Gill Sans MT', 15))
entry.place(relx=0.2,rely=0.025)

league_frame = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=0)
league_frame.place(relx=0.225,rely=0.275)
league_text = customtkinter.CTkLabel(master=app,text='League Ladder',font=('Gill Sans MT', 22))
league_text.place(relx=0.29,rely=0.22)

player_frame = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=0)
player_frame.place(relx=0.625,rely=0.25)
player_text = customtkinter.CTkLabel(master=app,text='Player Card',font=('Gill Sans MT', 22))
player_text.place(relx=0.7,rely=0.2)

ranking_frame = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=0)
ranking_frame.place(relx=0.225,rely=0.67)
ranking_text = customtkinter.CTkLabel(master=app,text='Player/Team\nRankings',font=('Gill Sans MT', 22))
ranking_text.place(relx=0.3,rely=0.575)

team_frame = customtkinter.CTkFrame(master=app,width=200,height=200,corner_radius=0)
team_frame.place(relx=0.625,rely=0.625)
team_text = customtkinter.CTkLabel(master=app,text='Team Card',font=('Gill Sans MT', 22))
team_text.place(relx=0.71,rely=0.57)

def create_leagues():
    tl4 = tk.Tk()
    tl4.geometry("1000x600")
    tl4.title("Premier League 2022/2023")
    tl4.resizable(False, False)

    fbref = sd.FBref(leagues = ['ENG-Premier League'], seasons = ['2223'])
    season_stats = fbref.read_team_season_stats(stat_type='standard')

    tl4.mainloop()

def create_about():
    tl8 = customtkinter.CTk()
    tl8.geometry("500x600")
    tl8.title("About")
    tl8.resizable(False,False)

    label = customtkinter.CTkLabel(master=tl8,text='About',font=('Gill Sans MT', 30))
    label.place(relx=0.5,rely=0.05,anchor='center')

    textbox = customtkinter.CTkTextbox(master=tl8, width=475, height=425)
    textbox.place(relx=0.5,rely=0.4)
    textbox.insert('1.0', "This is a football database app created by Lucas. It is still in development and is not yet complete.")
    textbox.configure(state='disabled')
    textbox.place(relx=0.5,rely=0.45,anchor='center')

    menu_button = customtkinter.CTkButton(master=tl8, text='Menu', height=50, width=200, command=lambda: main_menu(tl8), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5,rely=0.9,anchor='center')
    tl8.mainloop()

current_theme = 'Dark'

current_theme = 'Dark'

def save_current_theme():
    with open('current_theme.txt', 'w') as file:
        file.write(current_theme)

def load_current_theme():
    try:
        with open('current_theme.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return 'Dark'

def create_settings():
    current_theme = load_current_theme()

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
    appearance_menu.set(current_theme)  # Set the current theme in the menu

    menu_button = customtkinter.CTkButton(master=tl9, text='Menu', height=50, width=200, command=lambda: main_menu(tl9), font=('Gill Sans MT', 15))
    menu_button.place(relx=0.5, rely=0.9, anchor='center')

    tl9.mainloop()

def appearance_change(mode: str):
    global current_theme
    current_theme = mode
    customtkinter.set_appearance_mode(mode)
    save_current_theme()

def main_menu(root):
    root.withdraw()
    app.deiconify()

app.mainloop()