import time
from selenium import webdriver
import time
import pyautogui
import MVBcom
import os
import write_log
import get_time
import logCheck
localTime = get_time.now()

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)
account = "kim.yj.liou@viewsonic.com"
password = "Mandy877!"
path='C:/Users/Liouki/Downloads'  #ROGER: 'C:/Users/kero/Downloads'
recorder_time=10 #錄影時間s
save_time=10 #存檔時間s

driver.get("https://stage.myviewboard.com/signin")
driver.maximize_window()

def file_num(target_path): #讀取目標資料夾檔案個數
    all_content=os.listdir(target_path)
    print('檔案數量',len(all_content))


def  screen_recorder(recorder_time,save_time) : 
    recorder = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/img[2]') 
    recorder.click() #點選螢幕錄製
    pyautogui.moveTo(744 , 438, duration= 0.5) #選畫面
    pyautogui.click()
    pyautogui.moveTo(1194 , 703, duration= 0.5) #點分享
    pyautogui.click()
    pyautogui.moveTo(516 , 100, duration= 0.5) #點X
    pyautogui.click()
    time.sleep(recorder_time)  #錄影時間
                             
    stop = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[6]/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/img[2]')  #暫停錄影 
    stop.click()
    time.sleep(2)
    download = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div/div[2]/div[5]/h6') #選擇下載到本地端    
    download.click()                     
    time.sleep(1)                          
    mp4 = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/span/span/input') #檔案類型選mp4
    mp4.click()
    OK = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/button[1]') #點擊確認後存檔
    OK.click() 
    time.sleep(save_time)# 存檔時間

file_num(path)
MVBcom.loginMVBcom(driver,account,password)
MVBcom.enter_classroom(driver)
screen_recorder(recorder_time,save_time)
file_num(path)
