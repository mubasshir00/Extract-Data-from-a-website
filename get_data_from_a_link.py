# import requests
# from bs4 import BeautifulSoup

# base_url = "https://roar.media/bangla/main/science"

# page = requests.get('https://roar.media/bangla/main/science')

# soup = BeautifulSoup(page.content, 'html.parser')

# all_links = []

# links = soup.select('a')

# for link in links:
#     print(link)
#     text = link.get_text()
#     text = text.strip()
#     href = link.get('href')
#     href = href.strip()
#     links.append(href)

# if href.find(base_url) != -1:
#     print(href)
#     all_links.append(href)

# for h in all_links:
#     print(h)

from bs4 import BeautifulSoup
import requests
import json


url = "https://roar.media/bangla/main/science"

base_url = "https://roar.media/bangla/main/science/"

html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "html.parser")


p = soup.find_all('a')

all_links = []

for i in range(0, 1):
    for tag in p:
        # print(tag.get('href'))
        all_links.append(tag.get('href'))

formated_text = []

for link in all_links:
    if link.find(base_url) != -1:
        html_content_art = requests.get(link).text

        soup_art = BeautifulSoup(html_content_art, "html.parser")

        arti = soup_art.find_all('postcontentroarcheck')

        for art in arti:
            # print(art.get_text().strip())
            formated_text.append({
                "article": art.get_text().strip()
            })

        with open('test.txt', 'w') as f:
            f.write(str(formated_text))
