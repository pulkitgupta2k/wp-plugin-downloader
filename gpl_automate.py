from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from gpl_creds import *
import time

def login(user, passwd, driver):
    driver.get("https://wproto.net/wp-admin/")
    username = driver.find_element_by_id("user_login")
    password = driver.find_element_by_id("user_pass")
    username.send_keys(user)
    password.send_keys(passwd)
    submit = driver.find_element_by_xpath("//input[@type='submit']")
    submit.click()

def clicker(driver):
    plugins = "https://wproto.net/wp-admin/admin.php?page=gplberg-plugin-manager"
    themes = "https://wproto.net/wp-admin/admin.php?page=gplberg-theme-manager"
    
    #plugins
    driver.get(plugins)
    install_buttons = driver.find_elements_by_xpath("//button[@type='submit' and @value='Install']")
    for install_button in install_buttons:
        try:
            install_button.click()
            time.sleep(5)
        except:
            try:
                if not install_button.is_displayed():
                    next_button = driver.find_element_by_xpath("//button[@data-page='next']")
                    next_button.click()
                time.sleep(1)
                install_button.click()
            except:
                pass
    
    #themes
    driver.get(themes)
    install_buttons = driver.find_elements_by_xpath("//button[@type='submit' and @value='Install']")
    time.sleep(5)
    for install_button in install_buttons:
        try:
            hover = ActionChains(driver).move_to_element(install_button)
            hover.perform()
            install_button.click()
            time.sleep(5)
        except:
            try:
                if not install_button.is_displayed():
                    next_button = driver.find_element_by_xpath("//button[@data-page='next']")
                    next_button.click()
                time.sleep(1)
                hover = ActionChains(driver).move_to_element(install_button)
                hover.perform()
                install_button.click()
            except:
                pass


def driver():
    driver = webdriver.Chrome('./chromedriver')
    login(berg_username, berg_password, driver)
    clicker(driver)

if __name__ == "__main__":
    driver()