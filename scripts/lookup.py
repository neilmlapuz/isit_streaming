import sys
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Lookup(object):
    movie_name = ''

    def __init__(self, movie_name):
        self.movie_name = movie_name


    def check_availability(self):
        self.request_site()


    def request_site(self):
        search_q = self.movie_name
        region = 'ie'
        chrome_browser = webdriver.Chrome('/Users/adminy/Downloads/chromedriver')
        chrome_browser.get('https://www.justwatch.com/'+ region +'/search?providers=nfx&q='+search_q)

        try:
            WebDriverWait(chrome_browser, 30).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'navbar__search')))
        except TimeoutException as e:
            print('Wait Timed out')
            print(e)

        # movies = chrome_browser.find_element_by_class_name('title-list-row')

        print(chrome_browser.page_source)

        movies = [movie.text for movie in chrome_browser.find_elements_by_class_name('title-list-row__row')]
        print(movies)

        time.sleep(30)










