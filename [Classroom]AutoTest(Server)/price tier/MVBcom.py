from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from export_table import export_table,TestCase_steps,new_sheet,TestCase_result

# def loginMVBcom(driver, account, password):
    
#     WebDriverWait(driver, 20).until(                                #讓瀏覽器等待(最多10秒)，等到ID為"mat-input-0"的element出現才繼續進行
#                 EC.element_to_be_clickable((By.XPATH, '//*[@id="c_main"]/input[1]'))   
#             )
#     account_blank = driver.find_element_by_xpath('//*[@id="c_main"]/input[1]')
#     account_blank.send_keys(account)

#     #operation = 'Input account'

#     login_btn = driver.find_element_by_xpath('//*[@id="c_main"]/button[1]')
#     login_btn.click()

#     #operation1 = 'Click Login button'

#     WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="c_main"]/input[2]')))
#     password_blank = driver.find_element_by_xpath('//*[@id="c_main"]/input[2]')
#     password_blank.send_keys(password)
#     #operation2 = 'Input password'

#     continue_btn = driver.find_element_by_xpath('//*[@id="c_main"]/button[3]')
#     continue_btn.click()
#     #operation3 = 'Click continue button'
 

def loginMVBcom(driver, account, password):
    pathName = './output sign in'
    TestCase = './登入'
    
    new_sheet(pathName)
    WebDriverWait(driver, 20).until(                                           #讓瀏覽器等待(最多10秒)，等到ID為"mat-input-0"的element出現才繼續進行
            EC.presence_of_element_located((By.CSS_SELECTOR,'#c_main > input.s1'))   
        )
    account_blank = driver.find_element_by_css_selector('#c_main > input.s1')
    account_blank.send_keys(account)                                           #點擊帳號欄位並輸入帳號 
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    login_but = driver.find_element_by_css_selector("#c_main > button.login-submit.inspect.s1")
    login_but.click()                                                          #點擊登入按鈕
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    #WebDriverWait(driver, 10).until(
     #       EC.presence_of_element_located((By.XPATH, "/html/body/div/input[2]"))
     #   )
    time.sleep(2)
    password_blank = driver.find_element_by_css_selector("#c_main > input.s2")
    password_blank.send_keys(password)                                         #點擊密碼欄位並輸入密碼
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    continue_but = driver.find_element_by_css_selector("#c_main > button.login-submit.submit.s2")
    continue_but.click()                                                       #點擊登入按鈕
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單

    #WebDriverWait(driver, 20).until(
    #        EC.presence_of_element_located((By.ID, "footer"))
    #    )
    #confirm_but = driver.find_element_by_id("footer")
    #confirm_but.click()

def enter_whiteboard(driver):
    pathName = './output sign in'
    TestCase = './登入'
    WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , "#page-top > app-dashboard > div > div > app-entity > div > div:nth-child(2) > app-main-feature-panel > element-main-feature > div > div:nth-child(2) > div > div > a > mat-card > mat-card-content:nth-child(2) > div.sub-links-list.ng-star-inserted > a:nth-child(3)"))  
        )
    driver.find_element_by_css_selector("#page-top > app-dashboard > div > div > app-entity > div > div:nth-child(2) > app-main-feature-panel > element-main-feature > div > div:nth-child(2) > div > div > a > mat-card > mat-card-content:nth-child(2) > div.sub-links-list.ng-star-inserted > a:nth-child(3)").click() #定位進whiteboard的icon的html tag
    time.sleep(2)                                                              #點擊what's new視窗 X
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    driver.switch_to.window(driver.window_handles[1]) #因為開分頁的關係，此code為切換程式run on的目標視窗
    try:    #處理出現「開啟多個教室...」時的情況
        WebDriverWait(driver, 20).until(                                
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[3]/div/div[2]"))
                )
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/div[2]").click()  #點擊確認
        time.sleep(3)
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()  #彈出框點擊重新整理
    except:
        pass
    WebDriverWait(driver, 7).until(                                
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div/div'))
        ) 
    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div').click() #點擊what's new視窗 X   
    export_table(pathName,TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[8]/div[3]/div/div[1]")) 
    #     )
    # driver.find_element_by_xpath("//*[@id=\"root\"]/div[1]/div[1]/div/div/div/div/div[8]/div[3]/div/div[1]").click()   #關閉開啟儀表板  