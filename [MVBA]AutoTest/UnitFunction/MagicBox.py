from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
from Params.ElementParams import ElementParam


def OpenMagicBox(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnResource))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnResource).click()


def CloseMagicBox(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonMenuClose))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonMenuClose).click()


# Select a file or a folder, the parameter index is the file index in current folder
def SelectFile(self, index):
    tar_path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout"
    tar_index = '['+str(index)+']'
    tar_path += tar_index
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located((By.XPATH, tar_path))
    )
    tar = self.driver.find_element_by_xpath(tar_path)
    double_click = TouchAction(self.driver)
    double_click.tap(tar, count=2).perform()
    # time.sleep(2)


def LastFolder(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_currentFolder))
    )
    cur_folder = self.driver.find_element_by_id(
        ElementParam._Id_currentFolder)
    double_click = TouchAction(self.driver)
    double_click.tap(element=cur_folder, count=2).perform()


# Import all img files under current folder #Files can only be audio, video, img
def ImportAllFiles(self):
    # time.sleep(5)
    #all_files = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
    WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"))
    )
    all_files = self.driver.find_elements_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/*")
    # print(len(all_files))
    for i in range(len(all_files)):
        SelectFile(self, i+1)


def SelectStorage(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioLocalStorage))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioLocalStorage).click()


def SelectGoogleDrive(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioGoogleDrive))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioGoogleDrive).click()


def SelectOneDrive(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioOneDrive))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioOneDrive).click()


def SelectOneDriveForBusiness(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioOneDriveBusiness))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioOneDriveBusiness).click()


def SelectDropBox(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioDropBox))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioDropBox).click()


def SelectBox(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioBox))
    )
    self.driver.find_element_by_id(ElementParam._Id_radioBox).click()


def ChooseFileType(self, type):  # the parameter type is a string: 'img', 'video' or 'audio'
    if type == "img":
        self.driver.find_element_by_id(
            ElementParam._Id_radioImage).click()
    elif type == "video":
        self.driver.find_element_by_id(
            ElementParam._Id_radioVideo).click()
    elif type == "audio":
        self.driver.find_element_by_id(
            ElementParam._Id_radioAudio).click()
    else:
        print("CooseFileType wrong")


def SelectImageSearch(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioImageSearch))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioImageSearch).click()
