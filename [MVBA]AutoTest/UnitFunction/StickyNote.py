from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ClickStickynote(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/radioSticky"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/radioSticky").click()

def StickynoteColor(self, index:int):   #index: 1~4 or 2~5
    xpath = '(//android.widget.ImageView[@content-desc="Whiteboard"])[' + str(index+1) + ']'
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    self.driver.find_element_by_xpath(xpath).click()

def SelectText(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonTypingText"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonTypingText").click()
def SelectPen(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/buttonPen"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonPen").click()

def ChangeFont(self, index:int):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/spinnerFontName"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/spinnerFontName").click()
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']'))
        )
    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']').click()

def ChangeSize(self, index:int): #1-28
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/spinnerFontSize"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/spinnerFontSize").click()
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']'))
        )
    self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView['+str(index)+']').click()

def TextBold(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkBold"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkBold").click()


def TextItalic(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkItalic"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkItalic").click()


def TextUnderLine(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/checkUnderline"))
        )
    self.driver.find_element_by_id("com.viewsonic.droid:id/checkUnderline").click()

def TypeText(self, string:str):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/sticky_note_canvas"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/sticky_note_canvas").click()
    for char in string:
        if char>='a' and char<='z':
            keycode = str(29 + (ord(char)-ord('a')))
            self.driver.press_keycode(keycode)

def PenColor(self, color:str):  #colr: "Black", "Red", "Blue", "DarkGreen", "Gray"
    color_id = "com.viewsonic.droid:id/drawColor" + color
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, color_id))
    )
    self.driver.find_element_by_id(color_id).click()

def PenThickness(self, value:int):  #value: 1~12
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "com.viewsonic.droid:id/seekBarWidthHighlighter"))
    )
    self.driver.find_element_by_id("com.viewsonic.droid:id/seekBarWidthHighlighter").send_keys(str(value))

def CloseStickynote(self):
    self.driver.find_element_by_id("com.viewsonic.droid:id/buttonMenuClose").click()