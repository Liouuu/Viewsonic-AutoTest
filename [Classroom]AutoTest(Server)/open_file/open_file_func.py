import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def open_magicbox(driver) :
    magicbox = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]/div/div') 
    magicbox.click()

def select_drive_type (driver, drive_type): #1 for localdrive , 2 for googledrive , 3 for onedrive ,4 for onedrive for business
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,' //*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div['+str(drive_type)+']/div/div/div[2]/div'))
        )
    drive = driver.find_element_by_xpath(' //*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div['+str(drive_type)+']/div/div/div[2]/div')
    drive.click()
def localdrive_import (driver):
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,' //*[@id="toolbar-menu-layer"]/div/div[2]/div/div/p'))
        )
    drive = driver.find_element_by_xpath(' //*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div')#點import
    drive.click()

def turn_page(driver):
    page = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[2]/div[4]/div") 
    page.click()

