from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.common.action_chains import ActionChains

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError as dke

url = 'https://mail.ru/'
client = MongoClient('127.0.0.1', 27017)
db = client['email_parsing']
email_db = db.email


driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url)

mail_input = driver.find_element_by_class_name("email-input")
mail_input.send_keys("study.ai_172")

enter = mail_input.send_keys(Keys.ENTER)

# time.sleep(1)


password_input = driver.find_element_by_class_name("password-input")
time.sleep(1)
password_input.send_keys("NextPassword172???")

# password_input = driver.find_element_by_class_name("password-input")
# password_input.send_keys("NextPassword172???")

enter = password_input.send_keys(Keys.ENTER)

time.sleep(3)
last_element = 0
links_list = []
for _ in range(5):
    links = driver.find_elements(By.XPATH, "//a[contains(@href,'/inbox/')]")
    # print('links', links)

    for el in links:
        link_profile = el.get_attribute('data-id')
        # print('link', link_profile)
        links_list.append(link_profile)
    if last_element == links_list[-1]:
        break
    last_element = links_list[-1]

    actions = ActionChains(driver)
    actions.move_to_element(links[-1])
    # actions.key_down(Keys.LEFT_CONTROL).key_down('c')
    actions.perform()

links_unique = set(links_list)

for message in links_unique:
    full_url = 'https://e.mail.ru/inbox/' + message
    driver.get(full_url)
    button = driver.find_element(By.CLASS_NAME, 'letter-contact')

    # driver.close()