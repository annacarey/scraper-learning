import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en;q=0.5"}


url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url, headers=headers) 

soup = BeautifulSoup(results.text, "html.parser")

# Empty lists to store the data
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for movie_container in movie_div:
    title = movie_container.h3.a.text
    titles.append(title)



print(titles)

