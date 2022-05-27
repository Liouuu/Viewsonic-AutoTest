from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Params.ElementParams import ElementParam


def OpenShapeMenu(self):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnShape))
    )
    shape_btn = self.driver.find_element_by_id(
        ElementParam._Id_btnShape)
    if shape_btn.get_attribute("selected") == "true":
        shape_btn.click()
    else:
        shape_btn.click()
        time.sleep(1)
        shape_btn.click()


def CloseMenu(self):
    self.driver.find_element_by_id(
        'com.viewsonic.droid:id/buttonMenuClose').click()


def SelectShape(self, ShapeNum):  # ShapeNum: 1 for shape, 2 for 3D shape, 3 for lines
    if ShapeNum == 1:  # Shape ##
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioShape))
        )
        self.driver.find_element_by_id(
            'com.viewsonic.droid:id/radioShape').click()
    elif ShapeNum == 2:  # 3D Shape ##
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioPseudo3DShape))
        )
        self.driver.find_element_by_id(
            'com.viewsonic.droid:id/radioPseudo3DShape').click()
    elif ShapeNum == 3:  # Lines ##
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_radioLines))
        )
        self.driver.find_element_by_id(
            'com.viewsonic.droid:id/radioLines').click()


def SelectPattern(self, Num):  # Num 1-18
    try:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']'))
        )
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()
    except:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()


def ChangeColor(self, ColorNum):  # ColorNum: 1 for red, 2 for orange, 3 for yellow...(the third line colors in menu)  #When Colornum = 8, it equals MoreColor() function
    Num = ColorNum + 16     # Red = 17,Orange = 18, Yellow = 19 ......)
    try:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()
    except:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()


# Use MoreColor() to open color menu, then you can use functions in ColorMenu.py to adjust color.
def MoreColor(self):
    try:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView[24]').click()
    except:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView[24]').click()


def AdjustThickness(self, Num):  # 0~32 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarWidth))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarWidth).send_keys(str(Num))


def AdjustTransParency(self, Num):  # 0~229 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarAlpha))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarAlpha).send_keys(str(Num))
