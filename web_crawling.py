import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.w3schools.com/')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('h4.w3-margin-top'):
    print(tag.text)
