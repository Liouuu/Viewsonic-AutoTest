from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam


def ClickStickynote(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioSticky))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioSticky).click()


def StickynoteColor(self, index: int):  # index: 1~4 or 2~5
    xpath = '(//android.widget.ImageView[@content-desc="Whiteboard"])[' + str(
        index+1) + ']'
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    self.driver.find_element_by_xpath(xpath).click()


def SelectText(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonTypingText))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonTypingText).click()


def SelectPen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonPen))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonPen).click()


def ChangeFont(self, index: int):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_spinnerFontName))
    )
    self.driver.find_element_by_id(ElementParam._Id_spinnerFontName).click()
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']'))
    )
    self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']').click()


def ChangeSize(self, index: int):  # 1-28
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_spinnerFontSize))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_spinnerFontSize).click()
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']'))
    )
    self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']').click()


def TextBold(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkBold))
    )
    self.driver.find_element_by_id(ElementParam._Id_checkBold).click()


def TextItalic(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkItalic))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkItalic).click()


def TextUnderLine(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_checkUnderline))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_checkUnderline).click()


def TypeText(self, string: str):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_sticky_note_canvas))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_sticky_note_canvas).click()
    for char in string:
        if char >= 'a' and char <= 'z':
            keycode = str(29 + (ord(char)-ord('a')))
            self.driver.press_keycode(keycode)


def PenColor(self, color: str):  # colr: "Black", "Red", "Blue", "DarkGreen", "Gray"
    color_id = ElementParam._Id_drawColor + color
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, color_id))
    )
    self.driver.find_element_by_id(color_id).click()


def PenThickness(self, value: int):  # value: 1~12
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarWidthHighlighter))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarWidthHighlighter).send_keys(str(value))


def CloseStickynote(self):
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
