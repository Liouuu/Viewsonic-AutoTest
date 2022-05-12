import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import MVBcom
import test_case


#import image_process
import time

PATH = 'C:/Users/kero/Desktop/python/chromedriver.exe'
driver = webdriver.Chrome(PATH)
account = "roger.ke@viewsonic.com"
password = "#sS3133265"
remote_id = "DavidJie"

driver.get("https://stage.myviewboard.com/signin")
driver.maximize_window()
MVBcom.loginMVBcom(driver,account,password)
MVBcom.enter_classroom(driver)
test_case.test_localdrive(driver)
test_case.test_googledrive(driver)
