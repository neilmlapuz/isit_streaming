import sys
import time
import selenium
from selenium import webdriver

class Lookup(object):
    movie_name = ''

    def __init__(self, movie_name):
        self.movie_name = movie_name


    def check_availability(self):
        
        print('>>',self.movie_name)
        self.request_site()


    def set_chrome_browser(self):
        driver = webdriver.Chrome('/Users/adminy/Downloads/chromedriver')
        driver.get('http://www.google.com/')
        time.sleep(20)
        driver.quit()



    def request_site(self):
        print('reached')

        self.set_chrome_browser()





