import requests
from bs4 import BeautifulSoup

URL = 'https://knife.media/best/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
           'accept': '/*/'}


def get_html(html):
    request = requests.get(html, headers=HEADERS)
    return request


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='unit unit--triple')

    topics = []
    for item in items:
        topics.append({
            'head': item.find('div', 'unit__head').get_text(),
            'text': item.find('a', 'unit__content-link').get_text().replace('\xa0', ' '),
            'author': item.find('a', 'meta__item').get_text(),
            'published': item.find('span', 'meta__item').get_text()
        })

    for topic in topics:
        print('head: ' + topic['head'])
        print('text: ' + topic['text'])
        print('author: ' + topic['author'])
        print('published: ' + topic['published'])
        print()


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Nothing for You')


parse()
