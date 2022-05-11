import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buttonDelete(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonDelete"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonDelete").click()

def buttonLocked(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonLocked"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonLocked").click()

def buttonHyperlink(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonHyperlink"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonHyperlink").click()

def buttonCopy(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonCopy"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonCopy").click()

def buttonCut(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonCut"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonCut").click()

def buttonReplicate(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonReplicate"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonReplicate").click()

def buttonMoveLayer(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonMoveLayer"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMoveLayer").click()

def buttonFlip(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonFlip"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonFlip").click()

def buttonMirror(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonMirror"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMirror").click()

def buttonSaveResource(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonSaveResource"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonSaveResource").click()

def buttonCrop(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonCrop"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonCrop").click()

def buttonFitToScreen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonFitToScreen"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonFitToScreen").click()

def buttonSetAsBackground(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonSetAsBackground"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonSetAsBackground").click()

def buttonStrokeWidth(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonStrokeWidth"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonStrokeWidth").click()

def seekBarStrokeWidth(self,val):   #調整粗細拉條, val=0~32
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/seekBarStrokeWidth"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/seekBarStrokeWidth").send_keys(str(val))

def buttonColor(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonColor"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonColor").click()

def buttonFill(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonFill"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonFill").click()

def buttonSnapshot(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonSnapshot"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonSnapshot").click()

def buttonTransparency(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonAlpha"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonAlpha").click() 

def seekBarAlpha(self, val):     #調整透明度拉條, val=0~255
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/seekBarAlpha"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/seekBarAlpha").send_keys(str(val))

def doFlip(self, dir="X"):  #dir = "X" or "Y"
    if not (dir=="X" or dir=="Y"):
        print("Function doFlip parameter wrong!")
        return
    tar = "com.viewsonic.droid:id/buttonFlip" + dir
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, tar))
    )
    self.driver.find_element_by_id(tar).click() 

def doMirror(self, dir="Right"):    #dir = "Top", "Bottom", "Left", "Right"
    if not (dir=="Right" or dir=="Left" or dir=="Top" or dir=="Bottom"):
        print("Function doMirror parameter wrong!")
        return
    tar = "com.viewsonic.droid:id/buttonMirror" + dir
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, tar))
    )
    self.driver.find_element_by_id(tar).click()