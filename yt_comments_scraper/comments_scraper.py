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
    driver.implicitly_wait(10)

    driver.get(url)
    driver.maximize_window()

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #confirmation = driver.find_element(By.XPATH, "yt-spec-touch-feedback-shape__fill")
    #confirmation.click()







