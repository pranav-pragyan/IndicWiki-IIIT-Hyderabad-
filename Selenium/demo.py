from selenium.webdriver import Chrome, Safari, Edge, Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://pubchem.ncbi.nlm.nih.gov/bioassay/157#section=Data-Table&embed=true"
driver_path = 'Selenium\geckodriver.exe'
browser = Firefox(executable_path=driver_path)

browser.get(url)

# Wait for the page to fully load
browser.implicitly_wait(20)
time.sleep(2)

soup = BeautifulSoup(browser.page_source, 'lxml')

tables = soup.find_all('table')

print(browser.title)
dfs = pd.read_html(str(tables))
print(dfs)
# print(tables)

# browser.close()

# # print(browser)

# # class_name = "over_x_auto"
# id = "root-modal"

# table = browser.find_element(By.ID, id)

# print(table.accessible_name)
