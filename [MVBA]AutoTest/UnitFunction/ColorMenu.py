from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam

'''
ColorMenu.py is designed for the particular color menu when you adjust color.
The menu will show up when you click "+" icon in pen/shape/background menu, adjust color of text, and click color platte icon in adorner.
'''


# color_num: 1~17, 1 is blue, 2 is cyan...
def ChangeColorByStandard(self, color_num):
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonStandard))
    )
    self.driver.find_element_by_id(ElementParam._Id_buttonStandard).click()
    self.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(color_num)+']').click()


def edittextclear(self, text):  # this function is designed for ChangeColorByAdvanced function
    self.driver.press_keycode('123')
    for i in range(0, len(text)):
        self.driver.press_keycode('67')


def ChangeColorByAdvanced(self, R, G, B, A):
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
