import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare

def open_magic_box(driver,i) :  #i=5 image search , i=7 clips , i=8 youtube
    magic_box_button = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]')
    magic_box_button.click()
    time.sleep(1)
    select_magic_box_func = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div['+str(i)+']')     
    select_magic_box_func.click()

    time.sleep(1)

def clips_playlist(driver) :
    time.sleep(7)
    playlist_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div[2]/div[2]/div/div')
    playlist_button.click()
    
def menu_screenshot (driver,save_path):
    menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div[2]')
    menu.screenshot(save_path)


def click_My_quiz (driver,i):   #i=第幾個quiz
    My_quiz_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div[1]/div[3]')
    My_quiz_button.click()
    time.sleep(1)
    quiz_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div[2]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/div')
    quiz_button.click()
    time.sleep(1)
    select_quiz_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div/div/div[2]/div[2]/div/div['+str(i)+']/div[2]/div/div/div/div/div[2]/span/span')
    select_quiz_button.click()
    
def close_magic_box(driver):
    close_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]')
    close_button.click()

def canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[5]")
    canvas.screenshot(save_path)

def open_magicbox (driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]/div/div'))
            )
    open_menu = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[4]/div/div[2]/div[2]/div/div')  
    open_menu.click()   

def image_search_menu (driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div[5]/div/div/div[2]/div'))
            )
    open_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div[5]/div/div/div[2]/div')  
    open_menu.click()   

def youtube_menu (driver):
    #按">"直到youtube圖示顯示在magicbox
    slick_next = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[3]')  
    slick_next.click()
    time.sleep(3)
    #選擇youtube搜尋
    open_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/div/div[2]/div/div[8]/div/div/div[2]/div')  
    open_menu.click()   

def image_search(driver,word):
    #search image by inputting keyword
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div/div/div/div/input'))
            )
    input_word = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div/div/div/div/input')
    input_word.click()
    time.sleep(2)
    pyautogui.typewrite(word,0.2)
    pyautogui.press('enter')

    #拖曳第一張圖片至畫布
    time.sleep(3)
    pyautogui.click(648,540,clicks=1,duration=0.2)
    pyautogui.dragTo(374,523,duration=0.3)
    time.sleep(3)

def youtube_search(driver,url):
    #search image by inputting keyword
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div/div/div/div/input'))  
            )
    input_word = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/div/div/div/div/input')
    input_word.click()
    time.sleep(2)
    pyautogui.typewrite(url,0.1)

    #點擊搜尋按鈕
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/button[2]/div'))
            )
    input_word = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/button[2]/div')
    input_word.click()

    #拖曳第一支影片至畫布
    time.sleep(5)
    pyautogui.click(648,540,clicks=1,duration=0.2)
    pyautogui.dragTo(374,523,duration=0.3)
    time.sleep(3)

def close_magicbox(driver):
    WebDriverWait(driver, 30).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button'))
            )
    close_menu = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[1]/div[2]/button')  
    close_menu.click()   
    

def turn_page(driver):
    page = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[2]/div[4]/div") 
    page.click()