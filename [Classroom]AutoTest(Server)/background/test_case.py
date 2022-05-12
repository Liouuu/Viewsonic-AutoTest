import pyautogui

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare
import background_func

original_theme = [3,7]  #[主題,第幾個]
google_image = 2    #google drive第幾張圖
onedrive_image = 1   #onedrive第幾張圖
word = "test"
color = [5,2]

def test_originals(driver):

    sample_image = './image/SampleImageOriginals.png'
    case_image = './image/ImageOriginals.png'
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,1)
    background_func.originals_background(driver,original_theme[0],original_theme[1])
    background_func.apply_to_page(driver,1)         
    background_func.close_origanal(driver)   
    time.sleep(10)     
    background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,1)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

def test_google(driver):

    sample_image = './image/SampleImageGoogle.png'
    case_image = './image/ImageGoogle.png'
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,2)
    pyautogui.moveTo(900,550,duration=0.5)
    pyautogui.click()
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,2)
    time.sleep(5)
    background_func.cloud_drive_background(driver,google_image)
    background_func.apply_to_page(driver,2)
    time.sleep(20)
    background_func.close_clouddrive_background_manager(driver)
    #background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,2)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

def test_onedrive(driver):
    sample_image = './image/SampleImageOnedrive.png'
    case_image = './image/ImageOnedrive.png'

    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,3)
    pyautogui.moveTo(900,550,duration=0.5)
    pyautogui.click()
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,3)
    time.sleep(5)
    background_func.cloud_drive_background(driver,onedrive_image)
    background_func.apply_to_page(driver,2)
    time.sleep(13)
    background_func.close_clouddrive_background_manager(driver)
    background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,3)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

def test_business(driver):

    sample_image = './image/SampleImageForBusiness.png'
    case_image = './image/ImageForBusiness.png'

    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,4)
    pyautogui.moveTo(900,550,duration=0.5)
    pyautogui.click()
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,4)
    time.sleep(5)
    background_func.cloud_drive_background(driver,onedrive_image)
    background_func.apply_to_page(driver,2)
    time.sleep(13)
    background_func.close_clouddrive_background_manager(driver)
    background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,4)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

def test_image_search (driver):
    sample_image = './image/SampleImageImageSearch.png'
    case_image = './image/ImageImageSearch.png'
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,5)
    background_func.image_search(driver,word,1)
    background_func.apply_to_page(driver,1) 
    time.sleep(25)
    background_func.close_image_search(driver)
    background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,5)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

def test_color(driver):
    sample_image = './image/SampleImage6.png'
    case_image = './image/Image6.png'
    background_func.open_background_menu(driver)
    background_func.select_background_type(driver,6)
    background_func.color(driver,color[0],color[1])
    background_func.apply_to_page(driver,1)
    background_func.delete_background(driver)
    time.sleep(10)
    background_func.close_color(driver)
    background_func.canvas_screenshot(driver,sample_image)
    background_func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,6)
    if compare == True:
        print("Pass")
    else:
        print("Failed")