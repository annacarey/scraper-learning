# Tutorial: https://medium.com/swlh/tutorial-web-scraping-instagrams-most-precious-resource-corgis-235bf0389b0c

import pandas as pd
import time
from selenium.webdriver import Chrome

url = "https://www.instagram.com/explore/tags/workoutclass/?hl=en"

def get_post_links(link):
  if link[0:28] == 'https://www.instagram.com/p/':
    return True 
  else:
    return False

browser = Chrome()
browser.get(url)
top_links = [a.get_attribute('href') for a in browser.find_elements_by_tag_name('a')]
top_links = list(filter(get_post_links, top_links))[0:9]

comments = []
def view_all_links(links):
    for link in links:
        browser.get(link)
        xpath = '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span'
        comment = browser.find_element_by_xpath(xpath).text
        comments.append(comment)

view_all_links(top_links)
print(comments)

