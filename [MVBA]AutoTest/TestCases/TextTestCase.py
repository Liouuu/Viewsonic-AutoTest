import datetime
import time
from openpyxl import Workbook
from openpyxl import load_workbook
from LibData import export_table
from Params.ElementParams import ElementParam
from UnitFunction import Canvas, Text, Screenshot, Compare, log
import sys
import os
sys.path.append(os.getcwd())

getTime = datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S')
Text_w = Workbook()
w_s = Text_w.active
w_s.title = "TextCase1"
w_s1 = Text_w.create_sheet(index=1, title="TextCase2")
w_s1 = Text_w.create_sheet(index=2, title="TextCase3")
for w in range(3):
    sheet = Text_w.worksheets[w]
    sheet['A1'] = "時間"
    sheet['B1'] = "步驟"
    sheet['C1'] = "結果"
    sheet['D1'] = '圖片'
    sheet.column_dimensions['A'].width = 18.0  # 調整列寬
    sheet.column_dimensions['B'].width = 50.0
    sheet.column_dimensions['C'].width = 50.0
    #sheet.column_dimensions['D'].width = 48
Text_w.save('./Output/Excels/Text' + getTime + '.xlsx')
Text_log = log.Logger(
    './Output/Logs/Text'+datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S') + '.log', level='info')
save_path = './Cache images/cache_image.png'


def testCase1(self):
    try:
        allStep = export_table.TestCase_steps(
            './TestCases/case document/Text', 0)
        #Text_log.logger.info("Start TextCase1:在畫布建立文字編輯器，然後更改Font跟Size並套用Bold，接著輸入文字。")
        time.sleep(5)
        textIcon_id = ElementParam._Id_btnTypingText
        textIcon = self.driver.find_element_by_id(textIcon_id)
        textIcon.screenshot(save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[0], img_path=save_path)
        Text_log.logger.info("點擊Tool bar上的Text icon")
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        Text_log.logger.info("點擊畫布建立文字編輯框")
        Canvas.Tap(self, 900, 250)
        Canvas.Tap(self, 900, 250)
        Screenshot.screenshotTextEditor(self, save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[1], img_path=save_path)

        Text_log.logger.info("更改Font")
        Text.ChangeFont(self, 3)
        FontName_id = ElementParam._Id_spinnerFontName
        FontName = self.driver.find_element_by_id(FontName_id)
        FontName.screenshot(save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[2], img_path=save_path)
        Text_log.logger.info("更改Size")
        Text.ChangeSize(self, 9)
        FontSize_id = ElementParam._Id_spinnerFontSize
        FontSize = self.driver.find_element_by_id(FontSize_id)
        FontSize.screenshot(save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[3], img_path=save_path)
        Text_log.logger.info("套用Bold")
        Bold_id = ElementParam._Id_checkBold
        Bold = self.driver.find_element_by_id(Bold_id)
        Bold.screenshot(save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[4], img_path=save_path)
        Text.Bold(self)
        # Text.Italic(self)
        # Text.UnderLine(self)

        Text_log.logger.info("輸入文字'testcaseone'")
        Text.TypeText(self, "testcaseone")
        editText_id = ElementParam._Id_editText
        editText = self.driver.find_element_by_id(editText_id)
        editText.screenshot(save_path)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[5], img_path=save_path)

        Text_log.logger.info("擷取文字編輯框上的工具列")
        Screenshot.screenshotTextEditor(
            self, "./TestCases/Screenshots/Text/Case1_Editor.png")
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[6], img_path="./TestCases/Screenshots/Text/Case1_Editor.png")

        Text_log.logger.info("關閉文字編輯框")
        buttonMenuClose_id = ElementParam._Id_buttonMenuClose
        buttonMenuClose = self.driver.find_element_by_id(buttonMenuClose_id)
        buttonMenuClose.screenshot(save_path)
        Text.CloseEditor(self)
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[7], img_path=save_path)

        Text_log.logger.info("擷取畫布內容")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Text/Case1_Cavas.png")
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[8], img_path="./TestCases/Screenshots/Text/Case1_Cavas.png")
        Text_log.logger.info("比對編輯框內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case1_Editor.png", "./TestCases/Samples/Text/Case1_Editor.png"):
            export_table.export_table(
                './Excels/Text' + getTime, step=allStep[9], result='Failed')
            Text_log.logger.info("Case 1: Text Editor Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, step=allStep[9], result='Pass')
            Text_log.logger.info("Case 1: Text Editor Pass!")
        Text_log.logger.info("比對畫布內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case1_Cavas.png", "./TestCases/Samples/Text/Case1_Cavas.png"):
            export_table.export_table(
                './Excels/Text' + getTime, step=allStep[10], result='Failed')
            Text_log.logger.info("Case 1: Text Canvas Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, step=allStep[10], result='Pass')
            Text_log.logger.info("Case 1: Text Canvas Pass!")
        Text_log.logger.info("TextCase1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        export_table.export_table(
            './Excels/Text' + getTime, step=allStep[0], result="系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")


def testCase2(self):
    try:
        allStep = export_table.TestCase_steps(
            './TestCases/case document/Text', 1)
        Text_log.logger.info(
            "Start TextCase2:在畫布建立文字編輯器，然後更改Font跟Size並套用Italic，接著更改文字顏色(“Advanced”)以及底色(“STANDARD”)，再輸入文字。")
        time.sleep(5)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[0])
        Text_log.logger.info("點擊Tool bar上的Text icon")
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[1])
        Text_log.logger.info("點擊畫布建立文字編輯框")
        Canvas.Tap(self, 900, 500)
        Canvas.Tap(self, 900, 500)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[2])
        Text_log.logger.info("更改Font")
        Text.ChangeFont(self, 6)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[3])
        Text_log.logger.info("更改Size")
        Text.ChangeSize(self, 13)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[4])
        Text_log.logger.info("套用Italic")
        Text.Italic(self)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[5])
        Text_log.logger.info("點擊文字顏色icon，並點擊”ADVANCED")
        Text.ChangeColor(self, "Advanced", R=130, G=107, B=70)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[6])
        Text_log.logger.info("點擊底色icon，並點擊“STANDARD")
        Text.ChangeColorBg(self, ColorNum=9)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[7])
        Text_log.logger.info("輸入文字'testcasetwo'")
        Text.TypeText(self, "testcasetwo")
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[8])
        Text_log.logger.info("擷取文字編輯框上的工具列")
        Screenshot.screenshotTextEditor(
            self, "./TestCases/Screenshots/Text/Case2_Editor.png")
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[9])
        Text_log.logger.info("關閉文字編輯框")
        Text.CloseEditor(self)
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[10])
        Text_log.logger.info("擷取畫布內容")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Text/Case2_Cavas.png")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Text/Case2_Cavas.png")
        Text_log.logger.info("比對編輯框內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case2_Editor.png", "./TestCases/Samples/Text/Case2_Editor.png"):
            export_table.export_table(
                './Excels/Text' + getTime, 1, step=allStep[11], result="Failed")
            Text_log.logger.info("Case 2: Text Editor Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, 1, step=allStep[11], result="Pass")
            Text_log.logger.info("Case 2: Text Editor Pass!")
        Text_log.logger.info("比對畫布內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case2_Cavas.png", "./TestCases/Samples/Text/Case2_Cavas.png"):
            export_table.export_table(
                './Excels/Text' + getTime, 1, step=allStep[12], result="Failed")
            Text_log.logger.info("Case 2: Text Canvas Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, 1, step=allStep[12], result="Pass")
            Text_log.logger.info("Case 2: Text Canvas Pass!")
        Text_log.logger.info("TextCase2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        export_table.export_table(
            './Excels/Text' + getTime, 1, step=allStep[0], result="系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")


def testCase3(self):
    try:
        allStep = export_table.TestCase_steps(
            './TestCases/case document/Text', 2)
        Text_log.logger.info(
            "Start TextCase3:在畫布建立文字編輯器，然後更改Font跟Size並套用UnderLine，接著更改文字顏色(“STANDARD”)以及底色(“Advanced”)，再輸入文字。")
        time.sleep(5)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[0])
        Text_log.logger.info("點擊Tool bar上的Text icon")
        Text.SelectTextBtn(self)
        Text.SelectTextBtn(self)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[1])
        Text_log.logger.info("點擊畫布建立文字編輯框")
        Canvas.Tap(self, 900, 750)
        Canvas.Tap(self, 900, 750)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[2])
        Text_log.logger.info("更改Font跟Size")
        Text.ChangeFont(self, 9)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[3])
        Text.ChangeSize(self, 15)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[4])
        Text_log.logger.info("套用UnderLine")
        Text.UnderLine(self)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[5])
        Text_log.logger.info("點擊文字顏色icon，並點擊”STANDARD")
        Text.ChangeColor(self, ColorNum=6)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[6])
        Text_log.logger.info("點擊底色icon，並點擊”ADVANCED")
        Text.ChangeColorBg(self, "Advanced", R=110, G=200, B=90)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[7])
        Text_log.logger.info("輸入文字'testcasethree'")
        Text.TypeText(self, "testcasethree")
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[8])
        Text_log.logger.info("擷取文字編輯框上的工具列")
        Screenshot.screenshotTextEditor(
            self, "./TestCases/Screenshots/Text/Case3_Editor.png")
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[9])
        Text_log.logger.info("關閉文字編輯框")
        Text.CloseEditor(self)
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[10])
        Text_log.logger.info("擷取畫布內容")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Text/Case3_Cavas.png")
        Text_log.logger.info("比對編輯框內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case3_Editor.png", "./TestCases/Samples/Text/Case3_Editor.png"):
            export_table.export_table(
                './Excels/Text' + getTime, 2, step=allStep[11], result="Failed")
            Text_log.logger.info("Case 3: Text Editor Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, 2, step=allStep[11], result="Pass")
            Text_log.logger.info("Case 3: Text Editor Pass!")
        Text_log.logger.info("比對畫布內容")
        if not Compare.isImgEqual("./TestCases/Screenshots/Text/Case3_Cavas.png", "./TestCases/Samples/Text/Case3_Cavas.png"):
            export_table.export_table(
                './Excels/Text' + getTime, 2, step=allStep[12], result="Failed")
            Text_log.logger.info("Case 3: Text Canvas Fail!")
        else:
            export_table.export_table(
                './Excels/Text' + getTime, 2, step=allStep[12], result="Pass")
            Text_log.logger.info("Case 3: Text Canvas Pass!")
        Text_log.logger.info("TextCase3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        export_table.export_table(
            './Excels/Text' + getTime, 2, step=allStep[0], result="系統運行錯誤，請看log日誌")
        Text_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Text_log.logger.info("Finish")
