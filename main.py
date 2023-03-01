# Import required module
from bs4 import BeautifulSoup
import requests

# Getting website using requests & initiating soup instance
html_text = requests.get('https://www.forebet.com/en/football-tips-and-predictions-for-today/predictions-under-over-goals').text
soup = BeautifulSoup(html_text, 'lxml')

# Creating var containers for soup objects using element tags
highest_probabilities = soup.find_all('span', class_='fpr')
predictions = soup.find_all('span', class_='forepr')
homeTeams = soup.find_all('span', class_='homeTeam')
awayTeams = soup.find_all('span', class_='awayTeam')
container_A = soup.find_all('div', class_='rcnt tr_0')
container_B = soup.find_all('div', class_='rcnt tr_1')

# This code joins two seperate list containers into one
list_of_games = []
list_of_games.extend(container_A)
list_of_games.extend(container_B)
print(len(list_of_games))

