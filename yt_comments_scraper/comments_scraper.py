import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4 as soup
import time


url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'
chromedriver_folder = '/chromedriver.exe'


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    #confirmation = driver.find_element(By.XPATH, '//div[@class="eom-button-row style-scope '
                      #                           'ytd-consent-bump-v2-lightbox"]')
    #confirmation.click()

    confirmation = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope ytd-consent-bump-v2-lightbox"])[3]')
    confirmation.click()












