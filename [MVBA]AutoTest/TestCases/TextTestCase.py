import datetime
import time
from openpyxl import Workbook
from openpyxl import load_workbook
from Params.ElementParams import ElementParam
from Params.SystemParams import ImgPath
from Library.LibLogHelper import LogPackage
from Library.LibData import LibData
from openpyxl.drawing.image import Image
from UnitFunction import Canvas, Text, Screenshot, Compare, log
import sys
import os
sys.path.append(os.getcwd())
Text_log = log.Logger(
    './Output/Logs/Tier'+datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S') + '.log', level='info')
textImg_path = ImgPath._TextImgPath
Case1_Editor_img = Image(LibData.StringMerge(
    "/", textImg_path, "Case1_Editor.png"))
Case1_Canvas_img = Image(textImg_path+"/Case1_Canvas.png")
Case2_Editor_img = Image(textImg_path+"/Case2_Editor.png")
Case2_Canvas_img = Image(textImg_path+"/Case2_Canvas.png")
Case3_Editor_img = Image(textImg_path+"/Case3_Editor.png")
Case3_Canvas_img = Image(textImg_path+"/Case3_Canvas.png")
step_img = Image("./Cache images/cache_image.png")

LogPack = LogPackage("TextResult", srcFileName="Text")


def testCase1(self):
    sheetName = "TextCase1"
    LogPack.NewLogSheet(sheetName)
    try:
        #Text_log.logger.info("Start TextCase1:在畫布建立文字編輯器，然後更改Font跟Size並套用Bold，接著輸入文字。")
        time.sleep(5)
        textIcon_id = ElementParam._Id_btnTypingText
        textIcon = self.driver.find_element_by_id(textIcon_id)
        textIcon.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊Tool bar上的Text icon", "執行結果", step_img)
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        Canvas.Tap(self, 900, 250)
        Canvas.Tap(self, 900, 250)
        Screenshot.screenshotTextEditor(self, step_img)
        LogPack.AddUnitLog(sheetName, "點擊畫布建立文字編輯框", "執行結果", step_img)
        Text.ChangeFont(self, 3)
        FontName_id = ElementParam._Id_spinnerFontName
        FontName = self.driver.find_element_by_id(FontName_id)
        FontName.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Font", "執行結果", step_img)
        Text.ChangeSize(self, 9)
        FontSize_id = ElementParam._Id_spinnerFontSize
        FontSize = self.driver.find_element_by_id(FontSize_id)
        FontSize.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Size", "執行結果", step_img)
        Bold_id = ElementParam._Id_checkBold
        Bold = self.driver.find_element_by_id(Bold_id)
        Bold.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "套用Bold", "執行結果", step_img)
        Text.Bold(self)
        # Text.Italic(self)
        # Text.UnderLine(self)
        Text.TypeText(self, "testcaseone")
        editText_id = ElementParam._Id_editText
        editText = self.driver.find_element_by_id(editText_id)
        editText.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "輸入文字'testcaseone'", "執行結果", step_img)
        Screenshot.screenshotTextEditor(
            self, Case1_Editor_img)
        LogPack.AddUnitLog(sheetName, "擷取文字編輯框上的工具列", "執行結果", Case1_Editor_img)
        buttonMenuClose_id = ElementParam._Id_buttonMenuClose
        buttonMenuClose = self.driver.find_element_by_id(buttonMenuClose_id)
        buttonMenuClose.screenshot(step_img)
        Text.CloseEditor(self)
        LogPack.AddUnitLog(sheetName, "關閉文字編輯框", "執行結果", step_img)
        Screenshot.screenshotCanvas(
            self, Case1_Canvas_img)
        LogPack.AddUnitLog(sheetName, "擷取畫布內容", "執行結果", Case1_Canvas_img)
        if not Compare.isImgEqual(Case1_Editor_img, "./TestCases/Samples/Text/Case1_Editor.png"):
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Pass!")
        if not Compare.isImgEqual(Case1_Canvas_img, "./TestCases/Samples/Text/Case1_Canvas.png"):
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Pass!")
        #Text_log.logger.info("TextCase1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        #LogPack.AddLogRow(sheetName, "執行貼圖", "系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")


