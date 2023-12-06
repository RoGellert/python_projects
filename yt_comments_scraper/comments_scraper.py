import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.implicitly_wait(13)

    #confirmation = driver.find_element(By.XPATH, '//div[@class="eom-button-row style-scope '
                      #                           'ytd-consent-bump-v2-lightbox"]')
    #confirmation.click()

    actions = ActionChains(driver)

    element = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope ytd-consent-bump-v2-lightbox"])[3]')
    actions.click(element).perform()

    driver.refresh()

    element = driver.find_element(By.XPATH,'//video')
    actions.move_to_element(to_element=element).perform()

    element = driver.find_element(By.XPATH,'//button[@aria-keyshortcuts="k"]')
    actions.click(element).perform()

    actions.scroll_by_amount(0, 1000).perform()
    actions.scroll_by_amount(0, 100000).perform()













