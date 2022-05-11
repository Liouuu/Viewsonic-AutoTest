from UnitFunction import Canvas
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def SelectObject(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnLasso"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnLasso").click()


def OpenFileManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnFile"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnFile").click()


def OpenMagicBox(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnResource"))
    )
    self.driver.find_element_by_id(
        "com.viewsonic.droid:id/btnResource").click()


def SelectShapeBtn(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnShape"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnShape").click()


def SelectPenBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnPen"))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPen').click()


def SelectEraserBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/btnEraser"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnEraser").click()
