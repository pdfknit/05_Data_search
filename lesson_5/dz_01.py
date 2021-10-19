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

password_input = driver.find_element_by_class_name("password-input")
time.sleep(1)
password_input.send_keys("NextPassword172???")

enter = password_input.send_keys(Keys.ENTER)

time.sleep(3)
last_element = 0
links_list = []

while True:
    links = driver.find_elements(By.XPATH, "//a[contains(@href,'/inbox/')]")

    for el in links:
        link_profile = el.get_attribute('data-id')
        links_list.append(link_profile)

    if last_element == links_list[-1]:
        break

    last_element = links_list[-1]
    actions = ActionChains(driver)
    actions.move_to_element(links[-1])

    actions.perform()

links_unique = set(links_list[1::])
links_unique.remove(None)

for message in links_unique:
    print(message)
    current_letter = {}
    full_url = 'https://e.mail.ru/inbox/' + message
    driver.get(full_url)
    wait = WebDriverWait(driver, 10)

    letter_email = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'letter-contact')))
    letter_email = letter_email.get_attribute('title')
    letter_date = driver.find_element(By.CLASS_NAME, "letter__date").text
    letter_head = driver.find_element(By.XPATH, "//h2[contains(@class,'thread__subject')]").text
    letter_body = driver.find_element(By.XPATH, "//div[contains(@class,'js-helper js-readmsg-msg')]").text

    current_letter["letter_email"] = letter_email
    current_letter["letter_date"] = letter_date
    current_letter["letter_head"] = letter_head
    current_letter["letter_body"] = letter_body

    try:
        email_db.insert_one(current_letter)
    except dke:
        print('Document already exist')

    driver.close()
