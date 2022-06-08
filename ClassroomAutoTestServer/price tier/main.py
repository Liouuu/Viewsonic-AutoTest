from subprocess import check_output
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import MVBcom
import test_case
import time
import get_time
import export_table
# options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(ChromeDriverManager().install())
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
account = "kim.viewsonic@gmail.com"
password = "$Password1"
driver.get("https://stage.myviewboard.com/signin")
driver.maximize_window()

MVBcom.loginMVBcom(driver,account,password)
MVBcom.enter_whiteboard(driver)
test_case.test_setting(driver)    
test_case.test_cloud_intergration(driver) #------
# test_case.test_about(driver)
# test_case.test_new_file(driver)
# test_case.test_open_file(driver)
# test_case.test_export_file_loacal(driver)
# test_case.test_image_search(driver)
# test_case.test_youtube(driver)
# # test_case.test_webpage(driver)
# # test_case.test_widget(driver)
# test_case.test_sticky_note(driver)
# test_case.test_pen(driver)
# test_case.test_AI_pen(driver)
# test_case.test_eraser(driver)
# test_case.test_present_mode(driver)
# test_case.test_pagemanagement(driver)
# test_case.test_qrcode_share(driver)#kim
# test_case.user_profile(driver)#kim
# test_case.test_shapes(driver)#kim
# test_case.test_shapes_lines(driver)#kim
# test_case.test_shapes_3Dshapes(driver)#kim
# test_case.test_shapes_tables(driver)#kim
# test_case.test_text(driver)#kim
# test_case.test_background(driver)#kim
# test_case.test_background_original(driver)#kim
# test_case.test_background_googledrive(driver)#kim
# test_case.test_background_image_search(driver)#kim
# test_case.test_background_color(driver)#kim
