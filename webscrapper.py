import requests
import pandas as pd
from bs4 import BeautifulSoup
  
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('a'))
week = soup.find(id = 'seven-day-forecast-body')
item = week.find_all(class_ ='tombstone-container')


period_name =[item1.find(class_='period-name').get_text() for item1 in item]
description =[item1.find(class_='short-desc').get_text() for item1 in item]
temperature =[item1.find(class_='temp').get_text() for item1 in item]

dataframe  = pd.DataFrame(
    {
    'days':period_name,
    'weather':description,
    'temperature':temperature,
    })
print(dataframe)
dataframe = dataframe.to_csv('weather.csv')
    

    
    