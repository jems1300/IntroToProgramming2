'''
- bs4(beautifulSoup) is a library for parsing HTML and XML documents (in this instance for scraping the web)
btw parsing means to turn one form of data into a data structure. It makes it easier for the machine to read compared
to literal characters

- 'requests' is a library that simplifies sending like request from the web broswer, in this instance requesting the url

- we can take advantage of 're' library unctions like search, match, find_all and etc for data validation and stuff

- web browser actually lets us open links if needed
'''
from functools import partial

from bs4 import BeautifulSoup
import requests
import re
import webbrowser

product_input = input("Search: ")

# I will create an empty dictionary
items_found = {}
# This is our url, I included a input so if I want to look up something else other than a GPU, it's easily modifiable
url = f"https://www.newegg.com/p/pl?d={product_input}&N=4131"
page_content = requests.get(url).text
# This will let me access the contents of the url in a text format in the console.
spaghetti = BeautifulSoup(page_content, 'html.parser')

page_text = spaghetti.find(class_ = "list-tool-pagination-text").strong # <- Including this makes it extremely easy to isolate it in the console

# In order to split up the statement, we have to convert it to a string
page_num = int(str(page_text).split("/")[1].split(">")[-1][:-1]) # <- This slices off the last element



# I used the inspect element on newEgg to find the page elements. Basically the idea, is that we'll isolate the page
# number, then loop through all the pages to find each matching text and price and list them all.
# So for a 9070 can have different page amount, compared to a different product that might have 10 pages.



# if page_num > 2:
#     print(f"There are {page_num} pages")
# else:
#     print(f"There is {page_num} page")


for page_num in range(1, page_num + 1):
    url = f"https://www.newegg.com/p/pl?d={product_input}&N=4131"
    page_content = requests.get(url).text
    spaghetti = BeautifulSoup(page_content, 'html.parser')

    list_wrap = spaghetti.find_all("div", class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
    if not list_wrap:
        continue # <-- EXTREMELY important! Basically in the loop below it kept counting outside the bounded area

# Not mine
    items = spaghetti.find_all("div", class_ = "item-cell")

    for item in items:
        title_tag = item.find("a", class_="item-title")
        price_tag = item.find("li", class_="price-current")

        if title_tag and price_tag:
            title = title_tag.text
            link = title_tag['href']

            # Some prices have <strong> and <sup> inside
            price_strong = price_tag.find("strong")
            price_sup = price_tag.find("sup")
            if price_strong and price_sup:
                price = f"${price_strong.text}{price_sup.text}"
                items_found[title] = (price, link)

# Sort and print all
for title, (price, link) in sorted(items_found.items()):
    print(f"{title} — {price}\n{link}\n")