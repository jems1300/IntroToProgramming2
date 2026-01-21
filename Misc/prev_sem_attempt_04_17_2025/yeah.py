from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  # Or Firefox, Edge, etc.
driver.get("https://www.newegg.com/p/pl?d=rx+9070")

# Optional: Wait for page to fully load
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

pagination = soup.find(class_="list-tool-pagination-text")
print(pagination.strong.text if pagination else "Pagination not found")

driver.quit()