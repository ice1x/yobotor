import os
import sys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

VISITS = sys.argv[1]
LINKS = sys.argv[2]
MIN_WATCH = sys.argv[3]
MAX_WATCH = sys.argv[4]
TOR_BIN = "/Applications/TorBrowser.app/Contents/MacOS/firefox"

# os.system(TOR_BIN)

# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None


def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser

def get_uri(uri):
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print "getting", url_name, "at", url
        browser.get(url)



if __name__ == "__main__":
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print "getting", url_name, "at", url
        browser.get(url)
