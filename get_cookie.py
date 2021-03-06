from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from gpl_creds import *
from pprint import pprint
import itertools


def cookie_driver():
    driver = webdriver.Chrome('./chromedriver')
    link = "https://www.gplfamily.com/my-account/"
    driver.get(link)
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element_by_xpath(
        "//*[@id='main']/div[2]/div/div/div[2]/div/form/p[3]/button").click()
    cookies = driver.get_cookies()
    ret_cookie = ""
    for cookie in cookies:
        try:
            name = cookie['name']
            value = cookie['value']
            ret_cookie = ret_cookie + "{}={}; ".format(name, value)
        except:
            pass
    ret_cookie = ret_cookie[:-2]
    # print(ret_cookie)
    # print(type(ret_cookie))
    with open("cookie_gpl.txt", "w") as f:
        f.write(ret_cookie)
    driver.quit()


if __name__ == "__main__":
    cookie_driver()
