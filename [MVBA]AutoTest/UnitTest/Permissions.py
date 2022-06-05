import UnitFunc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Params.ElementParams import ElementParam


class Permissions(UnitFunc.FuncBase):
    def CheckPermission(self,menuElement,element,isActivty,isToast):
        if(not menuElement is None):
            self.Driver.ElementClick(menuElement)
        if(not menuElement is None):
            self.Driver.ElementClick(element)
        return self.CheckToastlog(self) if isToast else self.CheckAlertDialog(self)

    def CheckToastlog(self):
        toast_loc = '//*[contains(@text,"{}")]'.format(
            "Please sign in to use the feature.")
        try:
            WebDriverWait(self.driver, 5, 0.2).until(
                EC.presence_of_element_located((By.XPATH, toast_loc))
            )
            Toasttext = self.driver.find_element_by_xpath(toast_loc).text
            return Toasttext
        except:
            return "未出現Toast提示"

    def CheckAlertDialog(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_title))
            )
            text = self.driver.find_element_by_id(
                ElementParam._Id_title).get_attribute("text")
            if text == "Whiteboard activation required" or text == "啟用提示":
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonOk))
                )
                self.driver.find_element_by_id(
                    ElementParam._Id_buttonOk).click()
            elif text == "Subscription upgrade required" or text == "訂閱資料":
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonCancel))
                )
                self.driver.find_element_by_id(
                    ElementParam._Id_buttonCancel).click()
            else:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonOk))
                )
                self.driver.find_element_by_id(
                    ElementParam._Id_buttonOk).click()
            return text
        except:
            return "未出現提示"