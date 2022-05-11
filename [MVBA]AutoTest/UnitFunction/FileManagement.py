import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

def OpenFileManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnFile"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnFile").click()

def CloseFileManagement(self):
    try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonMenuClose"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMenuClose").click()
    except:
        pass

def ChooseOpenFile(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioFileOpen"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/radioFileOpen").click()

def SelectFile(self, index):    #Select a file or a folder, the parameter index is the file index in current folder
    tar_path = '(//android.widget.ImageView[@content-desc="Whiteboard"])'
    tar_index = '['+str(index)+']'
    tar_path += tar_index
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, tar_path))
    )
    tar = self.driver.find_element_by_xpath(tar_path)
    #double_click = TouchAction(self.driver)
    #double_click.tap(tar,count=2).perform()
    tar.click()
    tar.click()
    time.sleep(2)

def NewFile(self):
    pass

def Save(self):
    pass

def SaveAs(self):
    pass

def Export(self, type:str):
    pass

def QRcodeShare(self):
    pass