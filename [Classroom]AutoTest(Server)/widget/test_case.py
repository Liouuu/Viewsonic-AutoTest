import func
import time
import canvas_compare
from PIL import Image
from selenium import webdriver
import pyautogui
import pyperclip
def test_widget (driver):
    func.open_magicbox(driver)
    func.widget_menu(driver)
    for i in range(1,5):
        case_image = './image/CaseImage'+str(i)+'.png'
        sample_image = './image/SampleImage'+str(i)+'.png'
        func.select_widget_type(driver,i)
        time.sleep(5)
        func.menu_screenshot(driver,case_image)
        time.sleep(1)
        #func.menu_screenshot(driver,sample_image)
        time.sleep(2)
        pyautogui.moveTo(840,492,duration=0.7)
        pyautogui.mouseDown()
        pyautogui.moveTo(348,80+i*200,duration=0.5)
        pyautogui.mouseUp()
        compare = canvas_compare.canvas_compare(sample_image,case_image,i)
        if compare == True:
            print('menu'+str(i)+'Pass')
        else:
            print('menu'+str(i)+'Failed')
    func.close_magicbox(driver)
    case_image1 ='./image/CaseImagecanvas.png'
    sample_image1 = './image/SampleImagecanvas.png'
    time.sleep(7)
    func.canvas_screenshot(driver,case_image1)    
    #func.canvas_screenshot(driver,sample_image1)   
    
    compare = canvas_compare.canvas_compare(sample_image1,case_image1,i)
    if compare == True:
        print('canvas Pass')
    else:
        print('canvas Failed')
   