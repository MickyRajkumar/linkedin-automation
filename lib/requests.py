import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def request(search):   
    load_dotenv()
    # email = input('userName or email: ')
    # passwd = input('password: ')
    email = os.environ.get('EMAIL')
    passwd = os.environ.get("PASSWORD")
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.linkedin.com/')
    driver.implicitly_wait(15)
    wait = WebDriverWait(driver, 30)

    userName = driver.find_element(By.ID,'session_key')
    userName.send_keys(email)
    password = driver.find_element(By.ID,'session_password')
    password.send_keys(passwd)
    signIn = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button')
    signIn.click()
    driver.implicitly_wait(10)
    # network = driver.find_element(By.LINK_TEXT, 'My Network')
    # network.click()
    searchPeople = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
    searchPeople.send_keys(search)
    searchPeople.send_keys(Keys.ENTER)

    peopleButton = driver.find_elements(By.CLASS_NAME,'artdeco-pill')
    # # print("people",peopleButton[0])
    peopleButton[0].click()
    driver.implicitly_wait(10)
    # wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "entity-result__item")))
    # connectButton = driver.find_element(By.XPATH("//button[text()='Connect']"))
    connect = driver.find_elements(By.TAG_NAME, "button")
    print('----------',len(connect))
    # print('-------------',connectButton)

    footer = driver.find_element(By.TAG_NAME, "footer")
    delta_y = int(footer.rect['y'])
    ActionChains(driver)\
        .scroll_by_amount(0, delta_y)\
        .perform()
    driver.implicitly_wait(5)
    nextPage = driver.find_elements(By.CLASS_NAME,'artdeco-pagination__button--next')
    print('page: ---', len(nextPage ))
    nextPage[0].click()


    sleep(30)