import bs4
import requests
from fake_headers import Headers


header = Headers(headers=False)
HEADER = header.generate()

KEYWORDS = ['Научно-популярное', 'Карьера в IT-индустрии', 'Терминология IT', 'Хакатоны']
URL = "https://habr.com/ru/all/"

response = requests.get(URL, headers=HEADER)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
    hubs = [hub.text.strip() for hub in hubs]
    date = article.find("time").text
    title = article.find('a', class_='tm-article-snippet__title-link').find('span').text
    link = article.find(class_="tm-article-snippet__title-link").attrs['href']
    for hub in hubs:
        for keyword in KEYWORDS:
            if keyword in hub:
                print(f'{date} - {title} - {link}')
