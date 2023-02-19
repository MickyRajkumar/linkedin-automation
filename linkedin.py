from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

email = input('userName or email: ')
passwd = input('password: ')
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("--window-size=1920x1080")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get('https://www.linkedin.com/')
driver.implicitly_wait(15)
userName = driver.find_element(By.ID,'session_key')
userName.send_keys(email)
password = driver.find_element(By.ID,'session_password')
password.send_keys(passwd)
signIn = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button')
signIn.click()
driver.implicitly_wait(15)
network = driver.find_element(By.LINK_TEXT, 'My Network')
network.click()


sleep(10)

