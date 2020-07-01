# Tutorial: https://medium.com/better-programming/the-only-step-by-step-guide-youll-need-to-build-a-web-scraper-with-python-e79066bd895a

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Following this tutorial

headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url, headers=headers) 

soup = BeautifulSoup(results.text, "html.parser")

# Empty lists to store the data
titles = []
years = []
lengths = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for movie_container in movie_div:

    # Add title
    title = movie_container.h3.a.text
    titles.append(title)

    # Add year
    year = movie_container.h3.find('span', class_='lister-item-year text-muted unbold').text[1:-1]
    years.append(year)

    # Add length of movie
    movie_length = movie_container.find('span', class_='runtime').text
    lengths.append(movie_length)

    # Add imdb rating
    imdb_rating = float(movie_container.strong.text)
    imdb_ratings.append(imdb_rating)

    # Add metascores
    metascore = int(movie_container.find('span', class_='metascore').text)
    metascores.append(metascore)
    
    # Add votes
    vote_count = movie_container.find('p', class_='sort-num_votes-visible').find_all('span')[1].text
    votes.append(vote_count)

    #Add US gross
    gross = movie_container.find('p', class_='sort-num_votes-visible').find_all('span')[4].text if len(movie_container.find('p', class_='sort-num_votes-visible').find_all('span'))>2 else '-'
    us_gross.append(gross)



print(us_gross)

