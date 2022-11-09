import requests
from bs4 import BeautifulSoup

base_url = "https://roar.media/bangla/main/science"

page = requests.get('https://roar.media/bangla/main/science')

soup = BeautifulSoup(page.content, 'html.parser')

all_links = []

links = soup.select('a')

for link in links:
    text = link.text
    text = text.strip()
    href = link.get('href')
    href = href.strip()
    links.append(href)

    if href.find(base_url) != -1:
        print(href)
