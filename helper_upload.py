from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import glob
import time
from wproto_creds import *

driver = webdriver.Chrome('./chromedriver')

def login(user, passwd):
    driver.get("https://vm1.wproto.net/admin/home/")
    username = driver.find_element_by_id("login_name")
    password = driver.find_element_by_id("passwd")
    username.send_keys(user)
    password.send_keys(passwd)
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    submit.click()

def upload_plugin(name):
    driver.get("https://vm1.wproto.net/modules/wp-toolkit/index.php/index/plugins")
    upload_plugin = driver.find_element_by_xpath("//button[@data-test-id='toolbar-upload-button']")
    upload_plugin.click()
    driver.find_element_by_xpath("//input[@type='file']").send_keys(os.getcwd()+"/plugins/{}".format(name))
    time.sleep(2)
    ok_button = driver.find_element_by_xpath("//button[@type='button' and @class='pul-button pul-button--lg pul-button--primary pul-button--active']")
    ok_button.click()
    while(True):
        try:
            driver.find_element_by_xpath("//input[@type='file']").is_displayed()
        except:
            break

def upload_driver():
    login(user, passwd)
    name = []
    names = glob.glob("plugins/*.zip")
    for name in names:
        name = name.replace("plugins\\", "")
        print(name)
        upload_plugin(name)