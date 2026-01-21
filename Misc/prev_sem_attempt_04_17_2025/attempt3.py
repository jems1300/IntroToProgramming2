import pip
from bs4 import BeautifulSoup
import re
import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Webdriver is what's responsible for most actions

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

search = input("Search: ")

driver = webdriver.Chrome()
url = f"https://www.newegg.com/p/pl?d={search}&N=4131"
driver.get(url)
time.sleep(5)
# title = driver.title
# print(title)
find_page = driver.find_element(By.CLASS_NAME, "list-tool-pagination-text")

page_num = int(str(find_page.text.split("/")[1]))

print(f"There are {page_num} page results for the {search}")
# driver.close()

for page_num in range(1, page_num, +1):
    driver.get(url)
    find_cell = driver.find_element(By.CSS_SELECTOR, ".item-cells-wrap.border-cells.short-video-box.items-list-view.is-list")
    if not find_cell:
        continue

    find_item = driver.find_elements(By.CSS_SELECTOR, ".item_cell")
    print(find_item)


