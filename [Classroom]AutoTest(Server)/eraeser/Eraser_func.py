from time import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import pyautogui
import pyperclip
def new_file(driver):
    file_management_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[1]')    
    file_management_button.click()
    New_file_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[1]/div')    
    New_file_button.click()
    time.sleep(1)
    Comfirm_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/button[1]')    
    Comfirm_button.click()

def open_file_management(driver):
    file_management_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[1]')    
    file_management_button.click()
    open_button = driver.find_element_by_xpath(' //*[@id="toolbar-menu-layer"]/div[1]/ul/li[2]')        
    open_button.click()
    time.sleep(0.5)
    localdrive_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[2]/div/div/div/div/ul/li[1]')  
    localdrive_button.click()

def open_eraser_Menu(driver,i):
    eraser_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[6]')
    eraser_button.click()
    try:
        WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/p'))
            )
    except:
        eraser_button.click()
    select_eraser = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(i)+']')   
    select_eraser.click()

    time.sleep(1)

def circle_eraser(driver):
    WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[5]/div/div[2]/div[6]/div'))
            )
    eraser = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[5]/div/div[2]/div[6]/div')
    eraser.click(click=2)
    WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]'))
            )
    second_eraser = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]')
    second_eraser.click()

def circle_canvas():
    time.sleep(2)
    pyautogui.mouseDown(1692,248,duration=0.2)
    pyautogui.dragTo(222,245,duration=0.5)
    pyautogui.dragTo(222,958,duration=0.5)
    pyautogui.dragTo(1692,958,duration=0.5)
    pyautogui.mouseUp(1692,248,duration=0.2)
    pyautogui.click(clicks=1)
    time.sleep(2)

def confirm_clean_canvas(driver):
    
    WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/div[2]/div/button[1]'))
            )
    ok_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/button[1]')
    ok_button.click()

def canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]")
    canvas.screenshot(save_path)

def turn_page(driver):
    page = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[2]/div[3]/div') 
    page.click()

