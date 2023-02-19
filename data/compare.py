from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
from categories import TOPICS

chrome_options = Options() 
chrome_options.headless = False
prefs = {"download.default_directory" : os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)


for keyword in TOPICS:

    for year in range(2006, 2019):
        
        driver.get(f"https://trends.google.com/trends/explore?date={year}-01-01%20{year}-12-31&geo=PT&q=%2Fm%2F02mm_")
        driver.refresh()

        el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".add-term-button"))).click()

        time.sleep(0.5)

        actions = ActionChains(driver)
        actions.send_keys(keyword)
        actions.perform()


        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".md-autocomplete-suggestions > li:nth-child(3) > * .autocomplete-title"))).click()

        time.sleep(1.5)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".export"))).click()

        time.sleep(1)

        os.rename(os.path.join(os.getcwd(), "multiTimeline.csv"), os.path.join(os.getcwd(), "raw", f"--{keyword}-{year}.csv"))

        
driver.close()