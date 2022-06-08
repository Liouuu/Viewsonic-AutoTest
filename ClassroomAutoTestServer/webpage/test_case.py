from cv2 import groupRectangles
import pyautogui
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare
import webpage_func


url = 'https://translate.google.com.tw/?hl=zh-TW&tab=rT'
title = 'translate'

def webpage_test(driver):
    
    #比對MagicBox WebPage List
    webpage_func.open_magic_box(driver,9)
    webpage_func.input_url(driver,url)
    webpage_func.input_title(driver,title)
    webpage_func.add_to_list(driver)

    magicbox_sample = './image/MagicboxSample.png'
    magicbox_case = './image/MagicboxCase.png'
    #webpage_func.magicbox_screenshot(driver,magicbox_sample)
    webpage_func.magicbox_screenshot(driver,magicbox_case)
    compare = canvas_compare.canvas_compare(magicbox_sample,magicbox_case,1)
    if compare == True:
        print('Web page list : Pass')
    else: 
        print('Web page list : Failed')

    #比對畫布
    webpage_func.put_on_canvas()
    webpage_func.delete_hyperlink(driver)
    webpage_func.close_magicbox(driver)
    
    canvas_sample = './image/CanvasSample.png'
    canvas_case = './image/CanvasCase.png'
    #webpage_func.canvas_screenshot(driver,canvas_sample)
    webpage_func.canvas_screenshot(driver,canvas_case)
    compare = canvas_compare.canvas_compare(canvas_sample,canvas_case,2)
    if compare == True:
        print('Canvas : Pass')
    else: 
        print('Canvas : Failed')

    #比對網頁
    webpage_func.present_mode(driver)
    webpage_func.enter_webpage()

    webpage_sample = './image/WebpageSample.png'
    webpage_case = './image/WebpageCase.png'
    #webpage_func.webpage_screenshot(webpage_sample)
    webpage_func.webpage_screenshot(webpage_case)
    compare = canvas_compare.canvas_compare(webpage_sample,webpage_case,3)
    if compare == True:
        print('Web page : Pass')
    else: 
        print('Web page : Failed')