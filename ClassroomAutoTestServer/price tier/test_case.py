import pyautogui
import write_log
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import canvas_compare
from price_tier_func import image_search
import screenshot
import get_time
import logCheck
import file_check_and_remove
from export_table import export_table,TestCase_steps,new_sheet,TestCase_result,TestCase_case
localTime = get_time.now()
# 只要是mainToolBar點出來的視窗>有X按鈕的路徑為:  
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #點擊X關閉視窗

def test_setting (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    # pathName =      './output sign in'
    # TestCase =      './登入'
    # step =          "截圖比對"
    case_image =    'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\setting.png'
    sample_image =  'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\setting.png'
    # case_image = './image/case/setting.png'
    # sample_image = './image/sample/setting.png'
    setting_menu =  '//*[@id="toolbar-menu-layer"]/div'
    name =          'setting' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath =       "./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content =       "The case 'test_setting': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)          
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t14"]'))).click()  #點擊上方setting(步驟)                                                   #點擊上方setting(步驟)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='一般設定']"))).click()  #點擊一般設定(步驟)                                                       
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    #匯出步驟及結果到新的表單
    time.sleep(2)
    screenshot.canvas_screenshot(driver,setting_menu,case_image) #截圖
    # time.sleep(2)
    # screenshot.canvas_screenshot(driver,setting_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image) #比對結果為Pass，匯出結果到新的表單
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image) #比對結果為fail，匯出結果到新的表單
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #關閉background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    #匯出步驟及結果到新的表單
    write_log.log(content + " End", logPath)


def test_cloud_intergration (driver):
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    # pathName =      './output sign in'
    # TestCase =      './登入'
    # step =          "截圖比對"
    case_image =    'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\cloud_intergration.png'
    sample_image =    'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\cloud_intergration.png'
    # case_image =    './image/case/cloud_intergration.png'
    # sample_image =  './image/sample/cloud_intergration.png'
    setting_menu =  '//*[@id="toolbar-menu-layer"]/div'
    name =          'cloud_intergration'
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath =       "./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content =       "The case 'test_cloud_intergration': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="t14"]'))).click() #點擊上方setting(步驟)         
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='雲端服務整合']"))).click()#點擊cloud_intergration(步驟)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    time.sleep(2)
    screenshot.canvas_screenshot(driver,setting_menu,case_image) 
    # time.sleep(2)
    # screenshot.canvas_screenshot(driver,setting_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)                              #比對結果為Pass，匯出結果到新的表單
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)                              #比對結果為Fail，匯出結果到新的表單
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #點擊X關閉視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    write_log.log(content +" End", logPath)

def test_about (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    # pathName =      './output sign in'
    # TestCase =      './登入'
    step =          "截圖比對"
    case_image =    'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\about.png'
    sample_image =    'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\about.png'
    # case_image =    './image/case/about.png'
    # sample_image =  './image/sample/about.png'
    setting_menu =  '//*[@id="toolbar-menu-layer"]/div'
    name =          'about'
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath =       "./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content =       "The case 'test_about': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t14"]')))    
    open_setting_bar = driver.find_element_by_xpath('//div[@aria-label="t14"]')  
    open_setting_bar.click()                                                    #點擊上方setting(步驟)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) #匯出步驟及結果到新的表單
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/ul/li[3]'))) 
    about = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/ul/li[3]')   
    about.click()                                                               #點擊about(步驟)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) #匯出步驟及結果到新的表單
    time.sleep(2)
    screenshot.canvas_screenshot(driver,setting_menu,case_image) 
    # time.sleep(2)
    # screenshot.canvas_screenshot(driver,setting_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_steps(TestCase)+"+"+step,TestCase_result(TestCase)+"+"+"Pass",case_image)     #比對結果為Pass，匯出結果到新的表單
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_steps(TestCase)+"+"+step,TestCase_result(TestCase)+"+"+"Fail",case_image)  #比對結果為Fail，匯出結果到新的表單
    close_menu = driver.find_element_by_css_selector('#toolbar-menu-layer > div > div._2BEMrkOJ > div._24gr4Mph') 
    close_menu.click()                                                          #點擊setting視窗 X(步驟)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  #匯出步驟及結果到新的表單
    write_log.log(content +" End", logPath)

