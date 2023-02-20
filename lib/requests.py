import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

def request(search):   
    load_dotenv()
    print(os.environ.get('EMAIL'))
    print(os.environ.get('PASSWORD'))
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
    # peopleButton = driver.find_element(By.LINK_TEXT, 'People')
    # print("people",peopleButton[0])
    peopleButton[0].click()
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    nextPage = driver.find_elements(By.CLASS_NAME,'artdeco-pagination__indicator')
    print('page: ---', nextPage )
    # nextPage[1].click()


    sleep(30)