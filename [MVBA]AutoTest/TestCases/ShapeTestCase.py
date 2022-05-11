import datetime
import time
from UnitFunction import ColorMenu, Shape, Canvas, Screenshot, Compare, FloatBar, log
import sys
import os
sys.path.append(os.getcwd())

Shape_log = log.Logger(
    './Output/Logs/Shape'+datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S') + '.log', level='info')


def run_shapes(self, start, end, shapeNum):
    try:
        Shape_log.logger.info("Start ShapeCase")
        time.sleep(3)
        for i in range(start, end):
            Shape_log.logger.info("Open the ShapeMenu")
            Shape.OpenShapeMenu(self)
            time.sleep(2)
            Shape.SelectShape(self, shapeNum)
            time.sleep(2)
            if shapeNum == 1:
                Shape_log.logger.info("Select 2D Shapes")
                ShapesTest(self, i)
                Shape_log.logger.info("2D Shapes Finish")
            elif shapeNum == 2:
                Shape_log.logger.info("Select 3D Shapes")
                shapes3DTest(self, i)
                Shape_log.logger.info("3D shapes Finish")
            else:
                Shape_log.logger.info("Select Lines")
                LineTest(self, i)
                Shape_log.logger.info("Lines Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Shape_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Shape_log.logger.info("Finish")


def runMenu(self, ThickNum, TransNum, Num):
    Shape_log.logger.info("Adjust Thickness")
    Shape.AdjustThickness(self, ThickNum)
    time.sleep(1)
    Shape_log.logger.info("Adjust TransParency")
    Shape.AdjustTransParency(self, TransNum)
    time.sleep(1)
    Shape_log.logger.info("Change Color")
    Shape.ChangeColor(self, Num)
    time.sleep(1)


def finishMenu(self, num, menuPath):
    Shape_log.logger.info("Select Pattern")
    Shape.SelectPattern(self, num)
    Shape_log.logger.info("Open ShapeMenu again")
    Shape.OpenShapeMenu(self)
    Shape_log.logger.info("Screenshot ShapeMenu " + str(num))
    Screenshot.screenshotShapesMenu(self, menuPath)
    time.sleep(2)
    Shape_log.logger.info("Close ShapeMenu" + str(num))
    Shape.CloseMenu(self)


def ShapesTest(self, num):  # Nomal Test ##
    method = num % 3
    menuPath = "./TestCases/Screenshots/Out_shapes/Menu" + str(num) + ".png"
    menuPath_Sample = "./TestCases/Samples/Ex_shapes/Menu" + str(num) + ".png"
    canvasPath = "./TestCases/Screenshots/Out_shapes/Canvas" + \
        str(num) + ".png"
    canvasPath_Sample = "./TestCases/Samples/Ex_shapes/Canvas" + \
        str(num) + ".png"
    if method == 1:
        runMenu(self, 15, 100, 2)
        finishMenu(self, num, menuPath)
        if num == 10:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[300, 520], [300, 620]])
        elif num > 10:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[300, 520], [300, 720]])
        else:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[100, 320], [320, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    elif method == 2:
        runMenu(self, 20, 150, 8)
        Shape_log.logger.info("Change Color By Standard")
        ColorMenu.ChangeColorByStandard(self, 15)
        time.sleep(1)
        finishMenu(self, num, menuPath)
        if num > 10:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[800, 520], [800, 720]])
        else:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[800, 320], [1000, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    else:
        runMenu(self, 30, 200, 8)
        Shape_log.logger.info("Change Color By Advanced")
        ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
        Canvas.Tap(self, 1900, 90)  # (1900,90) to touch blank place
        time.sleep(2)
        finishMenu(self, num, menuPath)
        if num == 9:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[1400, 520], [1400, 620]])
        elif num == 3 or num > 10:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[1400, 520], [1400, 720]])
        else:
            Shape_log.logger.info("Create 2D shape " + str(num))
            Canvas.Swipe(self, [[1400, 320], [1800, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "ShapesTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
        Shape_log.logger.info("換頁囉")
        FloatBar.NewPage(self)


def shapes3DTest(self, num):
    method = num % 3
    menuPath = "./TestCases/Screenshots/Out_3D/Menu" + str(num) + ".png"
    menuPath_Sample = "./TestCases/Samples/Ex_3D/Menu" + str(num) + ".png"
    canvasPath = "./TestCases/Screenshots/Out_3D/Canvas" + str(num) + ".png"
    canvasPath_Sample = "./TestCases/Samples/Ex_3D/Canvas" + str(num) + ".png"
    if method == 1:
        runMenu(self, 15, 100, 2)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create 3D shape " + str(num))
        Canvas.Swipe(self, [[100, 320], [320, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    elif method == 2:
        runMenu(self, 20, 150, 8)
        Shape_log.logger.info("Change Color By Standard")
        ColorMenu.ChangeColorByStandard(self, 15)
        time.sleep(2)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create 3D shape " + str(num))
        Canvas.Swipe(self, [[800, 320], [1000, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    else:
        runMenu(self, 30, 200, 8)
        Shape_log.logger.info("Change Color By Advanced")
        ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
        Canvas.Tap(self, 1900, 90)  # (1900,90) to touch blank place
        time.sleep(2)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create 3D shape " + str(num))
        Canvas.Swipe(self, [[1200, 320], [1800, 590]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "Shapes3DTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
        Shape_log.logger.info("換頁囉")
        FloatBar.NewPage(self)


def LineTest(self, num):
    method = num % 3
    menuPath = "./TestCases/Screenshots/Out_lines/Menu" + str(num) + ".png"
    menuPath_Sample = "./TestCases/Samples/Ex_lines/Menu" + str(num) + ".png"
    canvasPath = "./TestCases/Screenshots/Out_lines/Canvas" + str(num) + ".png"
    canvasPath_Sample = "./TestCases/Samples/Ex_lines/Canvas" + \
        str(num) + ".png"
    if method == 1:
        runMenu(self, 15, 100, 2)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create Line " + str(num))
        Canvas.Swipe(self, [[300, 300], [600, 600]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    elif method == 2:
        runMenu(self, 20, 150, 8)
        Shape_log.logger.info("Change Color By Standard")
        ColorMenu.ChangeColorByStandard(self, 15)
        time.sleep(1)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create Line " + str(num))
        Canvas.Swipe(self, [[800, 300], [1100, 600]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
    else:
        runMenu(self, 30, 200, 8)
        Shape_log.logger.info("Change Color By Advanced")
        ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
        Canvas.Tap(self, 1900, 90)  # (1900,90) to touch blank place
        time.sleep(1)
        finishMenu(self, num, menuPath)
        Shape_log.logger.info("Create Line " + str(num))
        Canvas.Swipe(self, [[1300, 300], [1600, 600]])
        Shape_log.logger.info("Screenshot Canvas " + str(num))
        Screenshot.screenshotCanvas(self, canvasPath)
        Shape_log.logger.info("比對 Screenshot Menu " + str(num))
        if not Compare.isImgEqual(menuPath, menuPath_Sample):
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info("LineTest Case: Menu " + str(num) + " Pass!")
        Shape_log.logger.info("比對 Screenshot Canvas " + str(num))
        if not Compare.isImgEqual(canvasPath, canvasPath_Sample):
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Fail!")
            # return
        else:
            Shape_log.logger.info(
                "LineTest Case: Canvas " + str(num) + " Pass!")
        time.sleep(2)
        Shape_log.logger.info("換頁囉")
        FloatBar.NewPage(self)
