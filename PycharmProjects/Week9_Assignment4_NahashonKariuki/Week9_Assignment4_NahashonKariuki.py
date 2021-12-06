# start by installing required libraries which include requests for making HTTP requests and bs4 to extract the data
# from the HTML.install lxml as a parser
# Starting by importing the relevant libraries

import requests
from bs4 import BeautifulSoup
from datetime import datetime


# the url to scrap
url = f"https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 '
                  'Safari/537.36'
}# id card for my request module

# request to download the data
response = requests.get(url, headers=headers)

# to see if the page is accessible or not if result  is 200 it means that it is okay
print(response.status_code)

# verifying if the page is valid
print(response.headers)

# Extracting and storing the data from the page in a variable
source = response.content

# use beautifulsoup to parse and transform the data we have just stored
soup = BeautifulSoup(source,"html5lib")
print(soup.prettify()) # this is to see the source code of the page. the prettify organises the code in a structure that is readable

# this is to parse out specific tags
match = soup.find("")# using find method to parse in some arguments
print(match)

bookinfo = soup.select(".zg-item-immersion")

popular_books = []
for book in bookinfo:
    if "a-star-5" not in str(book):
        continue
    for book_names in book.select(".p13n-sc-truncate"):

        popular_books.append(book_names.getText().strip())

popular_books_prices = []
for book in bookinfo:
    if "a-star-5" in str(book):
        for prices in book.find(name="span", class_="p13n-sc-price"):
            popular_books_prices.append(float(prices.replace("$", "")))

sorted_top_ten_prices = []
max_range = 10
sorted_top_ten_prices.sort()
sorted_top_ten_prices = sorted_top_ten_prices[-max_range:]

ten_most_expensive = []
unsorted_prices = []

for book in bookinfo:
    if "a-star-5" in str(book):
        for val in sorted_top_ten_prices:
            if f"${val}" in str(book):
                ten_most_expensive.append((book.find(name="div", class_="p13n-sc-truncate").text.strip()))

final_result = [{ten_most_expensive[i]: unsorted_prices[i] for i in range(len(ten_most_expensive))}]
print(final_result)
