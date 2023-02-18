from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

chrome_options = Options() 
chrome_options.headless = False
prefs = {"download.default_directory" : os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

TOPICS = [
    # "automotive industry",
    # "auto insurance",
    # "second hand car",
    # "mobile phone",
    # "mercedes benz",
    # "electrical appliance",
    # "wifi",
    # "clothing",
    # "shoes",
    # "underwear",
    # "electricity",
    # "energy",
    # "gasoline",
    # "tobacco",
    # "video game",
    # "t-shirt",
    # "natural gas",
    # "health care",
    # "furniture",
    # "interior design",
    # "ebook",
    # "novel",
    # "footwear",
    # "lingerie",
    # "real estate",
    # "life insurance",
    # "dessert",
    # "potato",
    # "coffee",
    # "bottled water",
    # "margarine",
    # "offal",
    # "juice",
    # "jam",
    # "veterinarians",
    # "amusement park",
    # "television",
    # "hairdresser",
    # "timber",
    # "travel agency",
    # "nightclub",
    # "fur",
    # "vitamins",
    "petroleum",
    "beer",
    "lawyer",
    "renovation",
    "restaurant"
]


for keyword in TOPICS:

    for year in range(2006, 2019):
        
        driver.get(f"https://trends.google.com/trends/explore?date={year}-01-01%20{year}-12-31&geo=PT")
        driver.refresh()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-30"))).send_keys(keyword)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".md-autocomplete-suggestions > li:nth-child(2) > * .autocomplete-title"))).click()

        time.sleep(1.5)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".export"))).click()

        time.sleep(1)

        os.rename(os.path.join(os.getcwd(), "multiTimeline.csv"), os.path.join(os.getcwd(), "raw", f"{keyword}-{year}.csv"))

        
driver.close()