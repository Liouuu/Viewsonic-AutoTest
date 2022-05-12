import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare
def open_background_menu (driver):
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t2f"]'))
            )     #toolbar-menu-layer > div > ul > li:nth-child(3) > div > div
    open_menu = driver.find_element_by_xpath('//div[@aria-label="t2f"]')    
    open_menu.click()      

def select_background_type(driver,num):
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/ul/li['+str(num)+']/div'))
            )
    type_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li['+str(num)+']/div')
    type_button.click()

def originals_background(driver,theme_num,num):
    #choose originals background theme type
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/ul/li['+str(theme_num)+']/div'))
            )
    theme_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/ul/li['+str(theme_num)+']/div')
    theme_button.click()

    #choose background
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/div[2]/div['+str(num)+']'))
            )
    background_image = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/div[2]/div['+str(num)+']')
    background_image.click()

def cloud_drive_background(driver,num):
    WebDriverWait(driver, 20).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[3]/div['+str(num)+']'))
            )      
    background_image = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[3]/div['+str(num)+']')
    background_image.click()
    
def image_search(driver,word,num):
    #search background image by inputting keyword
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div/div/div/div/input'))
            )
    input_word = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div/div/div/div/input')
    input_word.click()
    time.sleep(2)
    pyautogui.typewrite(word,0.2)
    pyautogui.press('enter')

    #choose an image as background
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[3]/div['+str(num)+']'))
            )
    background_image = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[3]/div['+str(num)+']')
    background_image.click()

def delete_background (driver):
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[2]/div/button[1]'))
            )
    delete_Background = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/button[1]')
    delete_Background.click()


def color(driver,column,row):
    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div/div['+str(column)+']/div['+str(row)+']'))
            )
    background_color = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div/div['+str(column)+']/div['+str(row)+']')
    background_color.click()

def apply_to_page(driver,num):

    WebDriverWait(driver, 5).until(                                
        EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div[2]/div/button['+str(num)+']')) 
            )
    apply_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/button['+str(num)+']')
    apply_button.click()

def close_origanal(driver):            
    WebDriverWait(driver, 5).until(                   
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/button'))
            )
    x_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div[2]/button')
    x_button.click()


def close_clouddrive_background_manager(driver):
    WebDriverWait(driver, 40).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[2]/button'))
            )
    x_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[2]/button')
    x_button.click()

def close_image_search(driver):
    WebDriverWait(driver, 5).until(                   
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/button'))
            )
    x_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/button')
    x_button.click()

def close_color(driver):
    WebDriverWait(driver, 5).until(                   
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/button'))
            )
    x_button = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/button')
    x_button.click()

def canvas_screenshot(driver,save_path):
    canvas = driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[3]/div")
    canvas.screenshot(save_path)

