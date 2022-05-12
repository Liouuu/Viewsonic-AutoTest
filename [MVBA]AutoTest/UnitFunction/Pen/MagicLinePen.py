from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ChangePattern(self, index):
    self.driver.find_element_by_xpath(
        '(//android.widget.ImageView[@content-desc="Whiteboard"])['+str(index)+']').click()


def AdjustThickness(self, val):  # 0~32 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_seekBarWidth))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarWidth).send_keys(str(val))


def AdjustTransParency(self, val):  # 0~229 ##
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, ElementParam._Id_seekBarAlpha))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_seekBarAlpha).send_keys(str(val))
