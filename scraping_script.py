from urllib.request import urlopen
import bs4
import requests
from bs4 import BeautifulSoup
import random



def get_random_book():
    url = 'https://www.goodreads.com/review/list/159310567-kirill-pavlov?ref=nav_mybooks&shelf=to-read'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.find_all('td', class_='field title')
    authors = soup.find_all('td', class_='field author')

    books = []

    for title, author in zip(titles, authors):
        books.append({"title": title.get_text().strip(), "author": author.get_text().strip()})

    random_book = random.choice(books)

    return random_book