def test_new_file (driver) :
    pathName =      './output sign in'
    TestCase =      './登入'
    step =          "截圖比對"
    case_image =    './image/case/new_file.png'
    sample_image =  './image/sample/new_file.png'
    new_file_menu = '/html/body/div[4]/div/div'
    name =          'new_file'
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath =       "./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content =       "The case 'test_new_file': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t8"]')))    
    new_file_management = driver.find_element_by_xpath('//div[@aria-label="t8"]')    #開啟file management視窗
    new_file_management.click()     
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/ul/li[1]'))) 
    new_file = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[1]')   
    new_file.click() 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,new_file_menu,case_image) 
    # screenshot.canvas_screenshot(driver,new_file_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
    close_menu = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/div[1]') #關閉開啟新檔menu
    close_menu.click()
    new_file_management.click()  
    write_log.log(content +" End", logPath)   

def test_open_file (driver) :
    case_image = './image/case/open_file.png'
    sample_image = './image/sample/open_file.png'
    open_file_menu = '//*[@id="toolbar-menu-layer"]/div[2]/div/div/div/div/ul'
    name = 'open_file'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_open_file': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t8"]')) 
                )    
    open_file_management = driver.find_element_by_xpath('//div[@aria-label="t8"]')    #開啟file management視窗
    open_file_management.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div[1]/ul/li[2]'))  #點選open file
                ) 
    open_file = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[1]/ul/li[2]')   
    open_file.click() 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,open_file_menu,case_image) 
    # screenshot.canvas_screenshot(driver,open_file_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
    open_file_management.click() #關閉file management視窗
    write_log.log(content + " End", logPath)

def test_export_file_loacal (driver) :
    case_image = './image/case/export_file.png'
    sample_image = './image/sample/export_file.png'
    export_file_menu = '/html/body/div[4]/div'
    name = 'export_file'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_export_file': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t8"]')) 
                )    
    export_file_management = driver.find_element_by_xpath('//div[@aria-label="t8"]')    #開啟file management視窗
    export_file_management.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/ul/li[3]'))  #點選export file
                ) 
    export_file = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[3]')   
    export_file.click() 
    local = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[2]/div/div/div/div/ul/li[1]')   
    local.click() 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,export_file_menu,case_image) 
    # screenshot.canvas_screenshot(driver,export_file_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
    close_menu = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]') #關閉選擇檔案格式menu
    close_menu.click()
    export_file_management.click() #關閉file management視窗
    write_log.log(content + " End", logPath)


    case_image1 = './image/case/export_to_PDF.png'
    sample_image1 = './image/sample/export_to_PDF.png'
    export_file_menu = '/html/body/div[5]/div/div'
    name = 'export_to_pdf_localdrive' 
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_export_to_pdf_localdrive': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t8"]')) 
                )    
    export_file_management = driver.find_element_by_xpath('//div[@aria-label="t8"]')    #開啟file management視窗
    export_file_management.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/ul/li[3]'))  #點選export file
                ) 
    export_file = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[3]')   
    export_file.click() 
    local = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div[2]/div/div/div/div/ul/li[1]')   #點選本機
    local.click()
    try:    
        expert_to_PDF = driver.find_element_by_css_selector('body > div.jss322 > div > div:nth-child(2) > div:nth-child(3)')   #點選另存至PDF
        expert_to_PDF.click()   
        time.sleep(2)
        screenshot.canvas_screenshot(driver,export_file_menu,case_image1) 
        # time.sleep(2)
        # screenshot.canvas_screenshot(driver,export_file_menu,sample_image1)
        compare = canvas_compare.canvas_compare(sample_image1,case_image1,name)
        if compare == True:
            print("Pass.............................................")
            write_log.log(content + " Pass.............................................", logPath) 
        else:
            print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        close_menu = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/div[1]/p') #關閉收費視窗
        close_menu.click()
    except:
         write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
         print(content+"Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
         pass
    WebDriverWait(driver, 20).until(                                
            EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t1f"]'))
        ) 
    close=driver.find_element_by_css_selector('body > div.jss322 > div > div.jss328 > div')#關閉檔案格式視窗
    close.click()
    export_file_management.click() #關閉file management視窗
    write_log.log(content + " End", logPath) 

def test_image_search (driver):
    case_image = './image/case/image_search.png'
    sample_image = './image/sample/image_search.png'
    image_search_menu = '//div[@aria-label="t33"]' 
    name = 'image_search' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_image_search': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)  
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕  
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t9"]')) 
                )    
    open_magic_box = driver.find_element_by_xpath('//div[@aria-label="t9"]')    #開啟magic box視窗
    open_magic_box.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.CSS_SELECTOR,'#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(3) > div > div > div > div'))  #點選image search
                ) 
    image_search = driver.find_element_by_css_selector('#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(3) > div > div > div > div')   
    image_search.click() 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]')) 
                )    
    click = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]')  
    click.click()                                                   #消除tool tip (不要focus在元件上) 點擊magic box選單下方
    time.sleep(3)
    screenshot.canvas_screenshot(driver,image_search_menu,case_image) 
    # screenshot.canvas_screenshot(driver,image_search_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t1f"]')) 
                )    
    close_magic_box = driver.find_element_by_xpath('//div[@aria-label="t1f"]')    #點X關閉magic box視窗
    close_magic_box.click()
    write_log.log(content + " End", logPath) 

