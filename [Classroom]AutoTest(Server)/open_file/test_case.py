import open_file_func
import time
from PIL import Image
from selenium import webdriver
import pyautogui

def test_localdrive (driver):
    open_file_func.open_magicbox(driver) # 開magicbox
    open_file_func.localdrive_import(driver)  #點擊import
    pyautogui.click(375, 80,duration=1) #3點擊資料夾上方路經
    pyautogui.typewrite("C:\\Users\\kero\\Desktop\\python\\open_file\\image",interval=0.1) #輸入路徑
    pyautogui.press('enter')
    pyautogui.doubleClick(330,256,duration=1) #選第一張圖
    time.sleep(3)
    for i in range(1,4):  #選2-4張圖
        pyautogui.click(978, 745,duration=1)
        pyautogui.doubleClick(330+i*178 , 256,duration=1)
        time.sleep(4)
    pyautogui.click(241,595,duration=1)
    pyautogui.click(950,600 ,duration=1) #將最上方圖片拖曳至左上
    pyautogui.dragTo(470,400,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第二張圖片拖曳至右上
    pyautogui.dragTo(1345,400,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第三張圖片拖曳至左下
    pyautogui.dragTo(478,770,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第四張圖片拖曳至右下
    pyautogui.dragTo(1368,770,1,button='left')
    pyautogui.click(950,600 ,duration=1)  #點一下中心讓選取框消失
    open_file_func.turn_page(driver)
    
    
    open_file_func.open_magicbox(driver) # 開magicbox
    open_file_func.localdrive_import(driver)  #點擊import
    pyautogui.click(850, 80,duration=1) #3點擊資料夾上方路經
    pyautogui.typewrite("C:\\Users\\kero\\Desktop\\python\\open_file\\video",interval=0.1) #輸入影片路徑 
    pyautogui.press('enter')
    pyautogui.doubleClick(330,256,duration=1) #選一影片
    time.sleep(20)
    for i in range(1,2):  #選2影片
        pyautogui.click(978, 745,duration=1)
        pyautogui.doubleClick(330+i*178 , 256,duration=1)
        time.sleep(20)
    pyautogui.click(241,595,duration=1)
    pyautogui.click(950,600 ,duration=1) #將最上方圖片拖曳至左上
    pyautogui.dragTo(470,400,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第二張圖片拖曳至右上
    pyautogui.dragTo(1345,400,1,button='left')
    pyautogui.click(950,600 ,duration=1)
    open_file_func.turn_page(driver)
    
    
    open_file_func.open_magicbox(driver) # 開magicbox
    open_file_func.localdrive_import(driver)  #點擊import
    pyautogui.click(850, 80,duration=1) #3點擊資料夾上方路經
    pyautogui.typewrite("C:\\Users\\kero\\Desktop\\python\\open_file\\audio",interval=0.1) #輸入音訊路徑 
    pyautogui.press('enter')
    pyautogui.doubleClick(330,256,duration=1) #選一音訊
    time.sleep(50)
    for i in range(1,3):  #選2 3音訊
        pyautogui.click(978, 745,duration=1)
        pyautogui.doubleClick(330+i*178 , 256,duration=1)
        time.sleep(30)
    pyautogui.click(241,595,duration=1)
    pyautogui.click(950,600 ,duration=1) #將最上方音訊拖曳至左上
    pyautogui.dragTo(470,400,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第二音訊拖曳至右上
    pyautogui.dragTo(1345,400,1,button='left')
    pyautogui.click(950,600 ,duration=1) #將第三音訊拖曳至右上
    pyautogui.dragTo(470,770,1,button='left')
    pyautogui.click(950,600 ,duration=1)
    open_file_func.turn_page(driver)

def test_googledrive (driver):
    open_file_func.open_magicbox(driver) # 開magicbox
    time.sleep(3)
    open_file_func.select_drive_type(driver,2) #選googledrive
    time.sleep(10)
    pyautogui.click(800,567,duration=0.5) #選a資料夾
    time.sleep(1)
    pyautogui.moveTo(830,880,duration=0.3)  #拉圖
    pyautogui.dragTo(1600,255,duration=0.5)
    time.sleep(4)
    for i in range (0,3):
        pyautogui.moveTo(830+i*180,740,duration=0.5)
        pyautogui.dragTo(340,320+i*255,duration=0.5)
        time.sleep(4)
    pyautogui.click(800,570,duration=0.5) #選影音資料夾
    time.sleep(1)
    for j in range(0,2):
        pyautogui.moveTo(820+j*240,800,duration=0.7) 
        pyautogui.dragTo(1600,255,duration=0.5)
        time.sleep(30)
    for i in range (0,3):
        pyautogui.moveTo(820+i*240,670,duration=0.5)
        pyautogui.dragTo(340,320+i*255,duration=0.5)
        time.sleep(30)
    pyautogui.click(1600,255,duration=0.5)
    
    pyautogui.click(950,600,duration=0.5)
    pyautogui.dragTo(1500,850,duration=0.5)
    
    pyautogui.click(950,600,duration=0.5)
    pyautogui.dragTo(960,850,duration=0.5)
    
    pyautogui.click(950,600,duration=0.5)
    pyautogui.dragTo(1200,300,duration=0.5)
    
    pyautogui.click(950,600,duration=0.5)
    pyautogui.dragTo(700,300,duration=0.5)

