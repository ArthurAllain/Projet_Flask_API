from bs4 import BeautifulSoup
from requests import get
import pandas as pd

url = 'https://fr.wikipedia.org/wiki/Representational_state_transfer'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
content = html_soup.main.get_text()

content_alpha = ""

for char in content:
  if ord(char) >= 65 and ord(char) <= 90:
    content_alpha += char
  elif ord(char) >= 97 and ord(char) <= 122:
    content_alpha += char
  elif ord(char) >= 192 and ord(char) <= 246:
    content_alpha += char
  elif ord(char) == 32:
    content_alpha += char
  elif ord(char) == 10:
    content_alpha += char
  else:
    content_alpha += " "

c_split = content_alpha .split()

w_count= {}
for wd in c_split:
  if wd in w_count :
    w_count[wd]+= 1
  else:
    w_count[wd]= 1

print(w_count)