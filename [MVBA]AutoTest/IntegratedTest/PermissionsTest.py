from pickle import FALSE
from openpyxl import load_workbook
from openpyxl import Workbook
from unittest import result
import time
import datetime
from ElementParams import ElementParam
from UnitFunction import log, LoginAndActive, Tier


def NoActivateCase(self):
    Tier.Permissions.CheckPermission(ElementParam._Id_btnMeeting,ElementParam._Id_connect_cast,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture_rectangle_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_record,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_live,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSave,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSaveAs,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileExport,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonFileEmail,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)

    sheet['B12'] = "Check StickyNote for No Activate"
    if Tier.TryStickyNote(self, "orange")[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C12'] = "StickyNote for No Activate is pass!!"
    else:
        sheet['C12'] = "StickyNote for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)

    sheet['B13'] = "Check Mathtool for No Activate"
    if Tier.TryMathtool(self, "compass")[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C13'] = "Mathtool for No Activate is pass!!"
    else:
        sheet['C13'] = "Mathtool for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)

    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioDocumentCamera,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioYoutubeSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioImageSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioThrow,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioAIPen,False,False)

    sheet['B20'] = "Check FollowMeBackground for No Activate"
    if Tier.TryFollowMeBackground(self)[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C20'] = "FollowMeBackground for No Activate is pass!!"
    else:
        sheet['C20'] = "FollowMeBackground for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)



def TierPreloadCase(self):
    Tier.Permissions.CheckPermission(ElementParam._Id_btnMeeting,ElementParam._Id_connect_cast,False,True)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture,False,True)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture_rectangle_capture,False,True)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_record,False,True)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_live,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSave,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSaveAs,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileExport,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonFileEmail,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioDocumentCamera,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioYoutubeSearch,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioImageSearch,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioThrow,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,True)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioAIPen,False,True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,True)

def TierStandardCase(self):
    Tier.Permissions.CheckPermission(ElementParam._Id_btnMeeting,ElementParam._Id_connect_cast,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture_rectangle_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_record,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_live,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSave,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSaveAs,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileExport,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonFileEmail,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioDocumentCamera,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioYoutubeSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioImageSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioThrow,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioAIPen,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)

def TierPremiumCase(self):
    Tier.Permissions.CheckPermission(ElementParam._Id_btnMeeting,ElementParam._Id_connect_cast,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture_rectangle_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_record,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_live,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSave,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSaveAs,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileExport,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonFileEmail,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioDocumentCamera,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioYoutubeSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioImageSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioThrow,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioAIPen,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)

def TierEntityCase(self):
    Tier.Permissions.CheckPermission(ElementParam._Id_btnMeeting,ElementParam._Id_connect_cast,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_capture_rectangle_capture,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_record,False,False)
    Tier.Permissions.CheckPermission(ElementParam._Id_btnCapture,ElementParam._Id_capture_menu_button_live,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSave,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileSaveAs,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioFileExport,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonFileEmail,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioDocumentCamera,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioYoutubeSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioImageSearch,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioThrow,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
    Tier.Permissions.CheckPermission(None,ElementParam._Id_radioAIPen,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
