from time import time
from selenium import webdriver  
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def open_shape_menu(driver):
    shape_butuon = driver.find_element_by_xpath('//div[@aria-label="t2e"]')   
    shape_butuon.click()
    try:
        WebDriverWait(driver, 3).until(                                
                EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div'))
        )
    except:
        shape_butuon.click()

def select_shape_type (driver, shape_type): #1 for shape, 2 for line... 
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/div/div['+str(shape_type)+']'))
        )                                             
    shape = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/div/div['+str(shape_type)+']')
    shape.click()

def select_shape (driver,shape):   #選形狀 1 方形 ,2 圓形...   1~8
    WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[1]/div['+str(shape)+']/div'))   
    )                                                  
    shape_select = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[1]/div['+str(shape)+']/div')
    shape_select.click()

def select_line (driver,line):
    WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[1]/div['+str(line)+']/div'))   
    )                                           
    line_select = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[1]/div['+str(line)+']/div')
    line_select.click()

def adjust_shape_thickness(driver, val):  #range of val is 0~35
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, '//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[3]/div[1]/div/div/div/span/span[1]'))
        )                                                                                            
    thickness_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[3]/div[1]/div/div/div/span/span[3]")
    thickness_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[3]/div[1]/div/div/div/span/span[1]")
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,-thickness_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,val*thickness_bar.size['width']/35,0).perform()

def adjust_line_thickness(driver, val):  #range of val is 0~35
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, '//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[2]/div[1]/div/div/div/span'))
        )                                                                                            
    thickness_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[2]/div[1]/div/div/div/span/span[3]")
    thickness_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[2]/div[1]/div/div/div/span/span[1]")
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,-thickness_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(thickness_bar_thumb,val*thickness_bar.size['width']/35,0).perform()


def adjust_shape_transparency(driver, val):   #range of val is 0~35
    #select_pen_type(driver, 1)
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[3]/div[2]/div/div/div/span/span[3]"))
        )
    transparency_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[3]/div[2]/div/div/div/span/span[3]")
    transparency_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[3]/div[2]/div/div/div/span")    
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,-transparency_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,val*transparency_bar.size['width']/35,0).perform()

def adjust_line_transparency(driver, val):   #range of val is 0~35
    #select_pen_type(driver, 1)
    WebDriverWait(driver, 10).until(                                
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[2]/div[2]/div/div/div/span"))
        )
    transparency_bar_thumb = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[2]/div[2]/div/div/div/span/span[3]")
    transparency_bar = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div/div/div[2]/div[2]/div[2]/div/div/div/span/span[1]")
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,-transparency_bar.size['width'],0).perform()
    time.sleep(0.5)
    ActionChains(driver).drag_and_drop_by_offset(transparency_bar_thumb,val*transparency_bar.size['width']/35,0).perform()

def select_shape_up_color(driver, num): #range of num is 1~7
    #select_pen_type(driver, 1)
    time.sleep(0.5)
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[3]/div[3]/button['+str(num)+']')
    color_up.click()                         
                                                                   
def select_line_up_color(driver, num): #range of num is 1~7
    #select_pen_type(driver, 1)
    time.sleep(0.5)
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[2]/div[3]/button['+str(num)+']/div/div')
    color_up.click()

def close_shape_menu(driver):
    driver.find_element_by_xpath('//div[@aria-label="t1f"]').click()

def shape_menu_screenshot(driver, save_path):
    shape_menu = driver.find_element_by_xpath("//*[@id=\"toolbar-menu-layer\"]/div")
    shape_menu.screenshot(save_path)

def DrawLine(X1,Y1,X2,Y2):    
    pyautogui.moveTo(X1, Y1, duration= 0.5)
    pyautogui.mouseDown()   
    pyautogui.moveTo(X2, Y2, duration= 0.5)
    pyautogui.mouseUp()
    time.sleep(1)    

def canvas_screenshot(driver, save_path):
    canvas = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[3]/div/div')                            
    canvas.screenshot(save_path)

def turn_page(driver):
    page = driver.find_element_by_xpath('//div[@aria-label="t5"]') 
    page.click()

