from Params.ElementParams import ElementParam
from UnitFunction import Canvas
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def SelectObject(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnLasso))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnLasso).click()


def OpenFileManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnFile))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnFile).click()


def OpenMagicBox(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnResource))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnResource).click()


def SelectShapeBtn(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnShape))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnShape).click()


def SelectPenBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnPen))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPen').click()


def SelectEraserBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnEraser))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnEraser).click()
