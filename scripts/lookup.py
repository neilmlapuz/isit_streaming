import sys
from mechanicalsoup import StatefulBrowser

class Lookup(object):
    movie_name = ''

    def __init__(self, movie_name):
        self.movie_name = movie_name


    def check_availability(self):
        
        print('>>',self.movie_name)
        self.request_site()


    def request_site(self):
        print('reached')
        browser = StatefulBrowser()
        browser.open("https://www.justwatch.com/")
        # browser.select_form('#search_form_homepage')
        # browser['q'] = 'spiderman'
        # browser.submit_selected()

        print(browser.get_current_page())




