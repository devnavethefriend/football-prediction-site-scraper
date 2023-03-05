# Import beautifulsoup & request module
from bs4 import BeautifulSoup
import requests

# Getting website URL & initiating soup instance
html_text = requests.get('https://www.forebet.com/en/football-tips-and-predictions-for-today/predictions-under-over-goals').text
soup = BeautifulSoup(html_text, 'lxml')

# Creating var containers for soup objects using element tags
highest_probabilities = soup.find_all('span', class_='fpr')
predictions = soup.find_all('span', class_='forepr')
home_teams = soup.find_all('span', class_='homeTeam')
away_teams = soup.find_all('span', class_='awayTeam')

# Get first ten matches & predictions
pred_list = predictions[:10]
prob_list = highest_probabilities[:10]
home_list = home_teams[:10]
away_list = away_teams[:10]

print("Done retrieving data")
print("Printing teams and predictions")

# Display each match & prediction
for prob, hometeam, awayteam, predict in zip(prob_list, home_list, away_list, pred_list):
    print(f"{hometeam.text} vs {awayteam.text}\n Probability: {prob.text}\n Prediction: {predict.text}")