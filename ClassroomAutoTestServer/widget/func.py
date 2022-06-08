import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare


def menu_screenshot (driver,save_path):
    menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div')
    menu.screenshot(save_path)


def canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]")
    canvas.screenshot(save_path)

def open_magicbox (driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]/div/div'))
            )
    open_menu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]/div/div')  
    open_menu.click()   
  

def widget_menu (driver):
    #按">"直到youtube圖示顯示在magicbox
    slick_next = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[3]')  
    slick_next.click()
    time.sleep(3)
    #選擇widget
    open_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div[11]/div/div/div[2]/div')  
    open_menu.click()   


def close_magicbox(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button'))
            )
    close_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button')  
    close_menu.click()   

def select_widget_type (driver,i): #1-4
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div/div[1]/li['+str(i)+']'))
            )
    select_type = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div[1]/li['+str(i)+']')  
    select_type.click()


