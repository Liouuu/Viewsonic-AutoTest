from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam


def OpenBackgroundManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnBackground))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnBackground).click()


def CloseBackgroundManagement(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonMenuClose))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonMenuClose).click()


# menu="color"/ "preinstalled"/ "originals"/ "saved"/ "follow me"
def SelectBackgroundMenu(self, menu: str = "color"):
    if menu == "color":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioColor))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_radioColor).click()
    elif menu == "preinstalled":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioBuiltin))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_radioBuiltin).click()
    elif menu == "originals":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioOriginalContent))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_radioOriginalContent).click()
    elif menu == "saved":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioLocalBG))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_radioLocalBG).click()
    elif menu == "follow me":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioFollowMeBG))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_radioFollowMeBG).click()


def ChangeByColor(self, index):
    color_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(
        index)+"]"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, color_xpath))
    )
    self.driver.find_element_by_xpath(color_xpath).click()


def OpenMoreColor(self):
    ChangeByColor(self, 24)


# mode="this page"/ "all pages"
def ChangeByPreinstalled(self, index, mode="this page"):
    bg_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(
        index)+"]"
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, bg_xpath))
    )
    self.driver.find_element_by_xpath(bg_xpath).click()
    if mode == "this page":
        WebDriverWait(self.driver, 10).until(
            # RD named the ID of "this page" button with "buttonNeutral"
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonNeutral))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonNeutral).click()
    if mode == "all pages":
        WebDriverWait(self.driver, 10).until(
            # RD named the ID of "all pages" button with "buttonCancel"
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonCancel))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonCancel).click()


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
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkGridLine))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkGridLine).click()


def ClickWatermarkBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkWaterMark))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkWaterMark).click()
