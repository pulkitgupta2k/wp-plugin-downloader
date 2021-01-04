from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import glob
import time
from wproto_creds import *
import shutil


def login(user, passwd, driver, site):
    driver.get(f"https://{site}/admin/home/")
    username = driver.find_element_by_id("login_name")
    password = driver.find_element_by_id("passwd")
    username.send_keys(user)
    password.send_keys(passwd)
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    submit.click()


def upload_plugin(name, driver, site):
    driver.get(f"https://{site}/modules/wp-toolkit/index.php/index/plugins")
    upload_plugin = driver.find_element_by_xpath(
        "//button[@data-test-id='toolbar-upload-button']")
    upload_plugin.click()
    driver.find_element_by_xpath(
        "//input[@type='file']").send_keys(os.getcwd()+"/plugins/{}".format(name))
    time.sleep(2)
    ok_button = driver.find_element_by_xpath(
        "//button[@type='button' and @class='pul-button pul-button--lg pul-button--primary pul-button--active']")
    ok_button.click()
    while(True):
        try:
            driver.find_element_by_xpath(
                "//input[@type='file']").is_displayed()
        except:
            break
        try:
            driver.find_element_by_xpath(
                "//span[@class='pul-form-field__error']")
            shutil.move("plugins/{}".format(name),
                        "rejected_plugins/{}".format(name))
            break
        except:
            pass


def upload_theme(name, driver, site):
    driver.get(f"https://{site}/modules/wp-toolkit/index.php/index/themes")
    time.sleep(2)
    upload_plugin = driver.find_element_by_xpath(
        "//button[@data-test-id='toolbar-upload-button']")
    upload_plugin.click()
    driver.find_element_by_xpath(
        "//input[@type='file']").send_keys(os.getcwd()+"/themes/{}".format(name))
    time.sleep(2)
    ok_button = driver.find_element_by_xpath(
        "//button[@type='button' and @class='pul-button pul-button--lg pul-button--primary pul-button--active']")
    ok_button.click()
    while(True):
        try:
            driver.find_element_by_xpath(
                "//input[@type='file']").is_displayed()
        except:
            break
        try:
            driver.find_element_by_xpath(
                "//span[@class='pul-form-field__error']")
            shutil.move("themes/{}".format(name),
                        "rejected_themes/{}".format(name))
            break
        except:
            pass


def upload_driver():
    for site, cred in sites.items():
        driver = webdriver.Chrome('./chromedriver')
        login(cred["user"], cred["passwd"], driver, site)
        name = []
        names = glob.glob("plugins/*.zip")
        for name in names:
            name = name.replace("plugins\\", "")
            print(name)
            upload_plugin(name, driver, site)


def upload_driver_themes():
    for site, cred in sites.items():
        driver = webdriver.Chrome('./chromedriver')
        login(cred["user"], cred["passwd"], driver, site)
        name = []
        names = glob.glob("themes/*.zip")
        for name in names:
            name = name.replace("themes\\", "")
            print(name)
            upload_theme(name, driver, site)

# upload_theme("5sec-snow.zip", driver)
