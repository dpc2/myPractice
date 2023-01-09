#------------------------------------------------#
#         Ch. 20 - Bringing It All Together      #
#------------------------------------------------#

import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    # __init__ method takes a website to scrape
    # from as a parameter.
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # urlopen() makes a request and returns
        # a Response object. read() is used to
        # return the HTML from the Return object.
        r = urllib.request.urlopen(self.site)
        html = r.read()

        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)

        # find_all returns an interable containing
        # the tag objects it found
        for tag in sp.find_all('a'):
            # We get the 'href' tags by calling
            # the get method and passing 'href'
            url = tag.get('href')
            if url is None:
                continue
            if 'html' in url:
                print('\n' + url)


news = 'https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'
print(Scraper(news).scrape())

