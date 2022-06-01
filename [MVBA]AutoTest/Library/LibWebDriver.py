import time
from typing import TYPE_CHECKING
from appium import webdriver
from openpyxl.drawing.image import Image
import Library.Compare as Compare
from Params.ElementParams import ElementParam
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from Library.LibLogHelper import LogPackage
import subprocess


class LibWebDriver:
    """WebDriver幫助類"""

# region Construct
    def __init__(self, driver: webdriver.Remote, log: LogPackage):
        self.Driver = driver
        self.Log = log
        self.Touch = TouchAction(self.Driver)

    @classmethod
    def bydesired(self, desired_caps: dict, log: LogPackage):
        # def __init__(self, desired_caps: dict, blackBox: LogPackage):
        # 自動連線
        subprocess.Popen("adb connect "+"172.21.13.194", shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return self(driver, log)

    @classmethod
    def default(self, isActivate: bool, log: LogPackage):
        # def __init__(self, isActivate: bool, blackBox: LogPackage):
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
        return self.bydesired(desired_caps, log)
        # self.__init__(desired_caps, blackBox)
# endregion

# region Public
    # 以下方法應該要移至UnitTest分類...待處理
    def ElementClick(self, action, element: str, type: By):
        """點擊Element元件"""
        self.Log.AddUnitLog(action, "點擊按鈕", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        if type is By.ID:
            self.Driver.find_element_by_id(element).click()
        elif type is By.XPATH:
            self.Driver.find_element_by_xpath(element).click()

    def ElementSetValue(self,  action, val: str, element: str, type: By):
        """設置Element值"""
        self.Log.AddUnitLog(action, "$設值：{val} ", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        if type is By.ID:
            self.Driver.find_element_by_id(element).send_keys(val)
        elif type is By.XPATH:
            self.Driver.find_element_by_xpath(element).send_keys(val)

    def ElementClcikMenu(self,  action, element: str, type: By):
        """設置Element值"""
        self.Log.AddUnitLog(action, "$設值：{val} ", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        btn = self.driver.find_element_by_id(element)
        if btn.get_attribute("selected") == "true":
            btn.click()
        else:
            btn.click()
            time.sleep(1)
            btn.click()

    def ElementClcikNotMenu(self,  action, element: str, type: By):
        """設置Element值"""
        self.Log.AddUnitLog(action, "$設值：{val} ", element, type)
        WebDriverWait(self.Driver, 10).until(
            EC.presence_of_element_located((type, element)))
        btn = self.Driver.find_element_by_id(element)
        if btn.get_attribute("selected") == "true":
            pass
        else:
            btn.click()

    def ScreenshotAndCheck(self, src, element: str, elementType: By,):  # 待處理這段
        """將整個Canvas截圖並驗證"""
        action = "將整個Canvas截圖並驗證"
        self.Log.AddUnitLog(action, "將整個Canvas截圖並驗證", element, type)
        self.Driver.ScreenshotAndCompare(src, element, elementType)

    def ScreenshotAndCompare(self, srcPic, element: str, type: By):
        """截圖，並比較是否和原圖一致"""
        dstImg = self.Screenshot(element, type)
        srcImg = srcPic
        isSame = Compare.isImgEqual(dstImg, srcImg)
        return (isSame, dstImg)

    def Screenshot(self,  action, element, type: By):
        """根據元素截圖"""
        self.Log.AddUnitLog(action, "截圖", element, type)
        img = Image()
        if(type is By.XPATH):
            self.__ScreenshotByXpath(element)
        elif(type is By.ID):
            self.__ScreenshotById(element)
        return self.__SetPictureSize(img)

    def Tap(self, x, y):
        self.Touch.press(x=x, y=y).release().perform()

    def Swipe(self, positions: list):
        step = None
        for i, j in positions:
            if(step is None):
                step = self.Touch.press(x=i, y=j)
            else:
                step = step.move_to(x=i, y=j)
        step.release().perform()
        # T = True
        # MOV = "touch.press(x="+str(args[0][0])+",y="+str(args[0][1])+")"
        # i = 1
        # while T == True:
        #     MOV = MOV+".move_to(x="+str(args[i][0])+",y="+str(args[i][1])+")"
        #     i += 1
        #     if i >= len(args):
        #         MOV = MOV+".release().perform()"
        #         break
        # exec(MOV)

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
