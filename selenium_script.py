import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def get_random_book():
    url = 'https://www.goodreads.com/review/list/159310567-kirill-pavlov?ref=nav_mybooks&shelf=to-read'

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    def scroll_to_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

    scroll_to_bottom(driver)


    page = driver.page_source

    titles = driver.find_elements(By.CLASS_NAME, 'field.title')
    authors = driver.find_elements(By.CLASS_NAME, 'field.author')

    books = []

    for title, author, in zip(titles, authors):
        books.append({"title": title.text.strip(), "author": author.text.strip()})

    random_book = random.choice(books)

    driver.quit()

    print(len(books))

    return random_book

print(get_random_book())





    


