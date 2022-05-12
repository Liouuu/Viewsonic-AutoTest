from Params.ElementParams import ElementParam
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import sys
import os
from UnitFunction import Canvas
sys.path.append(os.getcwd())


def SelectTextBtn(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnTypingText))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_btnTypingText).click()


def TypeText(self, string: str):  # string can accept lower case a~z only
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_editText))
    )
    self.driver.find_element_by_id(ElementParam._Id_editText).click()
    for char in string:
        if char >= 'a' and char <= 'z':
            keycode = str(29 + (ord(char)-ord('a')))
            self.driver.press_keycode(keycode)


def ChangeFont(self, index: int):  # index of font is 1~9
    font_selector_id = ElementParam._Id_spinnerFontName
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, font_selector_id))
    )
    self.driver.find_element_by_id(font_selector_id).click()
    time.sleep(1)
    font_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(
        index) + "]"
    self.driver.find_element_by_xpath(font_xpath).click()


def ChangeSize(self, index: int):  # index of size is 1~
    size_selector_id = ElementParam._Id_spinnerFontSize
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, size_selector_id))
    )
    self.driver.find_element_by_id(size_selector_id).click()
    time.sleep(1)
    size_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(
        index) + "]"
    self.driver.find_element_by_xpath(size_xpath).click()


def Bold(self):  # 粗體
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkBold))
    )
    self.driver.find_element_by_id(ElementParam._Id_checkBold).click()


def Italic(self):  # 斜體
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkItalic))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkItalic).click()


def UnderLine(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkUnderline))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkUnderline).click()


def edittextclear(self, text):  # this function is designed for ChangeColorByAdvanced function
    self.driver.press_keycode('123')
    for i in range(0, len(text)):
        self.driver.press_keycode('67')


# type is "Standard" or "Advanced", Color num(1~17) for Standard and RGBA(0~255) for Advanced
def ChangeColor(self, type: str = "Standard", ColorNum: int = 1, R=255, G=255, B=255, A=255):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonColor))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonColor).click()
    if type == "Standard":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonStandard))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonStandard).click()
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
    elif type == "Advanced":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonAdvanced))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonAdvanced).click()
        for i in range(4):
            pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + \
                "[" + str(i+1) + "]" + \
                "/android.view.ViewGroup/android.widget.EditText"
            pattern = self.driver.find_element_by_xpath(pattern_xpath)
            if str(i+1) == "1":
                pattern.click()
                context1 = pattern.get_attribute('text')
                edittextclear(self, context1)
                pattern.send_keys(R)
                self.driver.press_keycode('66')

            elif str(i+1) == "2":
                pattern.click()
                context2 = pattern.get_attribute('text')
                edittextclear(self, context2)
                pattern.send_keys(G)
                self.driver.press_keycode('66')
            elif str(i+1) == "3":
                pattern.click()
                context3 = pattern.get_attribute('text')
                edittextclear(self, context3)
                pattern.send_keys(B)
                self.driver.press_keycode('66')
            else:
                pattern.click()
                context4 = pattern.get_attribute('text')
                edittextclear(self, context4)
                pattern.send_keys(A)
                self.driver.press_keycode('66')
        Canvas.Tap(self, 1900, 500)


# type is "Standard" or "Advanced", Color num(1~17) for Standard and RGBA(0~255) for Advanced
def ChangeColorBg(self, type: str = "Standard", ColorNum: int = 1, R=255, G=255, B=255, A=255):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonColorBg))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonColorBg).click()
    if type == "Standard":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonStandard))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonStandard).click()
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
    elif type == "Advanced":
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_buttonAdvanced))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_buttonAdvanced).click()
        for i in range(4):
            pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + \
                "[" + str(i+1) + "]" + \
                "/android.view.ViewGroup/android.widget.EditText"
            pattern = self.driver.find_element_by_xpath(pattern_xpath)
            if str(i+1) == "1":
                pattern.click()
                context1 = pattern.get_attribute('text')
                edittextclear(self, context1)
                pattern.send_keys(R)
                self.driver.press_keycode('66')

            elif str(i+1) == "2":
                pattern.click()
                context2 = pattern.get_attribute('text')
                edittextclear(self, context2)
                pattern.send_keys(G)
                self.driver.press_keycode('66')
            elif str(i+1) == "3":
                pattern.click()
                context3 = pattern.get_attribute('text')
                edittextclear(self, context3)
                pattern.send_keys(B)
                self.driver.press_keycode('66')
            else:
                pattern.click()
                context4 = pattern.get_attribute('text')
                edittextclear(self, context4)
                pattern.send_keys(A)
                self.driver.press_keycode('66')
        Canvas.Tap(self, 1900, 500)


def Superscript(self):  # 上標
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkUpscript))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkUpscript).click()


def Subscript(self):  # 下標
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkDownscript))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkDownscript).click()


def AlignLeft(self):  # 靠左對齊
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkAlignLeft))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkAlignLeft).click()


def AlignRight(self):  # 靠右對齊
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkAlignRight))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkAlignRight).click()


def Center(self):  # 置中
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkAlignCenter))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkAlignCenter).click()


def List(self):  # 條列項目
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkBulleted))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkBulleted).click()


def AddIdent(self):  # 縮排
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonIncIndent))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonIncIndent).click()


def ReduceIdent(self):  # 減少縮排
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonDecIndent))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonDecIndent).click()


def CloseEditor(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonMenuClose))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
