from subprocess import check_output
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import MVBcom
import test_case
import func
import time

driver = webdriver.Chrome()
account = "roger.ke@viewsonic.com"
password = "#sS3133265"

driver.get("https://stage.myviewboard.com/signin")
driver.maximize_window()

MVBcom.loginMVBcom(driver,account,password)
MVBcom.enter_classroom(driver)

test_case.test_image_search(driver)
test_case.clips_test(driver)
test_case.test_youtube_search(driver)