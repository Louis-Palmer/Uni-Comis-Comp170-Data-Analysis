import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def CSV():
  LeaderBoardData = open("HospitalRegional.csv")
  ReadData = csv.reader(LeaderBoardData)

  for entry in ReadData:
    print(entry[8])
  LeaderBoardData.close()

def main():
  font1= {'family':'sans-serif','color':'Black','size':30}#creates a font style.
  font2 ={'family':'sans-serif','color':'Black','size':20}#same as above.
  sns.set_palette(sns.color_palette("dark")) #Changes the colour
  frame = pd.read_csv("Data Research\CSV\Hospital Beds\Germany ICU 2017.csv") #Reads the Data from the csv and stores it as frame variable.
  newFrame = frame.sort_values(by = "beds",ascending=False) #sorts through the data into descending order of bed count and sotres it a newframe
  plt.rcParams["figure.figsize"] = [50, 50] #changes size of barchart
  plt.rcParams["figure.autolayout"] = True #automaticly adjusts the layout
  plottedData = sns.barplot(data=newFrame,x="state",y="beds").get_figure() #creates the bar chart using the sorted data
  plt.title("ICU Hospital beds for Germany 2017",fontdict=font1)
  plt.xlabel("States",fontdict=font2)
  plt.ylabel("Beds",fontdict=font2)
  plottedData.savefig(dir_path+"\Data Research\Images\Europe Acute 2017\ICU Germany titled") #saves the barchart automaticly.
  plt.show() #displays the barchart during execution.

def HeatMap():
  worldmap = gpd.read_file(dir_path+"\Data\World map SHP Data\World_Countries__Generalized_.shp")#reads the shapefile (a Map) of the world.
  dataframe = pd.read_csv(dir_path+"\Data\CSV\Hospital Beds\Global_Total.csv")#reads the dataset.
  font1= {'family':'sans-serif','color':'Black','size':30}#creates a font style.
  font2 ={'family':'sans-serif','color':'Black','size':20}#same as above.
  print("worldsmap",worldmap.columns) # prints the names of the collums.
  print("Dataframe",dataframe.columns)# this is because The collum that contains the iso codes needs to be the same name.
  map_and_stats=worldmap.merge(dataframe, on="ISO") #merges the dataset and the map using the iso codes.
  fig, ax = plt.subplots(1, figsize=(40, 40)) #sets the size of the heatmap.
  map_and_stats.plot(column="beds", cmap="binary", linewidth=0.4, ax=ax, edgecolor=".4",legend = True)#creates the heatmap and the bar on the rightside of the heatmap.
  plt.xlabel("Latitude",fontdict=font2) #creates the label with the suing the fonts we created earlier.
  plt.ylabel("Longitude",fontdict=font2)#same as above.
  plt.title("Total Hospital Beds Per 1000 People",fontdict=font1) # creates a title with the font from above.

  #plt.savefig("C:\Users\louis\Comp170-2206106-1\Images\4.Extras\Heatmap\mightbe.png")#save the heatmap automaticly.
  plt.show()#displays the heatmap after excecution.


def Dropnas():
  sns.set_palette(sns.color_palette("dark"))
  frame = pd.read_csv("HospitalRegional.csv")
  frame.drop(frame[frame["year"]=="2016"].index)
  print(frame)
  frame.plot(x="year",y="beds",kind="bar")
  plt.show()

def Cleaner():
  data = open(dir_path+"\Data Research\CSV\Hospital Beds\GlobalMixed.csv")
  df = pd.read_csv(data)
  print(df)
  cleanedDf = df[df["type"] == "Total"]
  #cleanedDf = cleanedDF[cleanedDf["year"] == 2019]
  HeatMapCleaned(cleanedDf)

def HeatMapCleaned(dataframe):
  worldmap = gpd.read_file(dir_path+"\Data Research\World map\World_Countries__Generalized_.shp")
  print("worldsmap",worldmap.columns)
  dataframe.rename(columns={"country": "ISO"}, inplace=True)
  print("Dataframe",dataframe.columns)
  map_and_stats=worldmap.merge(dataframe, on="ISO")
  fig, ax = plt.subplots(1, figsize=(40, 40))
  map_and_stats.plot(column="beds", cmap="Reds", linewidth=0.4, ax=ax, edgecolor=".4")

  bar_info = plt.cm.ScalarMappable(cmap="Reds",norm=plt.Normalize(vmin=0, vmax=20))
  bar_info._A = []
  cbar = fig.colorbar(bar_info)

  plt.savefig(dir_path+"\Data Research\Images\Heatmap\HeatmapICU")
  print(dataframe)
  plt.show()



  

#Cleaner()
#main()
HeatMap()

