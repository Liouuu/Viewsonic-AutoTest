from mimetypes import init
from appium import webdriver
from openpyxl.drawing.image import Image
from ElementParams import ElementParam, ElementType


class LibWebDriver:
    """WebDriver幫助類"""

# region Construct
    def __init__(self, driver: webdriver.Remote):
        self.Driver = driver

    def __init__(self, desired_caps: dict):
        self.__init__(webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps))

    def __init__(self, isActivate: bool):
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
        self.__init__(desired_caps)
# endregion

# region Public
    def Screenshot(self, element, type: ElementType):
        """根據元素截圖"""
        img = Image()
        if(type is ElementType.XPath):
            self.__ScreenshotByXpath(element)
        elif(type is ElementType.Id):
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
