from UnitFunction import ColorMenu, Canvas, Screenshot, Compare, log
from UnitFunction.Pen import Marker, PenMenu
import datetime
import time
import sys
import os
sys.path.append(os.getcwd())

Swipe_pen = [[929, 200], [764, 315], [741, 507], [845, 672],
             [991, 695], [1037, 564], [914, 484], [756, 534]]
marker_log = log.Logger(
    './Output/Logs/Marker '+datetime.datetime.now().strftime(" %Y-%m-%d_%H_%M_%S") + '.log', level='info')


def Case1_1(self):
    try:
        marker_log.logger.info(
            "Start Color Menu Case1-1: 調整Marker主menu的顏色/粗細/透明並畫出來")
        time.sleep(5)
        marker_log.logger.info("打開Marker menu")
        PenMenu.OpenPenMenu(self)
        marker_log.logger.info("選擇一個色域icon")
        Marker.ChangeColor(self, 20)
        marker_log.logger.info("調整粗細bar")
        Marker.AdjustThickness(self, 25)
        marker_log.logger.info("調整透明bar")
        Marker.AdjustTransParency(self, 200)
        marker_log.logger.info("選擇一個色域內的顏色icon")
        Marker.ChangeColor(self, 1)
        marker_log.logger.info("再次打開Marker menu")
        PenMenu.OpenPenMenu(self)
        time.sleep(2)
        marker_log.logger.info("將整個menu截圖")
        Screenshot.screenshotPenMenu(
            self, "./TestCases/Screenshots/Pen/Marker/Menu_Marker1-1.png")
        marker_log.logger.info("比對Menu")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Menu_Marker1-1.png", "./TestCases/Samples/Pen/Marker/Menu_Marker1-1.png"):
            marker_log.logger.info("Case1-1: Menu_Marker Fail!")
            return
        marker_log.logger.info("Case1-1: Menu_Marker Pass!")
        time.sleep(2)
        marker_log.logger.info("關閉Menu")
        PenMenu.ClosePenMenu(self)
        time.sleep(2)
        marker_log.logger.info("在畫布畫出一個6")
        Canvas.Swipe(self, Swipe_pen)
        marker_log.logger.info("將整個畫布截圖")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-1.png")
        marker_log.logger.info("比對Canvas")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-1.png", "./TestCases/Samples/Pen/Marker/Canvas_Marker1-1.png"):
            marker_log.logger.info("Case1-1: Canvas_Marker Fail!")
            return
        marker_log.logger.info("Marker Case 1-1 Pass!")
        marker_log.logger.info("Case 1-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        marker_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        marker_log.logger.info("Finish")


def Case1_2(self):
    try:
        marker_log.logger.info(
            "Start More Color Standard Case1-2: 調整Marker主menu上的”STANDARD”顏色/粗細/透明並畫出來")
        time.sleep(5)
        marker_log.logger.info("打開Marker menu")
        PenMenu.OpenPenMenu(self)
        marker_log.logger.info("點擊”+”icon")
        Marker.OpenMoreColor(self)
        marker_log.logger.info("點擊”STANDARD”")
        ColorMenu.ChangeColorByStandard(self, 11)
        marker_log.logger.info("調整粗細bar")
        Marker.AdjustThickness(self, 15)
        marker_log.logger.info("調整透明bar")
        Marker.AdjustTransParency(self, 150)
        marker_log.logger.info("選擇一個色域內的顏色icon")
        Marker.ChangeColor(self, 1)
        marker_log.logger.info("再次打開Marker menu")
        PenMenu.OpenPenMenu(self)
        time.sleep(2)
        marker_log.logger.info("將整個menu截圖")
        Screenshot.screenshotPenMenu(
            self, "./TestCases/Screenshots/Pen/Marker/Menu_Marker1-2.png")
        marker_log.logger.info("比對Menu")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Menu_Marker1-2.png", "./TestCases/Samples/Pen/Marker/Menu_Marker1-2.png"):
            marker_log.logger.info("Case1-2: Menu_Marker Fail!")
            return
        marker_log.logger.info("Case1-2: Menu_Marker Pass!")
        time.sleep(2)
        marker_log.logger.info("關閉Menu")
        PenMenu.ClosePenMenu(self)
        time.sleep(2)
        marker_log.logger.info("在畫布畫出一個6")
        Canvas.Swipe(self, Swipe_pen)
        marker_log.logger.info("將整個畫布截圖")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-2.png")
        marker_log.logger.info("比對Canvas")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-2.png", "./TestCases/Samples/Pen/Marker/Canvas_Marker1-2.png"):
            marker_log.logger.info("Case1-2: Canvas_Marker Fail!")
            return
        marker_log.logger.info("Marker Case 1-2 Pass!")
        marker_log.logger.info("Case 1-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        marker_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        marker_log.logger.info("Finish")


def Case1_3(self):
    try:
        marker_log.logger.info(
            "Start More Color Advanced Case1-3: 調整Marker主menu上的”ADVANCED”R/G/B/A並畫出來")
        time.sleep(5)
        marker_log.logger.info("打開Marker menu")
        PenMenu.OpenPenMenu(self)
        marker_log.logger.info("點擊”+”icon")
        Marker.OpenMoreColor(self)
        marker_log.logger.info("點擊”ADVANCED”")
        ColorMenu.ChangeColorByAdvanced(self, 0, 230, 230, 200)
        marker_log.logger.info("關閉”ADVANCED Menu”")
        Canvas.Tap(self, 1800, 900)  # to close menu
        marker_log.logger.info("調整粗細bar")
        Marker.AdjustThickness(self, 16)
        marker_log.logger.info("調整透明bar")
        Marker.AdjustTransParency(self, 190)
        marker_log.logger.info("選擇一個色域內的顏色icon")
        Marker.ChangeColor(self, 1)
        marker_log.logger.info("再次打開Marker menu")
        PenMenu.OpenPenMenu(self)
        marker_log.logger.info("將整個menu截圖")
        Screenshot.screenshotPenMenu(
            self, "./TestCases/Screenshots/Pen/Marker/Menu_Marker1-3.png")
        marker_log.logger.info("比對Menu")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Menu_Marker1-3.png", "./TestCases/Samples/Pen/Marker/Menu_Marker1-3.png"):
            marker_log.logger.info("Case1-3: Menu_Marker Fail!")
            return
        marker_log.logger.info("Case1-3: Menu_Marker Pass!")
        marker_log.logger.info("關閉Menu")
        PenMenu.ClosePenMenu(self)
        marker_log.logger.info("在畫布畫出一個6")
        Canvas.Swipe(self, Swipe_pen)
        marker_log.logger.info("將整個畫布截圖")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-3.png")
        marker_log.logger.info("比對Canvas")
        if not Compare.isImgEqual("./TestCases/Screenshots/Pen/Marker/Canvas_Marker1-3.png", "./TestCases/Samples/Pen/Marker/Canvas_Marker1-3.png"):
            marker_log.logger.info("Case1-3: Canvas_Marker Fail!")
            return
        marker_log.logger.info("Marker Case 1-3 Pass!")
        marker_log.logger.info("Case 1-3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        marker_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        marker_log.logger.info("Finish")
