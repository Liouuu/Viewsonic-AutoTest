import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam


def buttonDelete(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, ElementParam._Id_buttonDelete))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonDelete).click()


def buttonLocked(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonLocked))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonLocked).click()


def buttonHyperlink(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonHyperlink))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonHyperlink).click()


def buttonCopy(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonCopy))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonCopy).click()


def buttonCut(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam.buttonCut))
    )
    self.driver.find_element_by_id(ElementParam.buttonCut).click()


def buttonReplicate(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam.buttonReplicate))
    )
    self.driver.find_element_by_id(
        ElementParam.buttonReplicate).click()


def buttonMoveLayer(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam.buttonMoveLayer))
    )
    self.driver.find_element_by_id(
        ElementParam.buttonMoveLayer).click()


def buttonFlip(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonFlip))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonFlip).click()


def buttonMirror(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonMirror))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMirror).click()


def buttonSaveResource(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonSaveResource))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonSaveResource).click()


def buttonCrop(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonCrop))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonCrop).click()


def buttonFitToScreen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonFitToScreen))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonFitToScreen).click()


def buttonSetAsBackground(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonSetAsBackground))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonSetAsBackground).click()


def buttonStrokeWidth(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonStrokeWidth))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonStrokeWidth).click()


def seekBarStrokeWidth(self, val):  # 調整粗細拉條, val=0~32
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarStrokeWidth))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarStrokeWidth).send_keys(str(val))


def buttonColor(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonColor))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonColor).click()


def buttonFill(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonFill))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonFill).click()


def buttonSnapshot(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonSnapshot))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonSnapshot).click()


def buttonTransparency(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonAlpha))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonAlpha).click()


def seekBarAlpha(self, val):  # 調整透明度拉條, val=0~255
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarAlpha))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarAlpha).send_keys(str(val))


def doFlip(self, dir="X"):  # dir = "X" or "Y"
    if not (dir == "X" or dir == "Y"):
        print("Function doFlip parameter wrong!")
        return
    tar = ElementParam._Id_buttonFlip + dir
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, tar))
    )
    self.driver.find_element_by_id(tar).click()


def doMirror(self, dir="Right"):  # dir = "Top", "Bottom", "Left", "Right"
    if not (dir == "Right" or dir == "Left" or dir == "Top" or dir == "Bottom"):
        print("Function doMirror parameter wrong!")
        return
    tar = ElementParam._Id_buttonMirror + dir
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, tar))
    )
    self.driver.find_element_by_id(tar).click()
