from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

DwarfStars = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(DwarfStars)

soup = bs(page.text,'html.parser')
Tvalue = soup.find_all("table")
df = []
rows = Tvalue[7].find_all('tr')

for i in rows:
    td = i.find_all('td')
    stripper = [index.text.rstrip() for index in td]
    df.append(stripper)

name = []
dist = []
mass = []
radi = []

for i in range(1,len(df)):
    name.append(df[i][0])
    dist.append(df[i][5])
    mass.append(df[i][8])
    radi.append(df[i][9])

mdf = pd.DataFrame(list(zip(name,dist,mass,radi)),columns=["Star","Distance","Mass","Radius"])

mdf.to_csv("Dwarf_Stars_Data.csv")