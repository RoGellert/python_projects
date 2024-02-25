from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    print("Write the date you want the top from in format YYYY-MM-DD:")

    user_input = ""
    while True:
        user_input = input()

        try:
            user_test = datetime.strptime(user_input, '%Y-%m-%d')
        except ValueError:
            print("Wrong input, please provide a correct one")
            continue

        break

    print(user_input)



