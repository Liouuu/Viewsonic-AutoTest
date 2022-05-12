from time import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import pyautogui

def open_TextEditor_Menu(driver):
    texteditor_butuon = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[9]')
    texteditor_butuon.click()
    time.sleep(1)

def open_StickyNotes_Menu(driver,i):
    WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[7]'))
            )
    stickynote_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[7]')
    stickynote_button.click()
    WebDriverWait(driver, 3).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(i)+']'))
            )                                                 
    select_stickynote = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(i)+']')
    select_stickynote.click()
    time.sleep(1)

def enter_english_text(x,y,text):
    pyautogui.moveTo(x,y,duration=0.5)
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.typewrite(text)
    time.sleep(2)

def enter_chinese_text(x,y,text):
    time.sleep(2)
    pyautogui.moveTo(x,y,duration=0.5)
    pyautogui.click(clicks=1)
    pyautogui.hotkey("shift")
    time.sleep(1)
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.hotkey('shift')

def select_by_key():
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)

def text_editor_func_select(driver,func): #func= 1-7  
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[9]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div['+str(func)+']/div'))
            )
    func_select = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[9]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div['+str(func)+']/div')
    func_select.click()
    time.sleep(1)

def text_editor_func_select2(driver,func): #func= 1-7  
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[9]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div['+str(func)+']'))
            )
    func_select = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[9]/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div['+str(func)+']')
    func_select.click()
    time.sleep(1)

def text_type(driver,num):  #num = 1~19
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div['+str(num)+']'))
            )
    type_select = driver.find_element_by_xpath('/html/body/div[5]/div['+str(num)+']')
    type_select.click()         
    time.sleep(1)

def text_size(driver,num):  #num = 1~20
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div['+str(num)+']'))
            )
    size_select = driver.find_element_by_xpath('/html/body/div[5]/div['+str(num)+']')
    size_select.click()
    time.sleep(1)


def text_color(driver,num1,num2): 
    if num1 == 1:     #num2 = 1~7
        WebDriverWait(driver, 10).until(                                
                EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/button['+str(num2)+']/div/div')) 
                )
        color_select = driver.find_element_by_xpath('/html/body/div[4]/div[1]/button['+str(num2)+']/div/div')
        color_select.click()
    elif num1 == 2:   #num2 = 1~128
        WebDriverWait(driver, 10).until(                                
                EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/button['+str(num2)+']/div/div'))
                )
        color_select = driver.find_element_by_xpath('/html/body/div[4]/div[2]/button['+str(num2)+']/div/div')
        color_select.click()
        time.sleep(1)

def text_color2(driver,num1,num2): 
    if num1 == 1:     #num2 = 1~7
        WebDriverWait(driver, 10).until(                                
                EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/button['+str(num2)+']/div/div'))  
                )
        color_select = driver.find_element_by_xpath('/html/body/div[4]/div[1]/button['+str(num2)+']/div/div')
        color_select.click()
    elif num1 == 2:   #num2 = 1~128
        WebDriverWait(driver, 10).until(                                
                EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/button['+str(num2)+']/div/div'))
                )
        color_select = driver.find_element_by_xpath('/html/body/div[4]/div[2]/button['+str(num2)+']/div/div')
        color_select.click()
        time.sleep(1)

def canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]")
    canvas.screenshot(save_path)

def turn_page(driver):
    page = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[2]/div[4]/div") 
    page.click()
