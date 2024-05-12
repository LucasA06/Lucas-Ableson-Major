# Developer Notes
## Problems

1. The home page images do not stay a consistent size across devices and I am trying to figure out a way to make them all stay a consistent size and ratio across all devices.

2. There are not many useful libaries that I can find that is helpful for displaying the statistics in the way I want them displayed so I am trying to play around with differnt libaries and methods to display the statistics in the format I would like.

3. Some statistics are very hard to find and export when relating to that stats that I would like to display. i.e. the league tables are very hard to find in a pandas dataframe or any type of dataframe.

## Soultions

1. I have used the .resize feature of PhotoImage to make it relative to the size of different computers and monitors. The pictures are saved as part of the github repository and are pulled from it into the main gui home page of my gui. I also used app.minsize and app.maxsize to make sure that the main window's size cannot be changed no matter how big or small someones monitor is.

    Edit: I have realised that .resize does not work across devices because the size of the pictures depended on the systems scale so I have decided that the pictures will be on 100% scale and when someone download's my app I will get them, through the installation guide, to check their display scale and if it is not 100% I will get them to change it. It is between that or I make different gui files depending on different display scales.