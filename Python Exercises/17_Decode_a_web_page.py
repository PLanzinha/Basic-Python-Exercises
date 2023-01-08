from bs4 import BeautifulSoup
import requests


# Exercise 17 - Decode A Web Page

# Use the BeautifulSoup and requests Python packages to print out a list of all the article
# titles on the New York Times homepage.


def scrap():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    h3_ele = soup.find_all(class_='css-xdandi')

    titles = [h3.get_text() for h3 in h3_ele]
    title = []
    for tile in titles:
        if title not in titles:
            title.append(tile)
    print(title)


scrap()


def scrap():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    h3_ele = soup.find_all('h3')

    titles = [h3.get_text() for h3 in h3_ele]

    for title in titles:
        print(title)


scrap()
