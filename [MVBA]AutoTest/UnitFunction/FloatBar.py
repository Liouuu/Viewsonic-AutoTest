import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Paste(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnPaste"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnPaste").click()

def NewPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnPageAdd"))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPageAdd').click() 

def NextPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnPageNext"))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPageNext').click()

def LastPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnPagePrev"))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPagePrev').click()