def test_youtube (driver):
    case_image = './image/case/youtube.png'
    sample_image = './image/sample/youtube.png'
    youtube_menu = '//div[@aria-label="t33"]' 
    name = 'youtube' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_youtube': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)  
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t9"]')) 
                )    
    open_magic_box = driver.find_element_by_xpath('//div[@aria-label="t9"]')    #開啟magic box視窗
    open_magic_box.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.CSS_SELECTOR,'#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(4'))  #點選youtube
                ) 
    youtube = driver.find_element_by_css_selector('#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(4)')   
    youtube.click() 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]')) 
                )    
    click = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[3]')  
    click.click()                                                   #消除tool tip (不要focus在元件上) 點擊magic box選單下方
    time.sleep(3)
    screenshot.canvas_screenshot(driver,youtube_menu,case_image) 
    # screenshot.canvas_screenshot(driver,youtube_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t1f"]')) 
                )    
    close_magic_box = driver.find_element_by_xpath('//div[@aria-label="t1f"]')    #點X關閉magic box視窗
    close_magic_box.click()
    write_log.log(content + " End", logPath) 

def test_webpage (driver):
    case_image = './image/case/webpage.png'
    sample_image = './image/sample/webpage.png'
    webpage_menu = '//div[@aria-label="t33"]'      
    name = 'webpage'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_webpage': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t9"]'))    
                )    
    open_magic_box = driver.find_element_by_xpath('//div[@aria-label="t9"]')    #開啟magic box視窗
    open_magic_box.click()    
    time.sleep(2) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.CSS_SELECTOR,'#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(5'))  #點選image search
                ) 
    webpage = driver.find_element_by_css_selector('#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(5)')   
    webpage.click() 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/ul')) 
                )    
    click = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[2]/div/div/ul')  
    click.click()                                                   #消除tool tip (不要focus在元件上) 點擊magic box選單下方
    time.sleep(3)
    screenshot.canvas_screenshot(driver,webpage_menu,case_image) 
    # screenshot.canvas_screenshot(driver,webpage_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    open_magic_box.click()  #再點一次關閉magic box
    write_log.log(content + " End", logPath) 

def test_widget (driver):
    case_image = './image/case/widget.png'
    sample_image = './image/sample/widget.png'
    widget_menu = '/html/body/div[4]/div/div' 
    name = 'widget'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_widget': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t9"]')) 
                )    
    open_magic_box = driver.find_element_by_xpath('//div[@aria-label="t9"]')    #開啟magic box視窗
    open_magic_box.click()     
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.CSS_SELECTOR,'#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(6'))  #點選image search
                ) 
    widget = driver.find_element_by_css_selector('#toolbar-menu-layer > div > div:nth-child(1) > div._2B2e6IDj > div > div.slick-list > div > div:nth-child(6)')   
    widget.click() 
    
    time.sleep(3)
    screenshot.canvas_screenshot(driver,widget_menu,case_image) 
    # screenshot.canvas_screenshot(driver,widget_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    close_menu = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/div[1]') #關閉收費視窗
    close_menu.click()
    write_log.log(content + " End", logPath) 

