from UnitFunction import MagicBox, StickyNote, FileManagement, Background, Canvas
import time
from UnitFunction.Pen import PenMenu
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from unittest import result
from cgitb import text
from Params.ElementParams import ElementParam


def CheckPermission_message(self):
    try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.packageinstaller:id/permission_allow_button"))
        )
        self.driver.find_element_by_id(
            "com.android.packageinstaller:id/permission_allow_button").click()
    except:
        pass
    try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        self.driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_button").click()
    except:
        pass


def CheckCapturePermission_message(self):
    try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "android:id/button1"))
        )
        self.driver.find_element_by_id("android:id/button1").click()
    except:
        pass


def TrySendEmail(self):
    try:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText'))
        )
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.EditText').send_keys("mvbaautotest1@gmail.com")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "com.google.android.gm:id/send"))
        )
        self.driver.find_element_by_id("com.google.android.gm:id/send").click()
    except:
        pass


def TryCloseFileManagement(self):
    try:
        FileManagement.CloseFileManagement(self)
    except:
        pass


def CheckCaptureMenuClose(self):
    try:
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.ID, ElementParam._Id_capture_menu_buttonMenuClose))
        )
        self.driver.find_element_by_id(
            ElementParam._Id_capture_menu_buttonMenuClose).click()
    except:
        pass


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


def TryWirelessPresentation(self):
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnMeeting))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnMeeting).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_connect_cast))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_connect_cast).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryCaptureAll(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnCapture))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnCapture).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_capture_menu_button_capture))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_capture_menu_button_capture).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    CheckCapturePermission_message(self)
    CheckCaptureMenuClose(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryCaptureRectangle(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnCapture))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnCapture).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_capture_menu_button_capture_rectangle_capture))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_capture_menu_button_capture_rectangle_capture).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    Canvas.Select_Object(self, 626, 584, 879, 707)
    CheckCapturePermission_message(self)
    CheckCaptureMenuClose(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryRecord(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnCapture))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnCapture).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_capture_menu_button_record))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_capture_menu_button_record).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    try:
        self.driver.find_element_by_id(
            ElementParam._Id_capture_menu_buttonMenuClose).click()
    except:
        Canvas.Tap(self, 1889, 607)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryStream(self):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_btnCapture))
    )
    self.driver.find_element_by_id(ElementParam._Id_btnCapture).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_capture_menu_button_live))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_capture_menu_button_live).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    try:
        self.driver.find_element_by_id(
            ElementParam._Id_capture_menu_buttonMenuClose).click()
    except:
        Canvas.Tap(self, 1889, 607)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TrySave(self):
    FileManagement.OpenFileManagement(self)
    CheckPermission_message(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioFileSave))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioFileSave).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    FileManagement.CloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TrySaveAs(self):
    FileManagement.OpenFileManagement(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioFileSaveAs))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioFileSaveAs).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    FileManagement.CloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryExportBtn(self):
    FileManagement.OpenFileManagement(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioFileExport))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioFileExport).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    FileManagement.CloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryExportPDF(self):
    FileManagement.OpenFileManagement(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioFileExport))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_radioFileExport).click()
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_spnFileExportType))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_spnFileExportType).click()
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]"))
    )
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()  # select PDF
    self.driver.find_element_by_id(
        ElementParam._Id_editFileExportName).send_keys(str(int(time.time())))
    self.driver.find_element_by_id(
        ElementParam._Id_btnFileExportOK).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    FileManagement.CloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryMail(self):
    FileManagement.OpenFileManagement(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonFileEmail))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonFileEmail).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    TrySendEmail(self)
    TryCloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryQRcodeShare(self):
    FileManagement.OpenFileManagement(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_buttonQRCodeFile))
    )
    self.driver.find_element_by_id(
        ElementParam._Id_buttonQRCodeFile).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    FileManagement.CloseFileManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryAIpen(self):
    PenMenu.OpenPenMenu(self)
    WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, ElementParam._Id_radioAIPen))
    )
    self.driver.find_element_by_id(ElementParam._Id_radioAIPen).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    PenMenu.ClosePenMenu(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryFollowMeBackground(self):
    Background.OpenBackgroundManagement(self)
    Background.SelectBackgroundMenu(self, "follow me")
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    Background.CloseBackgroundManagement(self)
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryStickyNote(self, type="yellow"):
    MagicBox.OpenMagicBox(self)
    StickyNote.ClickStickynote(self)
    dict = {"yellow": 2, "orange": 3, "blue": 4, "green": 5}
    StickyNote.StickynoteColor(self, dict[type])
    time.sleep(2)
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryMathtool(self, type="ruler"):
    MagicBox.OpenMagicBox(self)
    dict = {"ruler": "3", "compass": "4", "protractor": "5"}
    try:
        Tool = self.driver.find_element_by_xpath(
            '(//android.widget.ImageView[@content-desc="Whiteboard"])[2]')
    except:
        dict = {"ruler": "2", "compass": "3", "protractor": "4"}
    self.driver.find_element_by_id(
        ElementParam._Id_radioMathTools).click()
    Tool = self.driver.find_element_by_xpath(
        '(//android.widget.ImageView[@content-desc="Whiteboard"])[' + dict[type] + ']')
    for i in range(2):
        Tool.click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryCamera(self):
    MagicBox.OpenMagicBox(self)
    self.driver.find_element_by_id(
        ElementParam._Id_radioDocumentCamera).click()
    Toastresult = CheckToastlog(self)
    CheckPermission_message(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryYouTubeSearch(self):
    MagicBox.OpenMagicBox(self)
    self.driver.find_element_by_id(
        ElementParam._Id_radioYoutubeSearch).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryImageSearch(self):
    MagicBox.OpenMagicBox(self)
    self.driver.find_element_by_id(
        ElementParam._Id_radioImageSearch).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryThrow(self):
    MagicBox.OpenMagicBox(self)
    self.driver.find_element_by_id(ElementParam._Id_radioThrow).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryPopQuiz(self):
    MagicBox.OpenMagicBox(self)
    self.driver.find_element_by_id(
        ElementParam._Id_radioPopQuiz).click()
    Toastresult = CheckToastlog(self)
    Alertresult = CheckAlertDialog(self)
    self.driver.find_element_by_id(
        ElementParam._Id_buttonMenuClose).click()
    result = []
    result.extend((Toastresult, Alertresult))
    return result


def TryClips(self):
    MagicBox.OpenMagicBox(self)
    try:
        self.driver.find_element_by_id(
            ElementParam._Id_radioClipsSearch).click()
        time.sleep(5)
        self.driver.find_element_by_id(
            ElementParam._Id_buttonMenuClose).click()
        return True
    except:
        return False
