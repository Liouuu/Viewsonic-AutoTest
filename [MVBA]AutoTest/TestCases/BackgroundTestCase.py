import datetime
import time
from Library import Compare
from UnitFunction import Background, FloatBar, Screenshot, Canvas, ColorMenu, log
import sys
import os
sys.path.append(os.getcwd())

background_log = log.Logger(
    './Output/Logs/Background '+datetime.datetime.now().strftime(" %Y-%m-%d_%H_%M_%S") + '.log', level='info')


def Case1_1(self):
    try:
        background_log.logger.info(
            "Start Color Menu Case1-1: 調整Background主menu的顏色")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Select Background Menu: color")
        Background.SelectBackgroundMenu(self, "color")
        background_log.logger.info("Change color: index 17")
        Background.ChangeByColor(self, 17)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background1-1.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background1-1.png", "./TestCases/Samples/Background/Canvas_Background1-1.png"):
            background_log.logger.info("Case1-1: Canvas_Background Fail!")
            return
        background_log.logger.info("Case1-1: Canvas_Background Pass!")
        background_log.logger.info("Case1-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case1_2(self):
    try:
        background_log.logger.info(
            "Start More Color Standard Case1-2: 調整Background上的”STANDARD”顏色")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Select Background Menu: color")
        Background.SelectBackgroundMenu(self, "color")
        background_log.logger.info("Click '+' icon")
        Background.OpenMoreColor(self)
        background_log.logger.info("Change Color By Standard: index 9")
        ColorMenu.ChangeColorByStandard(self, 9)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background1-2.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background1-2.png", "./TestCases/Samples/Background/Canvas_Background1-2.png"):
            background_log.logger.info("Case1-2: Canvas_Background Fail!")
            return
        background_log.logger.info("Case1-2: Canvas_Background Pass!")
        background_log.logger.info("Case1-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case1_3(self):
    try:
        background_log.logger.info(
            "Start More Color Advanced Case1-3: 調整Background上的”ADVANCED”顏色")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Select Background Menu: color")
        Background.SelectBackgroundMenu(self, "color")
        background_log.logger.info("Click '+' icon")
        Background.OpenMoreColor(self)
        background_log.logger.info(
            "Change Color By Advanced Color: value(229,169,222,255)")
        ColorMenu.ChangeColorByAdvanced(self, 229, 169, 222, 255)
        background_log.logger.info(
            "Tap coordinate (300,360) to close advanced color menu")
        Canvas.Tap(self, 300, 360)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background1-3.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background1-3.png", "./TestCases/Samples/Background/Canvas_Background1-3.png"):
            background_log.logger.info("Case1-3: Canvas_Background Fail!")
            return
        background_log.logger.info("Case1-3: Canvas_Background Pass!")
        background_log.logger.info("Case1-3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case2_1(self):
    try:
        background_log.logger.info("Start Case2-1: 主題Background套用所有頁面")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Select Background Menu: preinstalled")
        Background.SelectBackgroundMenu(self, "preinstalled")
        background_log.logger.info(
            "Change By Preinstalled Background: index 4, all pages")
        Background.ChangeByPreinstalled(self, 4, "all pages")
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background2-1.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background2-1.png", "./TestCases/Samples/Background/Canvas_Background2-1.png"):
            background_log.logger.info("Case2-1: Canvas_Background Fail!")
            return
        background_log.logger.info("Case2-1: Canvas_Background Pass!")
        background_log.logger.info("New a page")
        FloatBar.NewPage(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Allpages2-1.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Allpages2-1.png", "./TestCases/Samples/Background/Canvas_Allpages2-1.png"):
            background_log.logger.info("Case2-1: All pages Fail!")
            return
        background_log.logger.info("Case2-1: All pages Pass!")
        background_log.logger.info("Case2-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case2_2(self):
    try:
        background_log.logger.info("Start Case2-2: 主題Background套用這一頁")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Select Background Menu: preinstalled")
        Background.SelectBackgroundMenu(self, "preinstalled")
        background_log.logger.info(
            "Change By Preinstalled Background: index 6, this page")
        Background.ChangeByPreinstalled(self, 6, "this page")
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background2-2.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background2-2.png", "./TestCases/Samples/Background/Canvas_Background2-2.png"):
            background_log.logger.info("Case2-2: Canvas_Background Fail!")
            return
        background_log.logger.info("Case2-2: Canvas_Background Pass!")
        background_log.logger.info("New a page")
        FloatBar.NewPage(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Thispage2-2.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Thispage2-2.png", "./TestCases/Samples/Background/Canvas_Thispage2-2.png"):
            background_log.logger.info("Case2-2: This page Fail!")
            return
        background_log.logger.info("Case2-2: This page Pass!")
        background_log.logger.info("Case2-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case3_1(self):
    try:
        background_log.logger.info("Start Case3-1: 套用網格")
        time.sleep(5)
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Click Grid Button to apply grid")
        Background.ClickGridBtn(self)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background3-1.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background3-1.png", "./TestCases/Samples/Background/Canvas_Background3-1.png"):
            background_log.logger.info("Case3-1: Canvas_Background Fail!")
            background_log.logger.info("Open Background Management")
            Background.OpenBackgroundManagement(self)
            background_log.logger.info("Click Grid Button to close grid")
            Background.ClickGridBtn(self)  # close grid
            return
        background_log.logger.info("Case3-1: Canvas_Background Pass!")
        background_log.logger.info("Case3-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case3_2(self):
    try:
        background_log.logger.info("Start Case3-2: 套用浮水印")
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Click Watermark Button to apply watermark")
        Background.ClickWatermarkBtn(self)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background3-2.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background3-2.png", "./TestCases/Samples/Background/Canvas_Background3-2.png"):
            background_log.logger.info("Case3-2: Canvas_Background Fail!")
            background_log.logger.info("Open Background Management")
            Background.OpenBackgroundManagement(self)
            background_log.logger.info(
                "Click Watermark Button to close watermark")
            Background.ClickWatermarkBtn(self)  # close watermark
            return
        background_log.logger.info("Case3-2: Canvas_Background Pass!")
        background_log.logger.info("Case3-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")


def Case3_3(self):
    try:
        background_log.logger.info("Start Case3-3: 套用網格+浮水印")
        background_log.logger.info("Open Background Management")
        Background.OpenBackgroundManagement(self)
        background_log.logger.info("Click Grid Button to apply grid")
        Background.ClickGridBtn(self)
        background_log.logger.info("Click Watermark Button to apply watermark")
        Background.ClickWatermarkBtn(self)
        background_log.logger.info("Close Background Management")
        Background.CloseBackgroundManagement(self)
        background_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Background/Canvas_Background3-3.png")
        background_log.logger.info("Compare Screenshots")
        if not Compare.isImgEqual("./TestCases/Screenshots/Background/Canvas_Background3-3.png", "./TestCases/Samples/Background/Canvas_Background3-3.png"):
            background_log.logger.info("Case3-3: Canvas_Background Fail!")
            background_log.logger.info("Open Background Management")
            Background.OpenBackgroundManagement(self)
            background_log.logger.info("Click Grid Button to close grid")
            Background.ClickGridBtn(self)  # close grid
            background_log.logger.info(
                "Click Watermark Button to close watermark")
            Background.ClickWatermarkBtn(self)  # close watermark
            return
        background_log.logger.info("Case3-3: Canvas_Background Pass!")
        background_log.logger.info("Case3-3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        background_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        background_log.logger.info("Finish")