def test_sticky_note (driver) :
    case_image = './image/case/sticky_note_menu.png'
    sample_image = './image/sample/sticky_note_menu.png'
    sticky_note_menu = '//*[@id="toolbar-menu-layer"]/div'
    name = 'sticky_note'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_sticky_note': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t2d"]')) 
                )                       
    sticky_note_management = driver.find_element_by_xpath('//div[@aria-label="t2d"]')    #開啟sticky note視窗
    sticky_note_management.click()  
    time.sleep(1)  
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上)
    time.sleep(2)
    screenshot.canvas_screenshot(driver,sticky_note_menu,case_image) 
    # screenshot.canvas_screenshot(driver,sticky_note_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    sticky_note_management.click() #關閉sticky note 視窗
    write_log.log(content + " End", logPath) 

def test_pen (driver):
    case_image = './image/case/pen.png'
    sample_image = './image/sample/pen.png'
    pen_menu = '//*[@id="toolbar-menu-layer"]/div' 
    name = 'pen' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案 
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_pen': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    pen = driver.find_element_by_xpath('//div[@aria-label="t2b"]')
    pen.click()
    try:
        WebDriverWait(driver, 2).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div'))
            )
    except:
        pen.click()
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕
    time.sleep(3)
    screenshot.canvas_screenshot(driver,pen_menu,case_image) 
    # screenshot.canvas_screenshot(driver,pen_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
    pen.click()   #再次點擊關閉視窗
    write_log.log(content + " End", logPath) 

def test_AI_pen (driver):
    case_image = './image/case/AI_pen.png'
    sample_image = './image/sample/AI_pen.png'
    AI_pen_menu = '/html/body/div[4]/div/div' 
    name = 'AI_pen' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案 
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_AI_pen': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    pen = driver.find_element_by_xpath('//div[@aria-label="t2b"]')
    pen.click()
    try:
        WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div'))
            )
    except:
        pen.click()                                                                         #開筆視窗
    time.sleep(2)
    AI_pen = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div[2]/div[4]')
    AI_pen.click()                                                                          #選AI_pen
    time.sleep(3)
    screenshot.canvas_screenshot(driver,AI_pen_menu,case_image) 
    # screenshot.canvas_screenshot(driver,AI_pen_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 

    close_menu = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/div[1]') #關閉收費視窗
    close_menu.click()
    pen.click()   #再次點擊關閉視窗
    write_log.log(content + " End", logPath) 

def test_eraser (driver):
    case_image = './image/case/eraser.png'
    sample_image = './image/sample/eraser.png'
    eraser_menu = '//*[@id="toolbar-menu-layer"]/div' 
    name = 'eraser'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_eraser': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    eraser = driver.find_element_by_xpath('//div[@aria-label="t2c"]')
    eraser.click()
    try:
        WebDriverWait(driver, 2).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div'))
            )
    except:
        eraser.click()                                                                         #開橡皮擦視窗
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕
    time.sleep(3)
    screenshot.canvas_screenshot(driver,eraser_menu,case_image) 
    # screenshot.canvas_screenshot(driver,eraser_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 

    eraser.click()   #再次點擊關閉視窗
    write_log.log(content + " End", logPath) 

def test_present_mode (driver):
    case_image = './image/case/present_mode.png'
    sample_image = './image/sample/present_mode.png'
    present_mode_menu = '//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[3]' 
    name = 'present_mode' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_present_mode': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)  
    present_mode = driver.find_element_by_xpath('//div[@aria-label="t31"]')
    present_mode.click()                                                       #進入present mode
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[3]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[3]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕
    
    time.sleep(3)
    screenshot.canvas_screenshot(driver,present_mode_menu,case_image) 
    # screenshot.canvas_screenshot(driver,present_mode_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 

    present_mode.click()     #退出present mode
    write_log.log(content + " End", logPath) 

def test_pagemanagement (driver):
    case_image = './image/case/pagemanagement.png'
    sample_image = './image/sample/pagemanagement.png'
    pagemanagement_menu = '/html/body/div[4]/div/div/div[1]' 
    name = 'pagemanagement'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_pagemanagement': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    pagemanagement = driver.find_element_by_xpath('//div[@aria-label="t29"]')
    pagemanagement.click()                                                       #開啟頁面管理器
    
    time.sleep(3)
    screenshot.canvas_screenshot(driver,pagemanagement_menu,case_image) 
    # screenshot.canvas_screenshot(driver,pagemanagement_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
    close_pagemanagement = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]')
    close_pagemanagement.click()      #關閉頁面管理器              
    write_log.log(content + " End", logPath)