def testCase2(self):
    sheetName = "TextCase2"
    LogPack.NewLogSheet(sheetName)
    try:
        #Text_log.logger.info("Start TextCase2:在畫布建立文字編輯器，然後更改Font跟Size並套用Italic，接著更改文字顏色(“Advanced”)以及底色(“STANDARD”)，再輸入文字。")
        time.sleep(5)
        textIcon_id = ElementParam._Id_btnTypingText
        textIcon = self.driver.find_element_by_id(textIcon_id)
        textIcon.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊Tool bar上的Text icon", "執行結果", step_img)
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        Canvas.Tap(self, 900, 500)
        Canvas.Tap(self, 900, 500)
        Screenshot.screenshotTextEditor(self, step_img)
        LogPack.AddUnitLog(sheetName, "點擊畫布建立文字編輯框", "執行結果", step_img)
        Text.ChangeFont(self, 6)
        FontName_id = ElementParam._Id_spinnerFontName
        FontName = self.driver.find_element_by_id(FontName_id)
        FontName.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Font", "執行結果", step_img)
        Text.ChangeSize(self, 13)
        FontSize_id = ElementParam._Id_spinnerFontSize
        FontSize = self.driver.find_element_by_id(FontSize_id)
        FontSize.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Size", "執行結果", step_img)
        Italic_id = ElementParam._Id_checkItalic
        Italic = self.driver.find_element_by_id(Italic_id)
        Italic.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "套用Italic", "執行結果", step_img)
        Text.Italic(self)
        FontColor_id = ElementParam._Id_checkbuttonColor
        FontColor = self.driver.find_element_by_id(FontColor_id)
        FontColor.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊文字顏色icon，並點擊”ADVANCED", "執行結果", step_img)
        Text.ChangeColor(self, "Advanced", R=130, G=107, B=70)
        FontColorBg_id = ElementParam._Id_checkbuttonColorBg
        FontColorBg = self.driver.find_element_by_id(FontColorBg_id)
        FontColorBg.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊底色icon，並點擊“STANDARD", "執行結果", step_img)
        Text.ChangeColorBg(self, ColorNum=9)
        Text.TypeText(self, "testcasetwo")
        editText_id = ElementParam._Id_editText
        editText = self.driver.find_element_by_id(editText_id)
        editText.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "輸入文字'testcasetwo'", "執行結果", step_img)
        Screenshot.screenshotTextEditor(
            self, Case2_Editor_img)
        LogPack.AddUnitLog(sheetName, "擷取文字編輯框上的工具列", "執行結果", Case2_Editor_img)
        buttonMenuClose_id = ElementParam._Id_buttonMenuClose
        buttonMenuClose = self.driver.find_element_by_id(buttonMenuClose_id)
        buttonMenuClose.screenshot(step_img)
        Text.CloseEditor(self)
        LogPack.AddUnitLog(sheetName, "關閉文字編輯框", "執行結果", step_img)
        Screenshot.screenshotCanvas(
            self, Case2_Canvas_img)
        LogPack.AddUnitLog(sheetName, "擷取畫布內容", "執行結果", Case2_Canvas_img)
        if not Compare.isImgEqual(Case2_Editor_img, "./TestCases/Samples/Text/Case2_Editor.png"):
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Pass!")
        if not Compare.isImgEqual(Case2_Canvas_img, "./TestCases/Samples/Text/Case2_Cavas.png"):
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Pass!")
        #Text_log.logger.info("TextCase2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        #LogPack.AddLogRow(sheetName, "執行貼圖", "系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")


def testCase3(self):
    sheetName = "TextCase3"
    LogPack.NewLogSheet(sheetName)
    try:
        #Text_log.logger.info("Start TextCase3:在畫布建立文字編輯器，然後更改Font跟Size並套用UnderLine，接著更改文字顏色(“STANDARD”)以及底色(“Advanced”)，再輸入文字。")
        time.sleep(5)
        textIcon_id = ElementParam._Id_btnTypingText
        textIcon = self.driver.find_element_by_id(textIcon_id)
        textIcon.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊Tool bar上的Text icon", "執行結果", step_img)
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        Canvas.Tap(self, 900, 750)
        Canvas.Tap(self, 900, 750)
        Screenshot.screenshotTextEditor(self, step_img)
        LogPack.AddUnitLog(sheetName, "點擊畫布建立文字編輯框", "執行結果", step_img)
        Text.ChangeFont(self, 9)
        FontName_id = ElementParam._Id_spinnerFontName
        FontName = self.driver.find_element_by_id(FontName_id)
        FontName.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Font", "執行結果", step_img)
        Text.ChangeSize(self, 15)
        FontSize_id = ElementParam._Id_spinnerFontSize
        FontSize = self.driver.find_element_by_id(FontSize_id)
        FontSize.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "更改Size", "執行結果", step_img)
        UnderLine_id = ElementParam._Id_checkUnderline
        UnderLine = self.driver.find_element_by_id(UnderLine_id)
        UnderLine.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "套用UnderLine", "執行結果", step_img)
        Text.UnderLine(self)
        FontColor_id = ElementParam._Id_checkbuttonColor
        FontColor = self.driver.find_element_by_id(FontColor_id)
        FontColor.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊文字顏色icon，並點擊”STANDARD", "執行結果", step_img)
        Text.ChangeColor(self, ColorNum=6)
        FontColorBg_id = ElementParam._Id_checkbuttonColorBg
        FontColorBg = self.driver.find_element_by_id(FontColorBg_id)
        FontColorBg.screenshot(step_img)
        LogPack.AddUnitLog(
            sheetName, "點擊底色icon，並點擊“ADVANCED", "執行結果", step_img)
        Text.ChangeColorBg(self, "Advanced", R=110, G=200, B=90)
        Text.TypeText(self, "testcasethree")
        editText_id = ElementParam._Id_editText
        editText = self.driver.find_element_by_id(editText_id)
        editText.screenshot(step_img)
        LogPack.AddUnitLog(sheetName, "輸入文字'testcasethree'", "執行結果", step_img)
        Screenshot.screenshotTextEditor(
            self, Case3_Editor_img)
        LogPack.AddUnitLog(sheetName, "擷取文字編輯框上的工具列", "執行結果", Case3_Editor_img)
        buttonMenuClose_id = ElementParam._Id_buttonMenuClose
        buttonMenuClose = self.driver.find_element_by_id(buttonMenuClose_id)
        buttonMenuClose.screenshot(step_img)
        Text.CloseEditor(self)
        LogPack.AddUnitLog(sheetName, "關閉文字編輯框", "執行結果", step_img)
        Screenshot.screenshotCanvas(
            self, Case3_Canvas_img)
        LogPack.AddUnitLog(sheetName, "擷取畫布內容", "執行結果", Case3_Canvas_img)
        if not Compare.isImgEqual(Case3_Editor_img, "./TestCases/Samples/Text/Case3_Editor.png"):
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對編輯框內容", "Pass!")
        if not Compare.isImgEqual(Case3_Canvas_img, "./TestCases/Samples/Text/Case3_Cavas.png"):
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Fail!")
        else:
            LogPack.AddUnitLog(sheetName, "比對畫布內容", "Pass!")
        #Text_log.logger.info("TextCase3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        #LogPack.AddLogRow(sheetName, "執行貼圖", "系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")


LogPack.CreateLog()
