import datetime
import time
from UnitFunction import Canvas, Screenshot, Compare, log
from UnitFunction.Pen import Highlighter, PenMenu
import sys
import os
sys.path.append(os.getcwd())

highlighter_log = log.Logger('./Output/Logs/Highlighter '+datetime.datetime.now(
).strftime(" %Y-%m-%d_%H_%M_%S") + '.log', level='info')


def Case1(self):
    try:
        highlighter_log.logger.info("Start HighlighterCase")
        highlighter_log.logger.info("Open Pen Menu")
        PenMenu.OpenPenMenu(self)
        highlighter_log.logger.info("Select Highlighter")
        PenMenu.SelectHighlighter(self)
        highlighter_log.logger.info("Change Color: index 2")
        Highlighter.ChangeColor(self, 2)
        highlighter_log.logger.info("Open Pen Menu")
        PenMenu.OpenPenMenu(self)
        highlighter_log.logger.info("Adjust Thickness: value 16")
        Highlighter.AdjustThickness(self, 16)
        highlighter_log.logger.info("Close Pen Menu")
        PenMenu.ClosePenMenu(self)
        highlighter_log.logger.info("Open Pen Menu")
        PenMenu.OpenPenMenu(self)
        highlighter_log.logger.info("Screenshot Pen Menu")
        Screenshot.screenshotPenMenu(
            self, "./TestCases/Screenshots/Pen/Highlighter/Highliter Case 1_menu.png")
        highlighter_log.logger.info("Compare Pen Menu")
        if not Compare.isImgEqual("./TestCases/Samples/Pen/Highlighter/Highliter Case 1_menu.png", "./TestCases/Screenshots/Pen/Highlighter/Highliter Case 1_menu.png"):
            highlighter_log.logger.info("Highlighter Case 1 Fail! (menu)")
            return
        highlighter_log.logger.info("Close Pen Menu")
        PenMenu.ClosePenMenu(self)
        my_draw = [[1000, 350], [850, 350], [850, 650],
                   [1000, 650], [1000, 500], [850, 500]]
        highlighter_log.logger.info(
            "Draw: [[1000,350],[850,350],[850,650],[1000,650],[1000,500],[850,500]]")
        Canvas.Swipe(self, my_draw)
        highlighter_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Pen/Highlighter/Highliter Case 1_canvas.png")
        highlighter_log.logger.info("Compare Canvas")
        if not Compare.isImgEqual("./TestCases/Samples/Pen/Highlighter/Highliter Case 1_canvas.png", "./TestCases/Screenshots/Pen/Highlighter/Highliter Case 1_canvas.png"):
            highlighter_log.logger.info("Highlighter Case 1 Fail! (canvas)")
            return
        highlighter_log.logger.info("Highlighter Case 1 Pass!")
        highlighter_log.logger.info("HighlighterCase Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        highlighter_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        highlighter_log.logger.info("Finish")