def test_qrcode_share (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    # pathName ='./output sign in'
    # TestCase = './登入'
    step = "截圖比對"
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\qrcode_file.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\qrcode_file.png'
    # case_image = './image/case/setting.png'
    # sample_image = './image/sample/setting.png'
    qr_file_menu = '/html/body/div[4]/div/div'
    name = 'qrcode_file'
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath =       "./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_qrcode_file': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="t8"]'))).click() #開啟file management視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/ul/li[4]'))  #點選qr code share
                ) 
    qrcode_share = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[4]')   
    qrcode_share.click() 
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,qr_file_menu,case_image)  
    # time.sleep(2)
    screenshot.canvas_screenshot(driver,qr_file_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    cancal = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/div/div[1]') #關閉付費視窗(點擊取消)
    cancal.click()
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  
    write_log.log(content + " End", logPath)



def user_profile (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    # pathName ='./output sign in'
    # TestCase = './登入'
    step = "截圖比對"
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\user_profile.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\user_profile.png'
    # case_image = './image/case/user_profile.png'
    # sample_image = './image/sample/user_profile.png'
    user_profile_menu = '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div[8]/div'
    name = 'user_profile'
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_user_profile': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t15"]')) 
                )    
    user_profile = driver.find_element_by_xpath('//div[@aria-label="t15"]')    #開啟user profile視窗
    user_profile.click() 
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()                                                   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕    
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,user_profile_menu,case_image) 
    # time.sleep(2)
    screenshot.canvas_screenshot(driver,user_profile_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    user_profile.click()  #關閉user_profile視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    write_log.log(content + " End", logPath) 

def test_shapes (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\shapes.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\shapes.png'
    # case_image = './image/case/shapes.png'
    # sample_image = './image/sample/shapes.png'
    shapes_menu = '//*[@id="toolbar-menu-layer"]/div/div/div[2]'
    name = 'shapes'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_shapes': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                            
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2e"]')) 
                )                       
    shapes_management = driver.find_element_by_xpath('//div[@aria-label="t2e"]')    
    ActionChains(driver).double_click(shapes_management).perform()  #開啟(點擊兩下)shapes,lines,tables視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()  #消除tool tip (不要focus在元件上) 點擊上一頁按鈕
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,shapes_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,shapes_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   

    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    time.sleep(1)
    write_log.log(content + " End", logPath) 

def test_shapes_lines (driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\shapes_lines.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\shapes_lines.png'
    # case_image = './image/case/shapes_lines.png'
    # sample_image = './image/sample/shapes_lines.png'
    shapes_lines_menu = '//*[@id="toolbar-menu-layer"]/div/div/div[2]'
    name = 'shapes_lines'  
    logPath = "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_shapes_lines': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2e"]')) 
                )                       
    shapes_management = driver.find_element_by_xpath('//div[@aria-label="t2e"]')    
    ActionChains(driver).double_click(shapes_management).perform() #開啟(點擊兩下)shapes,lines,tables視窗
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    shapes_lines_management = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/div/div[2]/img') 
    shapes_lines_management.click() #點擊lines
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,shapes_lines_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,shapes_lines_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   

    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    time.sleep(1)    
    write_log.log(content + " End", logPath) 

def test_shapes_3Dshapes(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\shapes_3Dshapes.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\shapes_3Dshapes.png'
    # case_image = './image/case/shapes_3Dshapes.png'
    # sample_image = './image/sample/shapes_3Dshapes.png'
    shapes_3Dshapes_menu = '//*[@id="toolbar-menu-layer"]/div/div/div[2]'
    name = 'shapes_3Dshapes'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_3Dshapes': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2e"]')) 
                )                       
    shapes_management = driver.find_element_by_xpath('//div[@aria-label="t2e"]')    
    ActionChains(driver).double_click(shapes_management).perform() #開啟(點擊兩下)shapes,lines,tables視窗
    time.sleep(1)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    shapes_3Dshapes_management = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/div/div[3]/img') 
    shapes_3Dshapes_management.click() #點擊3Dshapes
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,shapes_3Dshapes_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,shapes_3Dshapes_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    time.sleep(1)
    write_log.log(content + " End", logPath) 

