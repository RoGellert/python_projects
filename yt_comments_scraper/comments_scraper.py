import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'
chromedriver_folder = '/chromedriver.exe'


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    actions = ActionChains(driver)

    driver.get(url)
    driver.implicitly_wait(13)

    element = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope ytd-consent-bump-v2-lightbox"])[3]')
    actions.click(element).perform()

    driver.refresh()

    element = driver.find_element(By.XPATH, '//video')
    actions.move_to_element(to_element=element).perform()

    element = driver.find_element(By.XPATH, '//button[@aria-keyshortcuts="k"]')
    actions.click(element).perform()

    actions.scroll_by_amount(0, 800).perform()

    comments = driver.find_element(By.XPATH, '//*[@id="comments"]')
    comments_data = comments.get_attribute('innerHTML')

    comments = BeautifulSoup(comments_data, 'html.parser')
    print(comments)
