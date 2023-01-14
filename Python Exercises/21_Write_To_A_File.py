# Exercise 21 -  Write To A File

# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some
# different code, use the code from the solution), and instead of printing the results to a screen, write the results
# to a txt file. In your code, just make up a name for the file you are saving to.
# Extras:
# Ask the user to specify the name of the output file that will be saved.

from bs4 import BeautifulSoup
import requests


def scrape():
    url = 'http://books.toscrape.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    all_h3 = soup.find_all('h3')

    all_href = [a['href'] for h3 in all_h3 for a in h3.find_all('a')]

    all_url = []

    for i in all_href:
        complete_url = url + i
        all_url.append(complete_url)

    save_name = input("Save file name as:\n")

    if not save_name.endswith('.txt'):
        save_name += '.txt'

    with open(save_name, 'w', encoding='latin-1') as save:
        for i in all_url:
            r = requests.get(i)
            soup = BeautifulSoup(r.text, features="html.parser")

            book_info = soup.find('div', class_='col-sm-6 product_main')

            if book_info:
                title = book_info.find('h1').get_text()
                description = soup.find('meta', attrs={'name': 'description'})['content']
                price = book_info.find('p', class_='price_color').get_text()

                save.write(f"Title: {title}\n")
                save.write(f"Description: {description}\n")
                save.write(f"Price: {price}\n\n")


if __name__ == "__main__":
    scrape()

