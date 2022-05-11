from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def OpenBackgroundManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/btnBackground"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/btnBackground").click()

def CloseBackgroundManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonMenuClose"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMenuClose").click()

def SelectBackgroundMenu(self ,menu:str="color"):   #menu="color"/ "preinstalled"/ "originals"/ "saved"/ "follow me"
    if menu == "color":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioColor"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/radioColor").click()
    elif menu == "preinstalled":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioBuiltin"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/radioBuiltin").click()
    elif menu == "originals":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioOriginalContent"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/radioOriginalContent").click()
    elif menu == "saved":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioLocalBG"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/radioLocalBG").click()
    elif menu == "follow me":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioFollowMeBG"))
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/radioFollowMeBG").click()

def ChangeByColor(self, index):
    color_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(index)+"]"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, color_xpath))
    )
    self.driver.find_element_by_xpath(color_xpath).click()

def OpenMoreColor(self):
    ChangeByColor(self, 24)

def ChangeByPreinstalled(self, index, mode="this page"):    #mode="this page"/ "all pages"
    bg_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(index)+"]"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, bg_xpath))
    )
    self.driver.find_element_by_xpath(bg_xpath).click()
    if mode=="this page":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonNeutral")) #RD named the ID of "this page" button with "buttonNeutral"
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonNeutral").click()
    if mode=="all pages":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonCancel"))  #RD named the ID of "all pages" button with "buttonCancel"
        )
        self.driver.find_element_by_id("com.viewsonic.droid:id/buttonCancel").click()   

def ChangeByOriginals(self, index, mode="this page"):
    ChangeByPreinstalled(self, index, mode)

def ChangeBySaved(self, index, mode="this page"):
    pass

def DeleteSavedBackgound(self, index):
    pass

def AddBackgroundImg(self):
    pass

def ClickGridBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkGridLine"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkGridLine").click()

def ClickWatermarkBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkWaterMark"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkWaterMark").click()