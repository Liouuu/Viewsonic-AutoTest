import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam


def Paste(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, ElementParam._Id_btnPaste))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnPaste).click()


def NewPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnPageAdd))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPageAdd').click()


def NextPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnPageNext))
    )
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/btnPageNext').click()


def LastPage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnPagePrev))
    )
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/btnPagePrev').click()
