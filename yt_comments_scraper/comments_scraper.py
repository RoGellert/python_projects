from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import date
from dateutil.relativedelta import relativedelta


def determine_approximate_date(date_text: str, today_date: date) -> str:
    """
    Function to approximately calculate day at which the comment was written
    (based on the label in YouTube comments (i.e '3 month ago'))

    date_text: text of the label
    today_date: today's date estimated by date.today()
    returns date in date format
    """
    comment_approximate_date = ''

    # calculate approximate date based on the value of the input string
    if re.search('year', date_text):
        comment_approximate_date = today_date - relativedelta(years=int(date_text[0:2].strip()))

    elif re.search('month', date_text):
        comment_approximate_date = today_date - relativedelta(months=int(date_text[0:2].strip()))

    elif re.search('week', date_text):
        comment_approximate_date = today_date - relativedelta(weeks=int(date_text[0:2].strip()))

    elif re.search('day', date_text):
        comment_approximate_date = today_date - relativedelta(days=int(date_text[0:2].strip()))

    elif re.search('yesterday', date_text):
        comment_approximate_date = today_date - relativedelta(days=1)

    elif re.search('minute', date_text):
        comment_approximate_date = today_date

    return comment_approximate_date


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
    date_today = date.today()
    for comment in comments:
        comment_to_append = []

        content = BeautifulSoup(comment.get_attribute('innerHTML'), 'html.parser')
        lines = content.find_all("yt-formatted-string", {"id": "content-text"})

        likes = content.find("span", {"id": "vote-count-middle"})
        likes = likes.text.replace(" ", "").replace("\n", "")
        likes = int(likes) if likes[-1] != 'K' else int(float(likes[0:-1]))*1000
        time_posted = content.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"}).text
        time_posted = determine_approximate_date(time_posted, date_today)

        text = lines[0].text.replace("\n", "").strip()
        comments_list.append([text, likes, time_posted])

    df_to_save = pd.DataFrame(comments_list)
    print(df_to_save)
    print(df_to_save[2].unique())
    df_to_save.to_csv('csv_file.csv', index=False, header=['comment', 'number of likes', 'approximate_time_posted'])
