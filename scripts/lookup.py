import sys
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


class Lookup(object):

    def __init__(self):
        self.movie_name = ''
        self.regions = ['ie', 'us', 'au']

    def set_movie_query_spec_regions(self, movie_name, regions):
        self.movie_name = movie_name
        self.regions = regions

    def set_movie_query(self, movie_name):
        self.movie_name = movie_name


    def configure_driver(self):
        '''
        configure webdriver to chrome and make it headless
        '''
        driver_options = Options()
        driver_options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path=os.path.dirname(os.path.realpath(__file__)) + '/geckodriver', firefox_options=driver_options)

        return driver


    def extract_movies_available(self, xml_page_result):
        for movie_title in xml_page_result.select('div.title-list-row'):
            for title_row in movie_title.select('.title-list-row__row'):
                title_selector = 'span.title-list-row__row__title'
                year_selector = 'span.title-list-row__row--muted'
                season_selector = 'div.price-comparison__grid__row__price'
                
                print({
                    'title':title_row.select_one(title_selector).text,
                    'year':title_row.select_one(year_selector).text,
                    # 'seasons':title_row.select_one(season_selector).text if title_row.select_one(season_selector) != None else ''
                })
        print('---------------------------------')

    def check_availability(self):
        search_q = self.movie_name
        ff_browser = self.configure_driver()


        for reg in self.regions:
            print(f'Region: {reg}')

            ff_browser.get(f'https://www.justwatch.com/{reg}/search?providers=nfx&q={search_q}')

            try:
                WebDriverWait(ff_browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'title-list-row')))
            except TimeoutException as e:
                print('Wait Timed out')
                print(e)

            xml_page_result = BeautifulSoup(ff_browser.page_source, "lxml")

            self.extract_movies_available(xml_page_result)

        ff_browser.quit()




