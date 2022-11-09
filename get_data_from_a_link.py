from bs4 import BeautifulSoup
import requests


url = "https://roar.media/bangla/main/science/the-history-of-diseases"

html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "html.parser")


p = soup.find_all('postcontentroarcheck')

for tag in p:
    print(tag.get_text().strip())

