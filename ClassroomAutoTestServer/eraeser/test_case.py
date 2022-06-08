from os import putenv
import Eraser_func
import time
import canvas_compare
from PIL import Image
from selenium import webdriver
import pyautogui
import pyperclip
def open_file(driver):
   Eraser_func.new_file(driver)
   Eraser_func.open_file_management(driver)
   pyautogui.click(987,73,duration=1) #3點擊資料夾上方路經
   pyautogui.typewrite("C:\\Users\\kero\\Desktop\\python\\eraeser",interval=0.1) #輸入路徑
   pyautogui.press('enter')
   pyautogui.doubleClick(434 , 270 , duration=0.5) #雙擊開檔
   pyautogui.click(1077 , 281 , duration=0.5) #關閉彈出的視窗
   pyautogui.click(1260 , 678 , duration=0.5)         #/html/body/div[4]/div/div/div[3]/div/button[1]/span
   pyautogui.click(1109 , 662 , duration=0.5)         #/html/body/div[4]/div/div[2]/button[2]/span
   time.sleep(100)    #開檔時間

def test_normal_eraser(driver):
   
   time.sleep(2)
   Eraser_func.open_eraser_Menu(driver,3)
   for i in range (0,5):
      pyautogui.moveTo(220 ,254+i*160,duration=1)
      pyautogui.dragTo(1680,254+i*160,1,button="left")
      
   sample_image = './image/SampleImage1.png'
   case_image = './image/ResultImage1.png'  
   Eraser_func.canvas_screenshot(driver,case_image)
   compare = canvas_compare.canvas_compare(sample_image,case_image,1)
   if compare == True:
      print("Pass")
   else:
      print("Failed")
   Eraser_func.turn_page(driver)
   time.sleep(3)

def circle_eraser(driver):
   sample_image = './image/SampleImage2.png'
   case_image = './image/ResultImage2.png'

   Eraser_func.open_eraser_Menu(driver,2)
   Eraser_func.circle_canvas()
   Eraser_func.canvas_screenshot(driver,case_image)
   result = canvas_compare.canvas_compare(sample_image,case_image,2)
   if result == True:
      print("Pass")
        
   else:
     print("Failed")
   Eraser_func.turn_page(driver)
   time.sleep(3)

def test_Handwriting_eraser(driver):
   time.sleep(6)
   Eraser_func.open_eraser_Menu(driver,3)
   time.sleep(5)
   sample_image = './image/SampleImage3.png'
   case_image = './image/ResultImage3.png'  
   Eraser_func.canvas_screenshot(driver,case_image)
   result = canvas_compare.canvas_compare(sample_image,case_image,3)
   
   if result == True:
      print("Pass")
        
   else:
      print("Failed")
   Eraser_func.turn_page(driver)
   time.sleep(3)

def clean_all(driver):
   sample_image = './image/SampleImage4.png'
   case_image = './image/ResultImage4.png'
   Eraser_func.open_eraser_Menu(driver,4)
   Eraser_func.confirm_clean_canvas(driver)
   Eraser_func.canvas_screenshot(driver,case_image)
   result = canvas_compare.canvas_compare(sample_image,case_image,4)
   if result == True:
      print("Pass")
        
   else:
      print("Failed")