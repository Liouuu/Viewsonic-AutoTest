from typing import TYPE_CHECKING
from appium import webdriver
from openpyxl.drawing.image import Image
import Compare
from ElementParams import ElementParam, By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Library.LibLogHelper import LogPackage


class LibWebDriver:
    """WebDriver幫助類"""

# region Construct
    def __init__(self, driver: webdriver.Remote, blackBox: LogPackage):
        self.Driver = driver
        self.BlackBox = blackBox

    def __init__(self, desired_caps: dict, blackBox: LogPackage):
        self.__init__(webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps), blackBox)

    def __init__(self, isActivate: bool, blackBox: LogPackage):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = '172.21.13.194:5555'
        desired_caps['appPackage'] = ElementParam._Site
        desired_caps['appActivity'] = '.MainActivity'
        if(isActivate):
            desired_caps["automationName"] = 'UiAutomator2'
            desired_caps['noReset'] = True
            desired_caps['resetKeyboard'] = True
            desired_caps['unicodeKeyboard'] = True
        else:
            desired_caps['noReset'] = False
        self.__init__(desired_caps, blackBox)
# endregion

# region Public
    # 以下方法應該要移至UnitTest分類...待處理
    def ElementClick(self, sheetName, action, element: str, type: By):
        """點擊Element元件"""
        self.blackbox.AddUnitLog(sheetName, action, "點擊按鈕", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        if type is By.ID:
            self.Driver.find_element_by_id(element).click()
        elif type is By.XPATH:
            self.Driver.find_element_by_xpath(element).click()

    def ElementSetValue(self, sheetName, action, val: str, element: str, type: By):
        """設置Element值"""
        self.blackbox.AddUnitLog(
            sheetName, action, "$設值：{val} ", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        if type is By.ID:
            self.Driver.find_element_by_id(element).send_keys(val)
        elif type is By.XPATH:
            self.Driver.find_element_by_xpath(element).send_keys(val)

    def ScreenshotAndCompare(self, srcPic, element: str, type: By):
        """截圖，並比較是否和原圖一致"""
        dstImg = self.Screenshot(element, type)
        srcImg = srcPic
        isSame = Compare.isImgEqual(dstImg, srcImg)
        return (isSame, dstImg)

    def Screenshot(self, sheetName, action, element, type: By):
        """根據元素截圖"""
        self.blackbox.AddUnitLog(sheetName, action, "截圖", element, type)
        img = Image()
        if(type is By.XPATH):
            self.__ScreenshotByXpath(element)
        elif(type is By.ID):
            self.__ScreenshotById(element)
        return self.__SetPictureSize(img)
# endregion

# region Private
    def __SetPictureSize(img: Image):
        """重新調整圖片大小，若高度超過135pixel，則照比例縮小"""
        if img.height * 3/4 >= 135:
            n = img.height/180
            img.width, img.height = img.width/n, img.height/n
        return img

    def __ScreenshotByXpath(self, xpath):
        """根據xpath截圖"""
        base64 = self.Driver.find_element_by_xpath(
            xpath).screenshot_as_base64()
        return Image(base64)

    def __ScreenshotById(self, id):
        """根據id截圖"""
        base64 = self.Driver.find_element_by_id(id).screenshot_as_base64()
        return Image(base64)
# endregion
