# import beautifulsoup & request module
from bs4 import BeautifulSoup
import requests

# make a request to the website
url = "https://www.forebet.com/en/football-tips-and-predictions-for-today/predictions-under-over-goals"
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find the sections containing the teams & predictions
highest_probabilities = soup.find_all('span', class_='fpr')
predictions = soup.find_all('span', class_='forepr')
home_teams = soup.find_all('span', class_='homeTeam')
away_teams = soup.find_all('span', class_='awayTeam')

# define a function to get the matches & predictions for a given number of inputs
def get_matches_and_predictions(user_input):
    pred_list = predictions[:user_input]
    prob_list = highest_probabilities[:user_input]
    home_list = home_teams[:user_input]
    away_list = away_teams[:user_input]

    return (pred_list, prob_list, home_list, away_list)

# prompt the user for the number of matches to get
try:
    # make sure input is integer
    user_input = int(input("Enter the number of matches to retrieve: "))
    print("Loading information...")
except ValueError:
    # catch the ValueError exception if the input is not an integer
    print("Input error!")

# get the first 'user_input' matches and predictions
matches_and_predictions = get_matches_and_predictions(user_input)

# open a new text file for writing
with open("result.txt", "w") as file:
    # write each match & prediction
    for prob, hometeam, awayteam, predict in matches_and_predictions:
        file.write(f"{hometeam.text} vs {awayteam.text}  Probability: {prob.text}  Prediction: {predict.text}\n")