from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=O5BJVO3PDeQ&t=2414s'

    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en-US")
    driver = webdriver.Chrome(options=options)
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
    driver.implicitly_wait(5)
    for i in range(100):
        actions.scroll_by_amount(0, 2000).perform()
        driver.implicitly_wait(5)
    driver.implicitly_wait(15)

    comments = driver.find_elements(By.XPATH, '//ytd-comment-renderer[@id="comment"]')
    comments_list = []
    for comment in comments:
        comment_to_append = []

        content = BeautifulSoup(comment.get_attribute('innerHTML'), 'html.parser')
        lines = content.find_all("yt-formatted-string", {"id": "content-text"})

        likes = content.find("span", {"id": "vote-count-middle"})
        likes = likes.text.replace(" ", "").replace("\n", "")
        likes = int(likes) if likes[-1] != 'K' else int(float(likes[0:-1]))*1000

        text = lines[0].text.replace("\n", "").strip()
        comments_list.append([text, likes])

    for i in comments_list:
        print(i)

    with open('./csv_file.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(comments_list)
        file.close()