def test_shapes_tables(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\shapes_tables.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\shapes_tables.png'
    # case_image = './image/case/shapes_tables.png'
    # sample_image = './image/sample/shapes_tables.png'
    shapes_tables_menu = '//*[@id="toolbar-menu-layer"]/div/div/div[2]'
    name = 'shapes_tables' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案 
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_shapes_tables': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2e"]')) 
                )                       
    shapes_management = driver.find_element_by_xpath('//div[@aria-label="t2e"]')    
    ActionChains(driver).double_click(shapes_management).perform() #開啟(點擊兩下)shapes,lines,tables視窗
    time.sleep(1)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    shapes_lines_tables = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[1]/div[2]/div/div[4]/img') 
    shapes_lines_tables.click() #點擊tables
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,shapes_tables_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,shapes_tables_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    time.sleep(1)
    shapes_management.click() #關閉shapes,lines,tables視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    write_log.log(content + " End", logPath) 

def test_text(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\text.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\text.png'
    # case_image = './image/case/text.png'
    # sample_image = './image/sample/text.png'
    test_text_menu = '//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[9]/div[1]/div/div[2]/div/div[2]'
    name = 'text'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_text': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    # time.sleep(2)
    # WebDriverWait(driver, 10).until(                                
    #     EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
    #             )    
    # click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    # click_add_page.click()              #消除tool tip (不要focus在元件上) 點擊上一頁按鈕  
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="tc"]')) 
                )                       
    test_text_management = driver.find_element_by_xpath('//div[@aria-label="tc"]')    
    test_text_management.click()  #開啟text視窗
    time.sleep(1)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    test_text= driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div/div/div/div[3]/div/div/canvas[2]') 
    test_text.click() #點擊白板一處讓text功能顯示出來
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,test_text_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,test_text_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")   
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)  
    driver.find_element_by_xpath('//div[@aria-label="t1f"]').click()  #關閉text視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    write_log.log(content + " End", logPath) 
    
def test_background(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\background.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\background.png'
    # case_image = './image/case/background.png'
    # sample_image = './image/sample/background.png'
    background_menu = '//*[@id="toolbar-menu-layer"]/div'
    name = 'background'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_background': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath) 
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2f"]')) 
                )                       
    test_background_management = driver.find_element_by_xpath('//div[@aria-label="t2f"]')    
    test_background_management.click()  #開啟background視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    WebDriverWait(driver, 10).until(                                
        EC.presence_of_element_located((By.XPATH,'//div[@aria-label="t3"]')) 
                )    
    click_add_page = driver.find_element_by_xpath('//div[@aria-label="t3"]')  
    click_add_page.click()   #消除tool tip (不要focus在元件上) 點擊上一頁按鈕
    time.sleep(2)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    screenshot.canvas_screenshot(driver,background_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,background_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath) 
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)  
    test_background_management.click() #點擊background視窗，關閉
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    write_log.log(content + " End", logPath)  

