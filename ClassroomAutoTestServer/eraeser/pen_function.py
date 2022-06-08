import time
from selenium import webdriver
import pyautogui
import pyscreenshot as ImageGrab
import cv2

def key_account(): #輸入帳號
    account = driver.find_element_by_id("mat-input-0")
    account.send_keys("roger.ke@viewsonic.com")
    login_button = driver.find_element_by_xpath('//*[@id="page-top"]/app-landing/div/div/ng-component/main/div/div/div/div/div/div/form/div[2]/button')
    login_button.click()
    time.sleep(5)

def key_password():   #輸入密碼
    password = driver.find_element_by_id("pwinput")
    password.send_keys("#sS3133265")
    login_button = driver.find_element_by_xpath('//*[@id="page-top"]/app-landing/div/div/ng-component/main/div/div/div/div/div/div/form/div[3]/button')
    login_button.click()
    time.sleep(7)

def notification():
    button = driver.find_element_by_id("footer")
    time.sleep(1)
    button.click()
    time.sleep(2)

def enter_Classroom():
    driver.find_element_by_class_name("mat-card").click() #定位進Classroom的icon的html tag
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1]) #因為開分頁的關係，此code為切換程式run on的目標視窗
    time.sleep(5)
    pyautogui.moveTo(1236, 713, duration= 0.5) #開啟多個教室，要點擊確認
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1073, 243, duration= 0.5) #點擊重新整理
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(1283, 223,duration= 1) #進教室會有what's new，此為關閉code 
    pyautogui.click()
    time.sleep(2)
 
def marker_pen():
    time.sleep(1)
    pyautogui.moveTo(1894, 514, duration= 1) #選筆功能
    pyautogui.doubleClick() #第一次點要點兩下才可以打開menu
    time.sleep(1)
    img = driver.find_element_by_xpath ('//*[@id="toolbar-menu-layer"]/div')
    img.screenshot('pen.png')
    pen_type =1
    pen = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div['+str(pen_type)+']/div/div')
    pen.click()
    num=1
    color_up = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[3]/div/div/div[3]/button['+str(num)+']/div/div')
    color_up.click()
    time.sleep(3)
    im = ImageGrab.grab(
    bbox=(1096,   # X1
        310,   # Y1
       1853,   # X2
       1013))  # Y2
    im.save("red.png") # 儲存檔案
    time.sleep(1)
    X = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[1]/div/button')
    X.click()
    time.sleep(4)




if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://stage.myviewboard.com/signin?returnurl=/home")
    driver.maximize_window()
    time.sleep(5)
    key_account()
    key_password()
    notification()
    enter_Classroom()
    marker_pen()
    #marker_check()
    #ighlighter()
    #HLpen_check()
    #laser_pen()
    #LSpen_check()
    driver.quit()