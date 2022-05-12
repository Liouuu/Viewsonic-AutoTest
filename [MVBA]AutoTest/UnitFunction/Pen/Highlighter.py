from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Params.ElementParams import ElementParam


def ChangeColor(self, index):  # index: 1~5
    try:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.ImageView['+str(index)+']').click()
    except:
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.ImageView['+str(index)+']').click()


def AdjustThickness(self, val):  # val= 0~32
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarWidthHighlighter))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarWidthHighlighter).send_keys(str(val))
