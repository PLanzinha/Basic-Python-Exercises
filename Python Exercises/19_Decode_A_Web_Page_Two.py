from bs4 import BeautifulSoup
import requests


# Exercise 19 - Decode A Web Page Two

# Using the requests and BeautifulSoup Python libraries,
# print to the screen the full text of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# vanity fair removed the pages, so using this one instead http://books.toscrape.com/,
# will go into pages and get the title and description of each for the first page

# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read
# the full article without having to click any buttons.

# (Hint: The post here describes in detail how to use the BeautifulSoup
# and requests libraries through the solution of the exercise posted here.)#

# This will just print the full text of the article to the screen.
# It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.


def scrape():
    url = 'http://books.toscrape.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    all_h3 = soup.find_all('h3')

    # titles = [a['title'] for h3 in all_h3 for a in h3.find_all('a')]

    all_href = [a['href'] for h3 in all_h3 for a in h3.find_all('a')]

    all_url = []

    for i in all_href:
        complete_url = url + i
        all_url.append(complete_url)
    # print(all_url)

    for i in all_url:
        r = requests.get(i)
        soup = BeautifulSoup(r.text, features="html.parser")

        book_info = soup.find('div', class_='col-sm-6 product_main')

        if book_info:
            title = book_info.find('h1').get_text()
            description = soup.find('meta', attrs={'name': 'description'})['content']
            price = book_info.find('p', class_='price_color').get_text()

            print(f"Title:", title)
            print(f"Description:", description)
            print(f"Price:", price)
            print("\n")


scrape()
