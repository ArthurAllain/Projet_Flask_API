from bs4 import BeautifulSoup
from requests import get

url = 'https://fr.wikipedia.org/wiki/Representational_state_transfer'

response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
content = html_soup.main.get_text()

