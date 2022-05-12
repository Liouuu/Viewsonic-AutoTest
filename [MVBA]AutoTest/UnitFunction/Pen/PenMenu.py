from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Params.ElementParams import ElementParam


def SelectPenBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, ElementParam._Id_btnPen))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnPen').click()


def OpenPenMenu(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, ElementParam._Id_btnPen))
    )
    pen_btn = self.driver.find_element_by_id(ElementParam._Id_btnPen)
    if pen_btn.get_attribute("selected") == "true":
        pen_btn.click()
    else:
        pen_btn.click()
        time.sleep(1)
        pen_btn.click()


def ClosePenMenu(self):
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/buttonMenuClose').click()


def SelectMarker(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioPen))
    )
    self.driver.find_element_by_id('com.viewsonic.droid:id/radioPen').click()


def SelectHighlighter(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioHighlighter))
    )
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/radioHighlighter').click()


def SelectShapePen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioShapePen))
    )
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/radioShapePen').click()


def SelectMagicLinePen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioMagicLinePen))
    )
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/radioMagicLinePen').click()
