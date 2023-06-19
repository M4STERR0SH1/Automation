import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def open_browser():
    options = Options()
    options.add_argument('--profile-directory=Profile 9')
    options.add_argument('--user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data\\')
    driver = uc.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", options=options)
    driver.implicitly_wait(5)
    return driver


def go_to_page(driver):
    driver.get("https://app.apollo.io/")


def click_on_search(driver):
    search_btn = driver.find_element(By.ID, 'searcher')
    search_btn.click()


def saved_searches(driver):
    saved_search_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/a[2]')
    saved_search_btn.click()


def new_pinned(driver):
    open_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/span/span')
    open_btn.click()
    sleep(2)
    net_new_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/a[2]')
    net_new_btn.click()


def box(driver):
    sleep(2)
    dropdown_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[1]')
    dropdown_btn.click()


def select(driver):
    sleep(2)
    select_btn = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/a[1]')
    select_btn.click()


def save(driver):
    save_btn = driver.find_element(By.ID, "lists")
    save_btn.click()
    list_btn = driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/a[1]')
    list_btn.click()


def enter_det(driver, list_name):
    sleep(2)
    list_field = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[2]/form/div/div/div/div/div/div/div')
    list_field.click()
    action_chains = ActionChains(driver)
    action_chains.send_keys_to_element(list_field, list_name).perform()
    apply_btn = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div/div/div[3]/button/div')
    apply_btn.click()


def refresh(driver):
    sleep(5)
    refresh_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]')
    refresh_btn.click()


if __name__ == '__main__':
    driver = open_browser()
    go_to_page(driver)
    click_on_search(driver)
    saved_searches(driver)
    new_pinned(driver)

    while True:
        box(driver)
        select(driver)
        save(driver)
        list_name = "try"
        enter_det(driver, list_name)
        refresh(driver)
