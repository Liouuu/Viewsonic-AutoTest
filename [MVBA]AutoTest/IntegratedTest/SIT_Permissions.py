from ElementParams import ElementParam
import Permissions


def NoActivateCase(self):
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnMeeting, ElementParam._Id_connect_cast, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture_rectangle_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_record, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_live, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSave, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSaveAs, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileExport, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonFileEmail, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonQRCodeFile, False, False)

    sheet['B12'] = "Check StickyNote for No Activate"
    if Permissions.TryStickyNote(self, "orange")[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C12'] = "StickyNote for No Activate is pass!!"
    else:
        sheet['C12'] = "StickyNote for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)

    sheet['B13'] = "Check Mathtool for No Activate"
    if Permissions.TryMathtool(self, "compass")[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C13'] = "Mathtool for No Activate is pass!!"
    else:
        sheet['C13'] = "Mathtool for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)

    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioDocumentCamera, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioYoutubeSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioImageSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioThrow, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioPopQuiz, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioAIPen, False, False)

    sheet['B20'] = "Check FollowMeBackground for No Activate"
    if Permissions.TryFollowMeBackground(self)[1] == "Whiteboard activation required" or "啟用提示":
        sheet['C20'] = "FollowMeBackground for No Activate is pass!!"
    else:
        sheet['C20'] = "FollowMeBackground for No Activate is fail!!"
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)


def TierPreloadCase(self):
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnMeeting, ElementParam._Id_connect_cast, False, True)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture, False, True)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture_rectangle_capture, False, True)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_record, False, True)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_live, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSave, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSaveAs, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileExport, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonFileEmail, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonQRCodeFile, False, True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioDocumentCamera, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioYoutubeSearch, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioImageSearch, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioThrow, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioPopQuiz, False, True)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioAIPen, False, True)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,True)


def TierStandardCase(self):
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnMeeting, ElementParam._Id_connect_cast, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture_rectangle_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_record, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_live, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSave, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSaveAs, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileExport, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonFileEmail, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonQRCodeFile, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioDocumentCamera, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioYoutubeSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioImageSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioThrow, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioPopQuiz, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioAIPen, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)


def TierPremiumCase(self):
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnMeeting, ElementParam._Id_connect_cast, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture_rectangle_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_record, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_live, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSave, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSaveAs, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileExport, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonFileEmail, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonQRCodeFile, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioDocumentCamera, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioYoutubeSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioImageSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioThrow, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioPopQuiz, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioAIPen, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)


def TierEntityCase(self):
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnMeeting, ElementParam._Id_connect_cast, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_capture_rectangle_capture, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_record, False, False)
    Permissions.Permissions.CheckPermission(
        ElementParam._Id_btnCapture, ElementParam._Id_capture_menu_button_live, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSave, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileSaveAs, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioFileExport, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonFileEmail, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_buttonQRCodeFile, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_buttonQRCodeFile,False,False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioDocumentCamera, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioYoutubeSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioImageSearch, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioThrow, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioPopQuiz, False, False)
    Permissions.Permissions.CheckPermission(
        None, ElementParam._Id_radioAIPen, False, False)
    # Tier.Permissions.CheckPermission(None,ElementParam._Id_radioPopQuiz,False,False)
