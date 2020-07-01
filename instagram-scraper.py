# Tutorial: 

import requests
from requests import get
from bs4 import BeautifulSoup

url = "https://www.instagram.com/explore/tags/fitness/?hl=en"

results = requests.get(url) 

soup = BeautifulSoup(results.text, "html.parser")

print(soup)