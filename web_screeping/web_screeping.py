import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.findAll('div'))
