from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pickle
import time
import pyautogui
username=''#user's username
password=''#user's password
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
r=driver.get('https://vtop.vit.ac.in/vtop/initialProcess')
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
ele=driver.find_element_by_link_text('Login to VTOP')
ele.click()
driver.get('https://vtop.vit.ac.in/vtop/vtopLogin')
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
driver.find_element_by_id('uname').send_keys(username)
driver.find_element_by_id('passwd').send_keys(password)
driver.find_element_by_id('captcha').click()
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
time.sleep(3)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
a=driver.find_element_by_id("recaptcha-token")
print(a)
"""
driver.get('https://vtop.vit.ac.in/vtop/doLogin')
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "recaptcha-audio-button"))
    )
except:
    driver.quit()
"""
#time.sleep(2)
#driver.switch_to.frame(1);
#time.sleep(3)
#driver.switch_to.frame('c-hfrmv4ck01mt')
#driver.find_element_by_id('recaptcha-audio-button').click()
try:
    g=driver.find_element_by_link_text('Login to V-TOP')
except:
    print("UNABLE TO LOGIN")
