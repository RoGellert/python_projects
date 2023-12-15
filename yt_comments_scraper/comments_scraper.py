from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'

    driver = webdriver.Chrome()
    actions = ActionChains(driver)

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    element = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope '
                                            'ytd-consent-bump-v2-lightbox"])[3]')
    actions.click(element).perform()

    driver.refresh()

    element = driver.find_element(By.XPATH, '//video')
    actions.move_to_element(to_element=element).perform()

    element = driver.find_element(By.XPATH, '//button[@aria-keyshortcuts="k"]')
    actions.click(element).perform()
    driver.implicitly_wait(10)

    actions.scroll_by_amount(0, 1000).perform()
    for i in range(200):
        actions.scroll_by_amount(0, 2000).perform()
        driver.implicitly_wait(1)
    driver.implicitly_wait(15)

    comments = driver.find_elements(By.XPATH, '//div[@id="comment-content"]')
    comments_list = []
    for comment in comments:
        comment_to_append = []
        content = BeautifulSoup(comment.get_attribute('innerHTML'), 'html.parser')
        lines = content.find_all("span", {"class": "style-scope yt-formatted-string"})
        for line in lines:
            if line.text != '\n':
                comment_to_append.append(line.text)
        if comment_to_append:
            comments_list.append(comment_to_append)

    for i in comments_list:
        print(i)
