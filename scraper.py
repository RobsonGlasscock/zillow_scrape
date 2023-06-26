from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
from time import sleep
import random
import os

browser = webdriver.Chrome()

# set path to download all files for Gaylord into a Gaylord folder.
file_path = os.getcwd() + "/Gaylord"

integer_hold = [681]
# for i in range(600, 700, 1):
for i in integer_hold:
    browser.get("https://redfin.com")
    # insert random sleep time for pull
    sleep(random.randint(2, 12))
    # input the address and then the enter key when fed into search box.
    text_str = str(i) + " " + "S Gaylord St Denver CO" + "\n"
    # more random sleep time
    sleep(random.randint(4, 8))
    # find the search box
    userElem = browser.find_element_by_id("search-box-input")
    # feed in the text string with the appended enter key at the end into the box
    userElem.send_keys(text_str)

    # write out each file with the appropriate address.
    file_str = str(i) + " " + "S Gaylord St Denver CO.html"
    with open(file_path + "/" + file_str, "w") as f:
        f.write(browser.page_source)
    # last random sleep
    sleep(random.randint(10, 20))

################
%pwd

# see url
browser.current_url


# set variable qual to current url. 
url_string= browser.current_url
browser.get(url_string)

url_string

import pywebcopy
from pywebcopy import save_webpage


url= url_string
download_folder= %pwd

url
# kwargs= {'bypass_robots':True, 'project_name': 'recognisable-name'}
save_webpage('https://www.redfin.com/CO/Denver/681-S-Gaylord-St-80209/home/34126392')

https://www.redfin.com/CO/Denver/681-S-Gaylord-St-80209/home/34126392

save_webpage(https://www.redfin.com/CO/Denver/681-S-Gaylord-St-80209/home/34126392)


browser.current_url.page_source()
browser.get(browser.current_url).page_source()

browser.page_source
print(browser.page_source)
browser
userElem

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# os.chdir("./tester")


save_me = ActionChains(browser).key_down(Keys.CONTROL)\
         .key_down('s').key_up(Keys.CONTROL).key_up('s')

save_me.perform()

browser.current_url

################


# find the url after entering the address.
browser.current_url

lister = []
lister.append(browser.current_url)

with open("page.html", "w") as f:
    f.write(browser.page_source)

lister


browser.get("https://redfin.com")

userElem = browser.find_element_by_id("search-box-input")

userElem.send_keys("6829 E. Lowry Blvd. Denver CO" + "\n")
browser.current_url

lister.append(browser.current_url)


lister


#####################################
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.DataFrame(data=None, columns=["url"])
df

browser = webdriver.Chrome()
type(browser)
browser.get("https://redfin.com")
browser.implicitly_wait(1)

userElem = browser.find_element_by_id("search-box-input")

# input the address and then the enter key into the search box.
userElem.send_keys("681 S Gaylord St Denver CO" + "\n")

# find the url after entering the address.
browser.current_url

lister = []
lister.append(browser.current_url)

with open("page.html", "w") as f:
    f.write(browser.page_source)

lister


browser.get("https://redfin.com")

userElem = browser.find_element_by_id("search-box-input")

userElem.send_keys("6829 E. Lowry Blvd. Denver CO" + "\n")
browser.current_url

lister.append(browser.current_url)


lister


##############

with open("lawrence_complete.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup


with open("lawrence_single.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup

with open("lawrence_html.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup
