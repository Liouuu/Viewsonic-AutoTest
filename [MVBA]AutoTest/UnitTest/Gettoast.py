from lzma import FORMAT_ALONE
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UnitBase import ToolBar
from Params.ElementParams import ElementParam


def get(self):
    # self.driver.find_element_by_id(ElementParam._Id_buttonMenuClose).click()#Close Sign in menu
    ToolBar.MagicBox.OpenMagicBox(self)
    ToolBar.MagicBox.SelectImageSearch(self)
    # self.driver.find_element_by_xpath('(//android.widget.ImageButton[@content-desc="Whiteboard"])[5]').click()#Close Sign in menu

    #toast_loc = ("//*[contains(@text,'Sign')]")
    toast_loc = '//*[contains(@text,"{}")]'.format(
        "Sign in required!\nPlease sign in to use this feature.")
    try:
        WebDriverWait(self.driver, 5, 0.2).until(
            EC.presence_of_element_located((By.XPATH, toast_loc))
        )
        s = self.driver.find_element_by_xpath(toast_loc).text
        print(s)

    except:
        print("Toast not found")