def test_background_original(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\background_original.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\background_original.png'
    # case_image = './image/case/background_original.png'
    # sample_image = './image/sample/background_original.png'
    background_original_menu = '//*[@id="toolbar-menu-layer"]/div/div[1]'
    name = 'background_original' 
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_background_original': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)  
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
        EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2f"]')) 
                )                       
    test_background_management = driver.find_element_by_xpath('//div[@aria-label="t2f"]')    
    test_background_management.click() #開啟background視窗
    time.sleep(1)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)) 
    test_background_original = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[1]/div')    
    test_background_original.click()  #點擊background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    WebDriverWait(driver, 100).until(                                
    EC.presence_of_element_located((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div[2]/div[1]/ul/li[1]/div/div/p')) 
            )    #等待original背景出現
    screenshot.canvas_screenshot(driver,background_original_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,background_original_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #關閉background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    write_log.log(content + " End", logPath)

def test_background_googledrive(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\background_googledrive.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\background_googledrive.png'
    # case_image = './image/case/background_googledrive.png'
    # sample_image = './image/sample/background_googledrive.png'
    background_googledrive_menu = '//*[@id="toolbar-menu-layer"]/div/div/div[2]'
    name = 'background_googledrive'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_background_googledrive': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 100).until(                              
    EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2f"]')) 
                )                       
    test_background_management = driver.find_element_by_xpath('//div[@aria-label="t2f"]')  
    test_background_management.click()  #點擊background視窗  
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    time.sleep(1)                                              
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Google 雲端硬碟']"))).click() #開啟background_googledrive視窗
    # test_background_googledrive = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[2]/div')    
    # test_background_googledrive.click()  #開啟background_googledrive視窗
    WebDriverWait(driver, 100).until(                                
    EC.element_to_be_clickable((By.XPATH,'//*[@id="toolbar-menu-layer"]/div/div/div[2]/div[1]/div[1]/img')) 
            )    #等待googledrive背景可被點擊
    time.sleep(2)     
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    screenshot.canvas_screenshot(driver,background_googledrive_menu,case_image) 
    time.sleep(2) 
    screenshot.canvas_screenshot(driver,background_googledrive_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #關閉background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    write_log.log(content + " End", logPath)

def test_background_image_search(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\background_image_search.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\background_image_search.png'
    # case_image = './image/case/background_image_search.png'
    # sample_image = './image/sample/background_image_search.png'
    background_image_search_menu = '//*[@id="toolbar-menu-layer"]/div/div'
    name = 'background_image_search'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_background_image_search': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 100).until(                              
    EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2f"]')) 
                )                       
    test_background_management = driver.find_element_by_xpath('//div[@aria-label="t2f"]')   
    test_background_management.click()  #點擊background視窗   
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='圖片搜尋']"))).click() #開啟background_image_search視窗
    # test_background_googledrive = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[3]/div')    
    # test_background_googledrive.click()   #開啟background_image_search視窗
    time.sleep(3)  
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))    
    del_cursor = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/div/div[3]')    
    del_cursor.click()                #消除打字時候後面一閃一閃的小豎線
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  
    screenshot.canvas_screenshot(driver,background_image_search_menu,case_image) 
    time.sleep(2)
    screenshot.canvas_screenshot(driver,background_image_search_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #關閉background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))  
    write_log.log(content + " End", logPath)

def test_background_color(driver) :
    pathName = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\output sign in'
    TestCase = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\xlsx\\sign in'
    case_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\case\\background_color.png'
    sample_image = 'C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\image\\sample\\background_color.png'
    # case_image = './image/case/background_color.png'
    # sample_image = './image/sample/background_color.png'
    background_color_menu = '//*[@id="toolbar-menu-layer"]/div/div'
    name = 'background_color'  
    logPath =       "C:\\Users\\Liouki\\Viewsonic-AutoTest\\ClassroomAutoTestServer\\price tier\\log\\" + localTime + "_log.txt" #找位置生成空的txt檔案
    # logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
    content = "The case 'test_background_color': "
    logCheck.logAmountCheck()
    write_log.log(content + " Start", logPath)
    time.sleep(2)
    WebDriverWait(driver, 10).until(                              
    EC.element_to_be_clickable((By.XPATH,'//div[@aria-label="t2f"]')) 
                )                       
    test_background_management = driver.find_element_by_xpath('//div[@aria-label="t2f"]') 
    test_background_management.click()  #點擊background視窗  
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))       
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='底色']"))).click() ##開啟background_color視窗
    # test_background_googledrive = driver.find_element_by_xpath('//*[@id="toolbar-menu-layer"]/div/ul/li[4]/div')    
    # test_background_googledrive.click()  #開啟background_color視窗
    time.sleep(1)
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))               
    screenshot.canvas_screenshot(driver,background_color_menu,case_image) 
    time.sleep(2) 
    screenshot.canvas_screenshot(driver,background_color_menu,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,case_image,name)
    if compare == True:
        print("Pass.............................................")
        write_log.log(content + " Pass.............................................", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Pass",case_image)   
    else:
        print("Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  
        write_log.log(content + " Failxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", logPath)
        export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase)+"\n"+"Fail",case_image)   
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[class="active"]'))).click() #關閉background_original視窗
    export_table(pathName,TestCase_case(TestCase),TestCase_steps(TestCase),TestCase_result(TestCase))       
    write_log.log(content + " End", logPath)