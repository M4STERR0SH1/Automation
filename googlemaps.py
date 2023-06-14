from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--profile-directory= ---')
options.add_argument('--user-data-dir= ---')
driver = uc.Chrome(executable_path="---", options=options)
driver.get("https://www.google.co.in/maps/")
sleep(2)


def searchplace():
    Place = driver.find_element(By.ID, "searchboxinput")
    Place.send_keys("Udaipur")
    Submit = driver.find_element(By.ID, "searchbox-searchbutton")
    Submit.click()

searchplace()

def directions():
    sleep(2)
    directions = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
    directions.click()

directions()

def find():
    sleep(1)
    wait = WebDriverWait(driver, 5)
    find_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")))
    find_input.send_keys("Jodhpur")
    find_input.send_keys(Keys.ENTER)
    sleep(1)

find()

def kilometers():
    sleep(1)
    Totalkilometers = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(1)
    Bus = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button/div[1]")
    print("Bus Travel:", Bus.text)
    sleep(7)

kilometers()
