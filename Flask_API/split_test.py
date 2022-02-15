from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://fr.wikipedia.org/wiki/Representational_state_transfer'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
content = html_soup.main.get_text()

content.split().value_counts()

c_split = content.split(sep=",")

w_count= {}
for wd in c_split:
  if wd in w_count :
    w_count[wd]+= 1
  else:
    w_count[wd]= 1