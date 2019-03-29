# conding: utf-8

import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

import jinchutou_mimetype

starter = 87205919

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/root/jinchutou-download')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', jinchutou_mimetype.jinchutou_mimetype)

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

# driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver = webdriver.Firefox(firefox_profile=profile)
driver.implicitly_wait(30)

driver.get("https://www.jinchutou.com/")
driver.find_element_by_link_text(u"[登录]").click()
driver.find_element_by_id("Content_txtUserName").click()
driver.find_element_by_id("Content_txtUserName").clear()
driver.find_element_by_id("Content_txtUserName").send_keys("USERNAME")
driver.find_element_by_id("Content_txtPassword").click()
driver.find_element_by_id("Content_txtPassword").clear()
driver.find_element_by_id("Content_txtPassword").send_keys("PASSWORD")
driver.find_element_by_id("Content_autologin").click()
driver.find_element_by_id("Content_btnLogin").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上传文档赚钱'])[1]/following::div[4]").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文学/艺术/历史'])[2]/following::nobr[1]").click()
# driver.find_element_by_link_text(u"长相思第一部...").click()
# time.sleep(3)
# handles = driver.window_handles
# driver.switch_to.window(handles[-1])
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='下载费用：'])[1]/following::input[1]").click()
while True:
    try:
        download_url = "https://www.jinchutou.com/d-" + str(starter) + ".html"
        driver.get(download_url)
        time.sleep(1)
        driver.find_element_by_id("Content_btnModify").click()
    except Exception as e:
        print(e)
        pass
    finally:        
        if starter > 1:
            starter = starter -1
        else:
            break

driver.close()
driver.quit()
