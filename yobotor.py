import os
import sys
from selenium.webdriver.firefox.firefox_BINARY import FirefoxBINARY
from selenium import webdriver
from random import randrange
from time import sleep


# path to the firefox BINARY inside the Tor package
BINARY = '/Applications/TorBrowser.app/Contents/MacOS/firefox'

VISITS = sys.argv[1]
LINKS = sys.argv[2]
MIN_WATCH = int(sys.argv[3])
MAX_WATCH = int(sys.argv[4])


# read file with links
with open(os.path.abspath(LINKS)) as f:
    links = f.readlines()
# remove whitespace characters like `\n` at the end of each line
links = [x.strip() for x in links]
print links

if os.path.exists(BINARY) is False:
    raise ValueError("The BINARY path to Tor firefox does not exist.")
firefox_BINARY = FirefoxBINARY(BINARY)

browser = None


def get_random_timeout():
    return randrange(MIN_WATCH, MAX_WATCH)


def get_browser(BINARY=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_BINARY=BINARY)
    return browser


def get_uri(uri):
    timeout = get_random_timeout()
    print uri
    print "Timeout: %i" % timeout
    browser = get_browser(BINARY=firefox_BINARY)
    browser.get(uri)

    sleep(timeout)
    print "getting", 'ip checker', "at"
    browser.get('http://icanhazip.com')
    sleep(3)
    browser.close()

if __name__ == "__main__":
    counter = 0
    while counter < VISITS:
        for uri in links:
            counter += 1
            get_uri(uri)
