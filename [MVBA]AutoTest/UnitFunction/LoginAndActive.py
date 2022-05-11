from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Activate(self, name, email, emailC):  

    WebDriverWait(self.driver, 10).until(                                #等待(最多10秒)，等到ID為"com.viewsonic.droid:id/textActivate"的element出現才繼續進行
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/textActivate"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/textActivate").click()   #點擊'啟用'

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonPersonal"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonPersonal").click() #點擊'個人'

    WebDriverWait(self.driver, 10).until(                                 #裝置非Chromebook或未開啟Google自動填充請註解此段
        EC.presence_of_element_located((By.ID, "android:id/button2"))
    )
    self.driver.find_element_by_id("android:id/button2").click()    #對google自動填入點擊'取消'

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/editName"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/editName").send_keys(name)   #輸入數位教室名稱
    self.driver.find_element_by_id("com.viewsonic.droid:id/editEmail").send_keys(email)     #輸入信箱
    self.driver.find_element_by_id("com.viewsonic.droid:id/editEmailC").send_keys(emailC)   #輸入信箱確認
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonSubmit").click()   #點擊'提交'

    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonOk"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonOk").click()   #點擊'好'

def NormalLogin(self, email, pw):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/editSignInEmail"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/editSignInEmail").send_keys(email)   #輸入信箱
    self.driver.find_element_by_id("com.viewsonic.droid:id/editSignInPassword").send_keys(pw)   #輸入密碼
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonSubmit").click()      #點擊'V'