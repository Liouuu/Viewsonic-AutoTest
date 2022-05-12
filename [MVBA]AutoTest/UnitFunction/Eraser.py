import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Params.ElementParams import ElementParam


def SelectEraserBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnEraser))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnEraser).click()


def OpenEraserMenu(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnEraser))
    )
    eraser_btn = self.driver.find_element_by_id(
        ElementParam._Id_btnEraser)
    if eraser_btn.get_attribute("selected") == "true":
        eraser_btn.click()
    else:
        eraser_btn.click()
        time.sleep(1)
        eraser_btn.click()


def CloseEraserMenu(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonMenuClose))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonMenuClose).click()


def ChooseRegularEraser(self):  # in eraser menu
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnEraser))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnEraser).click()


def ChooseCircleEraser(self):  # in eraser menu
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonEraseSelector))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonEraseSelector).click()


def ClearCanvas(self):  # in eraser menu
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonEraseAll))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonEraseAll).click()


# in main bar after click eraser btn one time
def ChooseRegularEraser_Sub(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnSubEraserEraser))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnSubEraserEraser).click()


def ChooseCircleEraser_Sub(self):  # in main bar after click eraser btn one time
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnSubEraserSelector))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnSubEraserSelector).click()


def ClearCanvas_Sub(self):  # in main bar after click eraser btn one time
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnSubEraserEraserAll))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnSubEraserEraserAll).click()


def AdjustEraserSize(self, val: int):  # val range: 0~40
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBar))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBar).send_keys(str(val))


# args are a list of points: [[292,346],[117,238],[108,353],[265,457],[204,572],[115,518]], duration is time to take the swipe
def Swipe(self, args: list, duration: int):
    for i in range(len(args)-1):
        self.driver.swipe(args[i][0], args[i][1],
                          args[i+1][0], args[i+1][1], duration)
    time.sleep(2)
