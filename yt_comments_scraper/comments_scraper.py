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

    element = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope ytd-consent-bump-v2-lightbox"])[3]')
    actions.click(element).perform()

    driver.refresh()

    element = driver.find_element(By.XPATH, '//video')
    actions.move_to_element(to_element=element).perform()

    element = driver.find_element(By.XPATH, '//button[@aria-keyshortcuts="k"]')
    actions.click(element).perform()
    driver.implicitly_wait(10)

    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)
    actions.scroll_by_amount(0, 1000).perform()
    driver.implicitly_wait(6)

    #comments = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="content-text" and @slot="content"]')
    comments = driver.find_elements(By.XPATH, '//ytd-comment-renderer[@id="comment"]')
    comments_data1 = comments[0].get_attribute('innerHTML')
    comments_data2 = comments[1].get_attribute('innerHTML')
    print(BeautifulSoup(comments_data1, 'html.parser').find_all("span", {"class": "style-scope yt-formatted-string"}))
    #print(comments_data2)

    comments_list = []
    for comment in comments:
        comment_to_append = ""
        for line in BeautifulSoup(comment.get_attribute('innerHTML'), 'html.parser').find_all("span", {"class": "style-scope yt-formatted-string"}):
            comment_to_append += line.text + '\n'
        comments_list.append(comment_to_append)

    print(comments_list)


    #comments_data_soup = BeautifulSoup(comments_data, 'html.parser')
    #print(comments_data_soup)
    #comments_data_soup.find("yt-formatted-string", {"id": "content-text"})
