import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

def scrape_data(hyperlink):
    
    request = requests.get(hyperlink)

    soup = BeautifulSoup(request.text, 'html.parser')

    star_table = soup.find_all('table')

    rows = star_table[7].find_all('tr')

    star_data = []
    
    for row in rows:
        
        columns = row.find_all('td')
       
        row_data = []
        
        row_data.append([i.text.rstrip() for i in columns])
        
        star_data.append(row_data)
    
    headers = ['name', 'radius', 'mass', 'distance']

    name = []
    distance = []
    mass = []
    radius = []
    
    for i in range(1, len(star_data)):
       
        name.append(star_data[i][0][0])

        distance.append(star_data[i][0][5])

        mass.append(star_data[i][0][7])

        radius.append(star_data[i][0][8])   

    df = pd.DataFrame(list(zip(name, radius, mass, distance)), columns=headers)
    df.to_csv('final_data.csv')

scrape_data(START_URL)