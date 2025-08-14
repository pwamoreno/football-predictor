import requests
from bs4 import BeautifulSoup
import pandas as pd

standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standing_url)

soup = BeautifulSoup(data.text)
standings_table = soup.select("table.stats_table")[0]
links = standings_table.find_all("a")
links = [l.get("href") for l in links]
links = [l for l in links if "/squads/" in l]

team_urls = [f"https://fbref.com{l}" for l in links]
team_url = team_urls[0]
data = requests.get(team_url)

matches = pd.read_html(data.text, match="Scores & Fixtures")