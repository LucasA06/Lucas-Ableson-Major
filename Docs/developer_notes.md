# Developer Notes
## Problems

1. The home page images do not stay a consistent size across devices and I am trying to figure out a way to make them all stay a consistent size and ratio across all devices.

2. There are not many useful libaries that I can find that is helpful for displaying the statistics in the way I want them displayed so I am trying to play around with differnt libaries and methods to display the statistics in the format I would like.

3. Some statistics are very hard to find and export when relating to that stats that I would like to display. i.e. the league tables are very hard to find in a pandas dataframe or any type of dataframe.

4. Whenever the application is first started an error pops up which reads ```UserWarning: CTkLabel Warning: Given image is not CTkImage but <class 'PIL.ImageTk.PhotoImage'>. Image can not be scaled on HighDPI displays, use CTkImage instead. warnings.warn(f"{type(self).__name__} Warning: Given image is not CTkImage but {type(image)}. Image can not be scaled on HighDPI displays, use CTkImage instead.\n")``` and also when the terms and conditons window is accecpted an error pops up which reads ```invalid command name "2103330467072<lambda>"
    while executing
"2103330467072<lambda>"
    ("after" script)
invalid command name "2103330467712update"
    while executing
"2103330467712update"
    ("after" script)
invalid command name "2103330468032check_dpi_scaling"
    while executing
"2103330468032check_dpi_scaling"
    ("after" script)
invalid command name "2103330467648_click_animation"
    while executing
"2103330467648_click_animation"
    ("after" script)```.

## Solutions

1. I have used the .resize feature of PhotoImage to make it relative to the size of different computers and monitors. The pictures are saved as part of the github repository and are pulled from it into the main gui home page of my gui. I also used app.minsize and app.maxsize to make sure that the main window's size cannot be changed no matter how big or small someones monitor is.

    Edit: I have realised that .resize does not work across devices because the size of the pictures depended on the systems scale so I have decided that the pictures will be on 100% scale and when someone download's my app I will get them, through the installation guide, to check their display scale and if it is not 100% I will get them to change it. It is between that or I make different gui files depending on different display scales.

2. I found a very useful libiary called soccerdata (sd) which I used to get all of the stats into my folder and then I found a widget in tkinter called ttk.Treeview which I used to create all the respective tables and change them when the option menus are changed.

3. In soccerdata I can pull data from FutMob which has a read_league_table for the leagues I want to display so I used that to pull the data and display it in my applicaton.

4. I have realised that the errors do not impact my code or have any effect on the user experience and are basically suggestions so I am just going to leave them as is because they do not affect anything.

## To Dos
* Find a better way to import massive amounts of data only once so that there isn't a massive wait time everytime the app opens as it is loading in all the data every time when there is already data there. *Completed

* Import and display all the data under their respective headings in a nice format. *Completed

* Get the search bar working and displaying kewwords and stats based on string queries.

* Get buttons under the pictures so that users can click on the pictures and they display the stats based upon the league, team or player. *Completed

* Make a terms and services that pops up once and never again once someone has read it and agreed to it. *Completed

* I need to add tooltips to each dataset's headings so user know what each thing means.

## Completed To Dos
* Finished the Gui and all the pictures that are displayed in the gui and fixed a problem with the display of the pictures.

* Found the best method to display the data in a way I like and a way that looks the best to me.

* I am going to import all the data I need into a folder called 'data' and add it to my respository so the data is always there when I need to access it in my gui.

* Terms and Service window now works and pops up when you first start the application and doesn't pop up again once you agree to it.

* I used the .bind feature to make it so when button 1 is clicked over one of the pictures it opens up the stats for that respective picture.

