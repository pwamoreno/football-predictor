import requests
from bs4 import BeautifulSoup

standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"

data = requests.get(standing_url)

soup = BeautifulSoup(data.text)