from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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

        for line in lines:
            line_text = line.text.replace("\n", " ")
            line_text.replace("    ", " ")
            line_text.replace("   ", " ")
            line_text.replace("  ", " ")
            comment_to_append.append(line_text)
        comments_list.append([comment_to_append, likes])

    for i in comments_list:
        print(i)

    print(type(comments_list[0][0]))
