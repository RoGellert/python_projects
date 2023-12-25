import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import date
from dateutil.relativedelta import relativedelta


class Scraper:
    def __init__(self, url: str) -> None:
        # url of a video to scrape the comments from
        self.url = url

        # list to store the scraped data
        self.data = []

        # today's date to estimate approximate date of the comment (in determine_approximate_date function)
        self.today_date = date.today()

    @staticmethod
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

    def scrape(self, range_of_scrolling: int) -> None:
        """
        Function to scrape the data and save in 'self.data' as a list

        range_of_scrolling: number of times to scroll down in the comments section to load the comments
        (essentially positively proportional to the number of comments scraped)
        """
        # reassign an empty list to store data to avoid duplicated comments (in case it's non-empty)
        self.data = []

        # instantiate selenium driver (in this case Google Chrome)
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en-US")
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)

        # open the browser getting the url, maximize window and let it load for a while
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # accept the cookies consent window
        element = driver.find_element(By.XPATH, '(//ytd-button-renderer[@class="style-scope '
                                                'ytd-consent-bump-v2-lightbox"])[3]')
        actions.click(element).perform()

        # refresh the page for selenium parse the html properly
        driver.refresh()

        # click to pause video (sometimes for some reason doesn't work, probably due to ads sometimes popping)
        element = driver.find_element(By.XPATH, '//video')
        actions.move_to_element(to_element=element).perform()
        element = driver.find_element(By.XPATH, '//button[@aria-keyshortcuts="k"]')
        actions.click(element).perform()
        driver.implicitly_wait(10)

        # due to the fact comments load after scrolling to them on the web page, scroll as much as needed to load them
        # range_of_scrolling is the integer value to determine how many times engine will scroll down 5000 pixels
        actions.scroll_by_amount(0, 1000).perform()
        driver.implicitly_wait(5)
        for i in range(range_of_scrolling):
            actions.scroll_by_amount(0, 5000).perform()
            driver.implicitly_wait(5)
        driver.implicitly_wait(15)

        # parse html
        comments = driver.find_elements(By.XPATH, '//ytd-comment-renderer[@id="comment"]')
        for comment in comments:
            content = BeautifulSoup(comment.get_attribute('innerHTML'), 'html.parser')

            # find and process the text of the comments
            lines = content.find_all("yt-formatted-string", {"id": "content-text"})
            text = lines[0].text.replace("\n", "").strip()

            # find and process the integer representing number of likes
            likes = content.find("span", {"id": "vote-count-middle"})
            likes = likes.text.replace(" ", "").replace("\n", "")
            likes = int(likes) if likes[-1] != 'K' else int(float(likes[0:-1])) * 1000

            # find and process the string representing time posted
            time_posted = content.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"}).text
            time_posted = self.determine_approximate_date(time_posted, self.today_date)

            self.data.append([text, likes, time_posted])

        return

    def save_data(self, save_type: str, save_file_name: str) -> None:
        """
        Funtion to save data from 'self.data' as either csv of json
        """
        df_to_save = pd.DataFrame(self.data)

        # save based on desired in the input save type
        if save_type == 'csv':
            df_to_save.to_csv(f'{save_file_name}.csv',
                              index=False, header=['comment', 'number of likes', 'approximate_time_posted'])
        elif save_type == 'json':
            df_to_save.to_json(f'{save_file_name}.json', orient="split")
        else:
            raise TypeError("Invalid save type (can be either csv or json)")

        return


if __name__ == '__main__':
    # parse arguments provided in the cli
    video_url = sys.argv[1]
    times_to_scroll_down = int(sys.argv[2])
    save_as = sys.argv[3]
    file_name = sys.argv[4]

    # instantiating the Scraper class
    scraper = Scraper(video_url)

    # scraping the data
    scraper.scrape(times_to_scroll_down)

    # saving the data
    scraper.save_data(save_as, file_name)
