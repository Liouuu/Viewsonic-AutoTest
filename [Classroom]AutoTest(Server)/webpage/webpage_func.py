from PIL.ImageOps import grayscale
import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import pyscreenshot as ImageGrab



def open_magic_box(driver,i) :  #i=5 image search , i=7 clips , i=8 youtube, i=9 webpage

    magic_box_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]')
    magic_box_button.click()
    time.sleep(1)

    if i>=8:
        #按">"直到youtube圖示顯示在magicbox
        WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[3]'))
            )
        slick_next = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[3]')  
        slick_next.click()
    time.sleep(1)    
        
    select_magic_box_func = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div['+str(i)+']')     
    select_magic_box_func.click()

    time.sleep(1)

def input_url(driver,url):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input'))
            )
    input_url = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input')  
    input_url.click()
    time.sleep(2)
    pyautogui.typewrite(url,0.1)

def input_title(driver,title):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/input'))
            )
    input_word = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[1]/div[2]/div/div/div/input')  
    input_word.click()
    time.sleep(2)
    pyautogui.typewrite(title,0.1)

def add_to_list(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[2]/button'))
            )
    add_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div[2]/button')  
    add_button.click()

    time.sleep(2)
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]/div/nav/ul/li[3]/button'))
            )
    next_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]/div/nav/ul/li[3]/button')  
    next_button.click()

def put_on_canvas():
    time.sleep(1)
    web_icon = './image/web_icon.png'
    x,y = pyautogui.locateCenterOnScreen(web_icon,grayscale = True, confidence = 0.7)
    pyautogui.click(x,y,clicks=1,duration=0.2)
    pyautogui.dragTo(374,523,duration=0.3)
    time.sleep(3)

  
def close_magicbox(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button'))
            )
    close_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button')  
    close_menu.click()   

def canvas_screenshot(driver, save_path):
    
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div")
    canvas.screenshot(save_path)

def magicbox_screenshot(driver,save_path):
    time.sleep(1)
    magicbox = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div')
    magicbox.screenshot(save_path)
    time.sleep(2)

def webpage_screenshot(save_path):
    img = ImageGrab.grab(bbox=(0,107,1913,1015))  
    img.save(save_path)

def present_mode(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[8]/div[2]/div/div/div'))
            )
    mode_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[8]/div[2]/div/div/div')  
    mode_button.click()  

def enter_webpage():
    web_icon = './image/web_icon.png'
    x,y = pyautogui.locateCenterOnScreen(web_icon,grayscale = True, confidence = 0.7)
    pyautogui.click(x,y)
    time.sleep(5)

def delete_hyperlink(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/ul/li/div/div/div[2]/button'))
            )
    x_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/ul/li/div/div/div[2]/button')  
    x_button.click()
 
