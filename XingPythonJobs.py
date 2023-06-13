from selenium import webdriver
from selenium.webdriver.common.by import By                 # -> find-elemnt(by=By.XPATH)
from selenium.webdriver.common.keys import Keys             # -> send_keys(Keys.ENTER, Keys.ESC)
from selenium.webdriver.support.ui import Select            # -> switch_to_frames | Dropdown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

# options.add_argument("--start-maximized")
options.add_argument("--headless")

exectuable_path = ChromeDriverManager().install()
driver = webdriver.Chrome(options=options, service=ChromeService(exectuable_path))

driver.get(url="https://www.xing.com/jobs/search?keywords=Python%20Developer&location=Alsfeld&remote=1")

# Cookie Conset
try:
    cookie_conset = driver.find_element(By.CSS_SELECTOR, "div.cookie-consent-CookieConsentBannerContent-container-b226d8b9")
    cookie_conset.find_element(By.ID, "consent-accept-button").click()
except:
    pass
  
jobs = driver.find_elements(By.CSS_SELECTOR, "div.list-item-job-teaser-list-item-details-a3cb46c1")
  
for job in jobs:
  descr = job.find_element(By.CSS_SELECTOR, "h3[data-xds='Headline']").text
  cities = job.find_elements(By.CSS_SELECTOR, "p[data-xds='BodyCopy']")
  print(f"{descr} in -> {cities[0].text}")
  print(f"{cities[1].text}\n")
    
