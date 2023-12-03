import selenium
from selenium import webdriver
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
    driver.execute_script("window.scrollTo(0, 1000);")







