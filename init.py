from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time
from userlogin import userLogin, userLoginIdirect
from search import searchFunc, auctionHouseClick, auctionHouseSearch, unselect_AH, open_dropdownbox, sorted_auction_search
from results import expandVehicleInfoIdirect, retrieveInfoUpd, retrieveInfoDetail, expandButton, waitLoader
from utils import printList, destructure, printDict, errorCheckUpd, createDirectory
from traversePage import nextResults
from dataScraping import getAllInfo
from bs4_searchTags import bs4_search_elements, destruct_basic, destruct_adv

url = "http://www.ibcjapan.co.jp/"
home_driver = r"E:\personal\program\chromedriver"
firefox_driver = r"E:\personal\program\geckodriver"

username = "glabadia"
passcode = "Optiplex3050!"

# driver = webdriver.Firefox(executable_path=firefox_driver)
# driver = webdriver.Chrome(executable_path=home_driver)
# driver = webdriver.Chrome(executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Chrome\chromedriver")
driver = webdriver.Firefox(
    executable_path=r"C:\Users\glabadia\Desktop\VS\selenium drivers\Firefox\geckodriver")
driver.get(url)

###
# Main Process
###

# userLogin(username, passcode, driver)

userLoginIdirect(username, passcode, driver)

# open_dropdownbox(driver)
# a = auctionHouseSearch(driver)
# auctionHouseClick(driver, a)
# unselect_AH(driver)
# conditionGrade()

searchFunc(driver)  # Search Button

expandVehicleInfoIdirect(driver)
sleep(20)

# bs4_search_elements(driver)
print(destruct_basic(driver))
print(destruct_adv(driver))


# isLoader = waitLoader(driver)
# expand = False
# while not expand:
#     expand = expandButton(driver)

# sleep(5)

# upd = retrieveInfoUpd(driver)
# print(len(upd))

# detail = retrieveInfoDetail(driver)
# printDict(detail)

# nextResults(driver)  # Normal Traverse


def one_AH_search(driver):
    searchFunc(driver)
    nextResults(driver)


def sorted_AH_search(driver):
    #   open dropdownbox
    #   retrieve all auction house info
    #   sort all auction houses ascending order
    #
    createDirectory()

    open_dropdownbox(driver)
    not_first_run = False
    sorted_ah_list, web_element = sorted_auction_search(driver)
    for auction_house in sorted_ah_list:
        sleep(10)
        if not_first_run:
            open_dropdownbox(driver)
            unselect_AH(driver)
        print(f"Now searching for: {auction_house}...")
        web_element[auction_house].click()
        one_AH_search(driver)
        print(f"Finished searching for: {auction_house}...")
        not_first_run = True


# one_AH_search(driver)
# sorted_AH_search(driver)
