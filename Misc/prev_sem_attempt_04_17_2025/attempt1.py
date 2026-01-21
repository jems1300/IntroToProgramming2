from bs4 import BeautifulSoup
import requests
import re
import webbrowser

gpu_input = input("Search: ")

url = f"https://www.newegg.com/p/pl?N=4131&d={gpu_input}&page=1"
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

page_text = soup.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
# Split and then get the 2nd last element

# print(page_text)
print(pages)

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={gpu_input}&N=4131&page={page}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find(class_ = "item-cells-wrap border-cells short-video-box items-list-view is-list")

    items = div.find_all("div", class_ = "item-cell")

    for item in items:
        parent = item.find("a", class_="item-title")
        if not parent:
            continue

        link = parent['href']
        next_parent = item.find_parent(class_ = "item-container position-relative")
        price = div.find(class_ = "price-current").strong.string

        # page_text = soup.find(class_="list-tool-pagination-text").strong
        # pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

        items_found = {link : f"${price}"}

    print(dict(sorted(items_found.items(), key=lambda x: x[0])))

print(items_found)

# for item in sorted_items:
#     print(items[0])
#     print(f"${items[1]['price']}")
#     print(items[1]['link'])
    #
    # print(items)
    #
    # div = soup.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
    # items = div.find_all("div", class_="item-cell")
    #
    # # Just look at the first one
    # if items:
    #     print(items[0].prettify())



# page = 1
# url = f"https://www.newegg.com/p/pl?d={gpu_input}&N=4131&page={page}"
# webbrowser.open(url)

# chatgpt generead version
items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={gpu_input}&N=4131&page={page}"
    page_content = requests.get(url).text
    soup = BeautifulSoup(page_content, 'html.parser')

    div = soup.find("div", class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
    if not div:
        continue

    items = div.find_all("div", class_="item-cell")

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