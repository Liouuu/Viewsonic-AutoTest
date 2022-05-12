import func
import time
import canvas_compare
from PIL import Image
from selenium import webdriver
import pyautogui
import pyperclip

word = 'test'
url = 'https://www.youtube.com/watch?v=Ptk_1Dc2iPY'

def clips_test(driver):   #i=5 image search , i=7 clips , i=8 youtube
    case_image = './image/CaseImage2.png'
    sample_image = './image/SampleImage2.png'
    case_image1 = './image/CaseImage2_1.png'
    sample_image1 = './image/SampleImage2_1.png'
    func.open_magic_box(driver,7)
    func.clips_playlist(driver)
    time.sleep(1)
    func.menu_screenshot(driver,case_image)
    time.sleep(1)
    #func.menu_screenshot(driver,sample_image)
    compare = canvas_compare.canvas_compare (sample_image,case_image,2)
    if compare == True:
        print("Pass")
    else:
        print("Failed")
    func.click_My_quiz(driver,3)
    pyautogui.moveTo(815 , 710,duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1500 ,569,duration=0.5)
    pyautogui.mouseUp()
    func.close_magic_box(driver)
    time.sleep(5)
    func.canvas_screenshot(driver,case_image1)
    time.sleep(1)
    #func.canvas_screenshot(driver,sample_image1)
    compare1 = canvas_compare.canvas_compare(sample_image1,case_image1,2)
    if compare1 == True:
        print("Pass")
    else:
        print("Failed")
    func.turn_page(driver)

def test_image_search(driver):
    sample_image = './image/SampleImageSearch.png'
    case_image = './image/ImageSearch.png'

    func.open_magicbox(driver)
    func.image_search_menu(driver)
    func.image_search(driver,word)
    func.close_magicbox(driver)

    #func.canvas_screenshot(driver,sample_image)
    func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,1)
    if compare == True:
        print("Pass")
    else:
        print("Failed")
    func.turn_page(driver)

def test_youtube_search(driver):
    sample_image = './image/SampleYoutube.png'
    case_image = './image/Youtube.png'
    time.sleep(2)
    func.open_magicbox(driver)
    time.sleep(2)
    func.youtube_menu(driver)
    time.sleep(1)
    func.youtube_search(driver,url)
    func.close_magicbox(driver)

    #func.canvas_screenshot(driver,sample_image)
    func.canvas_screenshot(driver,case_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,3)
    if compare == True:
        print("Pass")
    else:
        print("Failed")