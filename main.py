from bs4 import BeautifulSoup

import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "http://www.naver.com"
NAVER_SEARCH = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="

print("검색어:", end=" ")
query = input()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(NAVER_SEARCH + query)

try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "main_pack"))
    )
    print(element)
finally:
    driver.quit()