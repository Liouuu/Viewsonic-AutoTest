from UnitFunction import Canvas, Screenshot, Compare, Adorner, ToolBar, FloatBar, ColorMenu, Shape, log, Text
import time
import datetime
import sys
import os
sys.path.append(os.getcwd())


#------------------#
#   Case 1: Pen    #
#------------------#

Swipe_pen = [[929, 200], [764, 315], [741, 507], [845, 672],
             [991, 695], [1037, 564], [914, 484], [756, 534]]
Select_object = [[522, 626], [1275, 607]]
Replicate_object = [[902, 568], [1586, 561]]

adorner_log = log.Logger(
    './Output/Logs/adorner '+datetime.datetime.now().strftime(" %Y-%m-%d_%H_%M_%S") + '.log', level='info')


def Case1_1(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)  # 畫出物件
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)  # 選取物件
    adorner_log.logger.info("Screenshot Adorner Menu")
    Screenshot.screenshotAdornerMenu(
        self, "./TestCases/Screenshots/Adorner/Pen/Menu/Menu.png")
    adorner_log.logger.info("Compare Adorner Menu")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Menu/Menu.png", "./TestCases/Samples/Adorner/Pen/Menu/Menu.png"):
        adorner_log.logger.info("Case1-1: Pen_AdornerMenu Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-1 Pass!")


def Case1_2(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Delete Button")
    Adorner.buttonDelete(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Delete/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Delete/Canvas.png", "./TestCases/Samples/Adorner/Pen/Delete/Canvas.png"):
        adorner_log.logger.info("Case1-2: Delete Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-2 Pass!")


def Case1_3(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Lock Button")
    Adorner.buttonLocked(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Pen/Lock/Lock.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Lock/Lock.png", "./TestCases/Samples/Adorner/Pen/Lock/Lock.png"):
        adorner_log.logger.info("Case1-3: Lock icon Fail!")
        return
    adorner_log.logger.info("Select Eraser Button")
    ToolBar.SelectEraserBtn(self)
    time.sleep(2)
    adorner_log.logger.info("Try to Erase Object")
    Canvas.Tap(self, 845, 549)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Lock/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Lock/Canvas.png", "./TestCases/Samples/Adorner/Pen/Lock/Canvas.png"):
        adorner_log.logger.info("Case1-3: Lock Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-3 Pass!")


def Case1_4(self):
    adorner_log.logger.info("hyperlink skip")
    pass  # 超連結先跳過


def Case1_5(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Copy Button")
    Adorner.buttonCopy(self)
    time.sleep(2)
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Copy/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Copy/Canvas.png", "./TestCases/Samples/Adorner/Pen/Copy/Canvas.png"):
        adorner_log.logger.info("Case1-5: Copy Paste Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-5 Pass!")


def Case1_6(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Cut Button")
    Adorner.buttonCut(self)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Cut/Canvas1.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Cut/Canvas1.png", "./TestCases/Samples/Adorner/Pen/Cut/Canvas1.png"):
        adorner_log.logger.info("Case1-6: Cut Fail!")
        return
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Cut/Canvas2.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Cut/Canvas2.png", "./TestCases/Samples/Adorner/Pen/Cut/Canvas2.png"):
        adorner_log.logger.info("Case1-6: Paste Cut Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-6 Pass!")


def Case1_7(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Replicate Button")
    Adorner.buttonReplicate(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Pen/Replicate/Replicate.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Replicate/Replicate.png", "./TestCases/Samples/Adorner/Pen/Replicate/Replicate.png"):
        adorner_log.logger.info("Case1-7: Replicate Fail!")
        return
    time.sleep(2)
    adorner_log.logger.info("Replicate")
    Canvas.Swipe(self, Replicate_object)
    Canvas.Swipe(self, Replicate_object)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Replicate/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Replicate/Canvas.png", "./TestCases/Samples/Adorner/Pen/Replicate/Canvas.png"):
        adorner_log.logger.info("Case1-7: Paste Replicate Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-7 Pass!")


def Case1_8(self):
    adorner_log.logger.info("layer skip")
    pass  # 分層先跳過


def Case1_9(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Adjust Stroke Width: value 32")
    Adorner.seekBarStrokeWidth(self, 32)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/StrokeWidth/StrokeWidth.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/StrokeWidth/StrokeWidth.png", "./TestCases/Samples/Adorner/Pen/StrokeWidth/StrokeWidth.png"):
        adorner_log.logger.info("Case1-9: StrokeWidth Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-9 Pass!")


def Case1_10(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Transparency Button")
    Adorner.buttonTransparency(self)
    adorner_log.logger.info("Adjust Transparency: value 128")
    Adorner.seekBarAlpha(self, 128)
    adorner_log.logger.info("Click Transparency Button")
    Adorner.buttonTransparency(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Transparency/Transparency.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Transparency/Transparency.png", "./TestCases/Samples/Adorner/Pen/Transparency/Transparency.png"):
        adorner_log.logger.info("Case1-10: Transparency Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-10 Pass!")


def Case1_11(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Standard: index 1")
    ColorMenu.ChangeColorByStandard(self, 1)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Color/StandardColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Color/StandardColor.png", "./TestCases/Samples/Adorner/Pen/Color/StandardColor.png"):
        adorner_log.logger.info("Case1-11: Standard Color Fail!")
        return
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Advanced: value (0,255,255,200)")
    ColorMenu.ChangeColorByAdvanced(self, 0, 255, 255, 200)
    adorner_log.logger.info("Tap coordinate (1900,500) to close color menu")
    Canvas.Tap(self, 1900, 500)  # close color menu
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Color/AdvancedColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Color/AdvancedColor.png", "./TestCases/Samples/Adorner/Pen/Color/AdvancedColor.png"):
        adorner_log.logger.info("Case1-11: Advanced Color Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-11 Pass!")


def Case1_12(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Flip Button")
    Adorner.buttonFlip(self)
    adorner_log.logger.info("Flip: dir Y")
    Adorner.doFlip(self, "Y")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Flip/FlipY.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Flip/FlipY.png", "./TestCases/Samples/Adorner/Pen/Flip/FlipY.png"):
        adorner_log.logger.info("Case1-12: FlipY Fail!")
        return
    adorner_log.logger.info("Flip: dir X")
    Adorner.doFlip(self, "X")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Flip/FlipX.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Flip/FlipX.png", "./TestCases/Samples/Adorner/Pen/Flip/FlipX.png"):
        adorner_log.logger.info("Case1-12: FlipX Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-12 Pass!")


def Case1_13(self):
    time.sleep(5)
    adorner_log.logger.info("Create Pen Object")
    Canvas.Swipe(self, Swipe_pen)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_object)
    adorner_log.logger.info("Click Mirror Button")
    Adorner.buttonMirror(self)
    dirs = ["Top", "Bottom", "Left", "Right"]
    for dir in dirs:
        adorner_log.logger.info("Mirror: dir " + dir)
        Adorner.doMirror(self, dir)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Pen/Mirror/Mirror.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Pen/Mirror/Mirror.png", "./TestCases/Samples/Adorner/Pen/Mirror/Mirror.png"):
        adorner_log.logger.info("Case1-13: Mirror Fail!")
        return
    adorner_log.logger.info("Adorner Case 1-13 Pass!")

#------------------#
#   Case 2: Shape  #
#------------------#


Swipe_shape = [[900, 400], [1000, 500]]
Replicate_shape = [[950, 450], [1400, 650]]


def Case2_1(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Screenshot Adorner Menu")
    Screenshot.screenshotAdornerMenu(
        self, "./TestCases/Screenshots/Adorner/Shape/Menu/Menu.png")
    adorner_log.logger.info("Compare Adorner Menu")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Menu/Menu.png", "./TestCases/Samples/Adorner/Shape/Menu/Menu.png"):
        adorner_log.logger.info("Case2-1: Shape_AdornerMenu Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-1 Pass!")


def Case2_2(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Delete Button")
    Adorner.buttonDelete(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Delete/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Delete/Canvas.png", "./TestCases/Samples/Adorner/Shape/Delete/Canvas.png"):
        adorner_log.logger.info("Case2-2: Delete Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-2 Pass!")


def Case2_3(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Lock Button")
    Adorner.buttonLocked(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Shape/Lock/Lock.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Lock/Lock.png", "./TestCases/Samples/Adorner/Shape/Lock/Lock.png"):
        adorner_log.logger.info("Case2-3: Lock icon Fail!")
        return
    adorner_log.logger.info("Select Eraser Button")
    ToolBar.SelectEraserBtn(self)
    time.sleep(2)
    adorner_log.logger.info("Try to Erase Object")
    Canvas.Tap(self, Swipe_shape[0][0]+10, Swipe_shape[0][1]+10)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Lock/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Lock/Canvas.png", "./TestCases/Samples/Adorner/Shape/Lock/Canvas.png"):
        adorner_log.logger.info("Case2-3: Lock Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-3 Pass!")


def Case2_4(self):
    adorner_log.logger.info("hyperlink skip")
    pass  # 超連結先跳過


def Case2_5(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Copy Button")
    Adorner.buttonCopy(self)
    time.sleep(2)
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Copy/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Copy/Canvas.png", "./TestCases/Samples/Adorner/Shape/Copy/Canvas.png"):
        adorner_log.logger.info("Case2-5: Copy Paste Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-5 Pass!")


def Case2_6(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Cut Button")
    Adorner.buttonCut(self)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Cut/Canvas1.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Cut/Canvas1.png", "./TestCases/Samples/Adorner/Shape/Cut/Canvas1.png"):
        adorner_log.logger.info("Case2-6: Cut Fail!")
        return
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Cut/Canvas2.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Cut/Canvas2.png", "./TestCases/Samples/Adorner/Shape/Cut/Canvas2.png"):
        adorner_log.logger.info("Case2-6: Paste Cut Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-6 Pass!")


def Case2_7(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Replicate Button")
    Adorner.buttonReplicate(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Shape/Replicate/Replicate.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Replicate/Replicate.png", "./TestCases/Samples/Adorner/Shape/Replicate/Replicate.png"):
        adorner_log.logger.info("Case2-7: Replicate Fail!")
        return
    time.sleep(2)
    adorner_log.logger.info("Replicate")
    Canvas.Swipe(self, Swipe_shape)
    Canvas.Swipe(self, Replicate_shape)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Replicate/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Replicate/Canvas.png", "./TestCases/Samples/Adorner/Shape/Replicate/Canvas.png"):
        adorner_log.logger.info("Case2-7: Paste Replicate Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-7 Pass!")


def Case2_8(self):
    adorner_log.logger.info("layer skip")
    pass  # 分層先跳過


def Case2_9(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Adjust Stroke Width: value 32")
    Adorner.seekBarStrokeWidth(self, 32)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/StrokeWidth/StrokeWidth.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/StrokeWidth/StrokeWidth.png", "./TestCases/Samples/Adorner/Shape/StrokeWidth/StrokeWidth.png"):
        adorner_log.logger.info("Case2-9: StrokeWidth Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-9 Pass!")


def Case2_10(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Standard: index 1")
    ColorMenu.ChangeColorByStandard(self, 1)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Color/StandardColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Color/StandardColor.png", "./TestCases/Samples/Adorner/Shape/Color/StandardColor.png"):
        adorner_log.logger.info("Case2-10: Standard Color Fail!")
        return
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Advanced: value (0,255,255,200)")
    ColorMenu.ChangeColorByAdvanced(self, 0, 255, 255, 200)
    adorner_log.logger.info("Tap coordinate (1900,500) to close color menu")
    Canvas.Tap(self, 1900, 500)  # close color menu
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Color/AdvancedColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Color/AdvancedColor.png", "./TestCases/Samples/Adorner/Shape/Color/AdvancedColor.png"):
        adorner_log.logger.info("Case2-10: Advanced Color Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-10 Pass!")


def Case2_11(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Flip Button")
    Adorner.buttonFlip(self)
    adorner_log.logger.info("Flip: dir Y")
    Adorner.doFlip(self, "Y")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Flip/FlipY.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Flip/FlipY.png", "./TestCases/Samples/Adorner/Shape/Flip/FlipY.png"):
        adorner_log.logger.info("Case2-11: FlipY Fail!")
        return
    adorner_log.logger.info("Flip: dir X")
    Adorner.doFlip(self, "X")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Flip/FlipX.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Flip/FlipX.png", "./TestCases/Samples/Adorner/Shape/Flip/FlipX.png"):
        adorner_log.logger.info("Case2-11: FlipX Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-11 Pass!")


def Case2_12(self):
    time.sleep(5)
    adorner_log.logger.info("Click Shape Button")
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Create Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Mirror Button")
    Adorner.buttonMirror(self)
    dirs = ["Top", "Bottom", "Left", "Right"]
    for dir in dirs:
        adorner_log.logger.info("Mirror: dir " + dir)
        Adorner.doMirror(self, dir)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Shape/Mirror/Mirror.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Shape/Mirror/Mirror.png", "./TestCases/Samples/Adorner/Shape/Mirror/Mirror.png"):
        adorner_log.logger.info("Case2-12: Mirror Fail!")
        return
    adorner_log.logger.info("Adorner Case 2-12 Pass!")


def Case2_13(self):
    # 目前版本1.35.1-s尚未修正Fill和Transparency icon bug，暫時Skip
    adorner_log.logger.info("Fill skip")


def Case2_14(self):
    # 目前版本1.35.1-s尚未修正Fill和Transparency icon bug，暫時Skip
    adorner_log.logger.info("Transparency skip")

#------------------#
#  Case 3:3D Shape #
#------------------#


def select3DShape(self):
    adorner_log.logger.info("Click Shape Button twice to open menu")
    ToolBar.SelectShapeBtn(self)
    ToolBar.SelectShapeBtn(self)
    adorner_log.logger.info("Select 3D Shape")
    Shape.SelectShape(self, 2)
    adorner_log.logger.info("Close Shape Menu")
    Shape.CloseMenu(self)


def Case3_1(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Screenshot Adorner Menu")
    Screenshot.screenshotAdornerMenu(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Menu/Menu.png")
    adorner_log.logger.info("Compare Adorner Menu")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Menu/Menu.png", "./TestCases/Samples/Adorner/3D Shape/Menu/Menu.png"):
        adorner_log.logger.info("Case3-1: 3D Shape_AdornerMenu Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-1 Pass!")


def Case3_2(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Delete Button")
    Adorner.buttonDelete(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Delete/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Delete/Canvas.png", "./TestCases/Samples/Adorner/3D Shape/Delete/Canvas.png"):
        adorner_log.logger.info("Case3-2: Delete Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-2 Pass!")


def Case3_3(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Lock Button")
    Adorner.buttonLocked(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Lock/Lock.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Lock/Lock.png", "./TestCases/Samples/Adorner/3D Shape/Lock/Lock.png"):
        adorner_log.logger.info("Case3-3: Lock icon Fail!")
        return
    adorner_log.logger.info("Select Eraser Button")
    ToolBar.SelectEraserBtn(self)
    time.sleep(2)
    adorner_log.logger.info("Try to Erase Object")
    Canvas.Tap(self, Swipe_shape[0][0]+10, Swipe_shape[0][1]+10)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Lock/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Lock/Canvas.png", "./TestCases/Samples/Adorner/3D Shape/Lock/Canvas.png"):
        adorner_log.logger.info("Case3-3: Lock Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-3 Pass!")


def Case3_4(self):
    adorner_log.logger.info("hyperlink skip")
    pass  # 超連結先跳過


def Case3_5(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Copy Button")
    Adorner.buttonCopy(self)
    time.sleep(2)
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Copy/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Copy/Canvas.png", "./TestCases/Samples/Adorner/3D Shape/Copy/Canvas.png"):
        adorner_log.logger.info("Case3-5: Copy Paste Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-5 Pass!")


def Case3_6(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Cut Button")
    Adorner.buttonCut(self)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Cut/Canvas1.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Cut/Canvas1.png", "./TestCases/Samples/Adorner/3D Shape/Cut/Canvas1.png"):
        adorner_log.logger.info("Case3-6: Cut Fail!")
        return
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Cut/Canvas2.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Cut/Canvas2.png", "./TestCases/Samples/Adorner/3D Shape/Cut/Canvas2.png"):
        adorner_log.logger.info("Case3-6: Paste Cut Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-6 Pass!")


def Case3_7(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Replicate Button")
    Adorner.buttonReplicate(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Replicate/Replicate.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Replicate/Replicate.png", "./TestCases/Samples/Adorner/3D Shape/Replicate/Replicate.png"):
        adorner_log.logger.info("Case3-7: Replicate Fail!")
        return
    time.sleep(2)
    adorner_log.logger.info("Replicate")
    Canvas.Swipe(self, Swipe_shape)
    Canvas.Swipe(self, Replicate_shape)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Replicate/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Replicate/Canvas.png", "./TestCases/Samples/Adorner/3D Shape/Replicate/Canvas.png"):
        adorner_log.logger.info("Case3-7: Paste Replicate Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-7 Pass!")


def Case3_8(self):
    adorner_log.logger.info("layer skip")
    pass  # 分層先跳過


def Case3_9(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Adjust Stroke Width: value 32")
    Adorner.seekBarStrokeWidth(self, 32)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/StrokeWidth/StrokeWidth.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/StrokeWidth/StrokeWidth.png", "./TestCases/Samples/Adorner/3D Shape/StrokeWidth/StrokeWidth.png"):
        adorner_log.logger.info("Case3-9: StrokeWidth Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-9 Pass!")


def Case3_10(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Standard: index 1")
    ColorMenu.ChangeColorByStandard(self, 1)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Color/StandardColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Color/StandardColor.png", "./TestCases/Samples/Adorner/3D Shape/Color/StandardColor.png"):
        adorner_log.logger.info("Case3-10: Standard Color Fail!")
        return
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Advanced: value (0,255,255,200)")
    ColorMenu.ChangeColorByAdvanced(self, 0, 255, 255, 200)
    adorner_log.logger.info("Tap coordinate (1900,500) to close color menu")
    Canvas.Tap(self, 1900, 500)  # close color menu
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Color/AdvancedColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Color/AdvancedColor.png", "./TestCases/Samples/Adorner/3D Shape/Color/AdvancedColor.png"):
        adorner_log.logger.info("Case3-10: Advanced Color Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-10 Pass!")


def Case3_11(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Flip Button")
    Adorner.buttonFlip(self)
    adorner_log.logger.info("Flip: dir Y")
    Adorner.doFlip(self, "Y")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Flip/FlipY.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Flip/FlipY.png", "./TestCases/Samples/Adorner/3D Shape/Flip/FlipY.png"):
        adorner_log.logger.info("Case3-11: FlipY Fail!")
        return
    adorner_log.logger.info("Flip: dir X")
    Adorner.doFlip(self, "X")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Flip/FlipX.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Flip/FlipX.png", "./TestCases/Samples/Adorner/3D Shape/Flip/FlipX.png"):
        adorner_log.logger.info("Case3-11: FlipX Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-11 Pass!")


def Case3_12(self):
    time.sleep(5)
    select3DShape(self)
    adorner_log.logger.info("Create 3D Shape Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Swipe_shape)
    adorner_log.logger.info("Click Mirror Button")
    Adorner.buttonMirror(self)
    dirs = ["Top", "Bottom", "Left", "Right"]
    for dir in dirs:
        adorner_log.logger.info("Mirror: dir " + dir)
        Adorner.doMirror(self, dir)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/3D Shape/Mirror/Mirror.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/3D Shape/Mirror/Mirror.png", "./TestCases/Samples/Adorner/3D Shape/Mirror/Mirror.png"):
        adorner_log.logger.info("Case3-12: Mirror Fail!")
        return
    adorner_log.logger.info("Adorner Case 3-12 Pass!")


def Case3_13(self):
    # 目前版本1.35.1-s尚未修正Fill和Transparency icon bug，暫時Skip
    adorner_log.logger.info("Fill skip")


def Case3_14(self):
    # 目前版本1.35.1-s尚未修正Fill和Transparency icon bug，暫時Skip
    adorner_log.logger.info("Transparency skip")

#------------------#
#   Case 4: Line   #
#------------------#


Swipe_line = [[714, 307], [1167, 687]]
Select_line = [[614, 507], [1152, 484]]
Replicate_line = [[787, 488], [1321, 495]]


def Case4_1(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)  # 畫出物件
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)  # 選取物件
    adorner_log.logger.info("Screenshot Adorner Menu")
    Screenshot.screenshotAdornerMenu(
        self, "./TestCases/Screenshots/Adorner/Line/Menu/Menu.png")
    adorner_log.logger.info("Compare Adorner Menu")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Menu/Menu.png", "./TestCases/Samples/Adorner/Line/Menu/Menu.png"):
        adorner_log.logger.info("Case4-1: Line_AdornerMenu Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-1 Pass!")


def Case4_2(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Delete Button")
    Adorner.buttonDelete(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Delete/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Delete/Canvas.png", "./TestCases/Samples/Adorner/Line/Delete/Canvas.png"):
        adorner_log.logger.info("Case4-2: Delete Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-2 Pass!")


def Case4_3(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Lock Button")
    Adorner.buttonLocked(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Line/Lock/Lock.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Lock/Lock.png", "./TestCases/Samples/Adorner/Line/Lock/Lock.png"):
        adorner_log.logger.info("Case4-3: Lock icon Fail!")
        return
    adorner_log.logger.info("Select Eraser Button")
    ToolBar.SelectEraserBtn(self)
    time.sleep(2)
    adorner_log.logger.info("Try to Erase Object")
    Canvas.Tap(self, 845, 549)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Lock/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Lock/Canvas.png", "./TestCases/Samples/Adorner/Line/Lock/Canvas.png"):
        adorner_log.logger.info("Case4-3: Lock Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-3 Pass!")


def Case4_4(self):
    adorner_log.logger.info("hyperlink skip")
    pass  # 超連結先跳過


def Case4_5(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Copy Button")
    Adorner.buttonCopy(self)
    time.sleep(2)
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Copy/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Copy/Canvas.png", "./TestCases/Samples/Adorner/Line/Copy/Canvas.png"):
        adorner_log.logger.info("Case4-5: Copy Paste Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-5 Pass!")


def Case4_6(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Cut Button")
    Adorner.buttonCut(self)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Cut/Canvas1.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Cut/Canvas1.png", "./TestCases/Samples/Adorner/Line/Cut/Canvas1.png"):
        adorner_log.logger.info("Case4-6: Cut Fail!")
        return
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Cut/Canvas2.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Cut/Canvas2.png", "./TestCases/Samples/Adorner/Line/Cut/Canvas2.png"):
        adorner_log.logger.info("Case4-6: Paste Cut Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-6 Pass!")


def Case4_7(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Replicate Button")
    Adorner.buttonReplicate(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Line/Replicate/Replicate.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Replicate/Replicate.png", "./TestCases/Samples/Adorner/Line/Replicate/Replicate.png"):
        adorner_log.logger.info("Case4-7: Replicate Fail!")
        return
    time.sleep(2)
    adorner_log.logger.info("Replicate")
    Canvas.Swipe(self, Replicate_line)
    Canvas.Swipe(self, Replicate_line)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Replicate/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Replicate/Canvas.png", "./TestCases/Samples/Adorner/Line/Replicate/Canvas.png"):
        adorner_log.logger.info("Case4-7: Paste Replicate Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-7 Pass!")


def Case4_8(self):
    adorner_log.logger.info("layer skip")
    pass  # 分層先跳過


def Case4_9(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Adjust Stroke Width: value 32")
    Adorner.seekBarStrokeWidth(self, 32)
    adorner_log.logger.info("Click Stroke Width Button")
    Adorner.buttonStrokeWidth(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/StrokeWidth/StrokeWidth.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/StrokeWidth/StrokeWidth.png", "./TestCases/Samples/Adorner/Line/StrokeWidth/StrokeWidth.png"):
        adorner_log.logger.info("Case4-9: StrokeWidth Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-9 Pass!")


def Case4_10(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Transparency Button")
    Adorner.buttonTransparency(self)
    adorner_log.logger.info("Adjust Transparency: value 128")
    Adorner.seekBarAlpha(self, 128)
    adorner_log.logger.info("Click Transparency Button")
    Adorner.buttonTransparency(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Transparency/Transparency.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Transparency/Transparency.png", "./TestCases/Samples/Adorner/Line/Transparency/Transparency.png"):
        adorner_log.logger.info("Case4-10: Transparency Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-10 Pass!")


def Case4_11(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Standard: index 1")
    ColorMenu.ChangeColorByStandard(self, 1)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Color/StandardColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Color/StandardColor.png", "./TestCases/Samples/Adorner/Line/Color/StandardColor.png"):
        adorner_log.logger.info("Case4-11: Standard Color Fail!")
        return
    adorner_log.logger.info("Click Color Button")
    Adorner.buttonColor(self)
    adorner_log.logger.info("Change Color By Advanced: value (0,255,255,200)")
    ColorMenu.ChangeColorByAdvanced(self, 0, 255, 255, 200)
    adorner_log.logger.info("Tap coordinate (1900,500) to close color menu")
    Canvas.Tap(self, 1900, 500)  # close color menu
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Color/AdvancedColor.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Color/AdvancedColor.png", "./TestCases/Samples/Adorner/Line/Color/AdvancedColor.png"):
        adorner_log.logger.info("Case4-11: Advanced Color Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-11 Pass!")


def Case4_12(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Flip Button")
    Adorner.buttonFlip(self)
    adorner_log.logger.info("Flip: dir Y")
    Adorner.doFlip(self, "Y")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Flip/FlipY.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Flip/FlipY.png", "./TestCases/Samples/Adorner/Line/Flip/FlipY.png"):
        adorner_log.logger.info("Case4-12: FlipY Fail!")
        return
    adorner_log.logger.info("Flip: dir X")
    Adorner.doFlip(self, "X")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Flip/FlipX.png")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Flip/FlipX.png", "./TestCases/Samples/Adorner/Line/Flip/FlipX.png"):
        adorner_log.logger.info("Case4-12: FlipX Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-12 Pass!")


def Case4_13(self, LineNum=2):
    time.sleep(5)
    adorner_log.logger.info("Open Shape Menu")
    Shape.OpenShapeMenu(self)
    time.sleep(2)
    adorner_log.logger.info("Select Lines")
    Shape.SelectShape(self, 3)
    adorner_log.logger.info("Select Pattern" + str(LineNum))
    Shape.SelectPattern(self, LineNum)
    time.sleep(2)
    adorner_log.logger.info("Draw object")
    Canvas.Swipe(self, Swipe_line)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select object")
    Canvas.Swipe(self, Select_line)
    adorner_log.logger.info("Click Mirror Button")
    Adorner.buttonMirror(self)
    dirs = ["Top", "Bottom", "Left", "Right"]
    for dir in dirs:
        adorner_log.logger.info("Mirror: dir " + dir)
        Adorner.doMirror(self, dir)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Line/Mirror/Mirror.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Line/Mirror/Mirror.png", "./TestCases/Samples/Adorner/Line/Mirror/Mirror.png"):
        adorner_log.logger.info("Case4-13: Mirror Fail!")
        return
    adorner_log.logger.info("Adorner Case 4-13 Pass!")

#------------------#
#   Case 5: text   #
#------------------#


Select_text = [[960, 161], [956, 392]]
Replicate_text = [[1044, 269], [269, 549]]


def Case5_1(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornermenu'")
    Text.TypeText(self, "testadornermenu")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)  # 選取物件
    adorner_log.logger.info("Screenshot Adorner Menu")
    Screenshot.screenshotAdornerMenu(
        self, "./TestCases/Screenshots/Adorner/Text/Menu/Menu.png")
    adorner_log.logger.info("Compare Adorner Menu")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Menu/Menu.png", "./TestCases/Samples/Adorner/Text/Menu/Menu.png"):
        adorner_log.logger.info("Case5-1: Text_AdornerMenu Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-1 Pass!")


def Case5_2(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornerdelete'")
    Text.TypeText(self, "testadornerdelete")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Delete Button")
    Adorner.buttonDelete(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Delete/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Delete/Canvas.png", "./TestCases/Samples/Adorner/Text/Delete/Canvas.png"):
        adorner_log.logger.info("Case5-2: Delete Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-2 Pass!")


def Case5_3(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornerlock'")
    Text.TypeText(self, "testadornerlock")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Lock Button")
    Adorner.buttonLocked(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Text/Lock/Lock.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Lock/Lock.png", "./TestCases/Samples/Adorner/Text/Lock/Lock.png"):
        adorner_log.logger.info("Case5-3: Lock icon Fail!")
        return
    adorner_log.logger.info("Select Eraser Button")
    ToolBar.SelectEraserBtn(self)
    time.sleep(2)
    adorner_log.logger.info("Try to Erase Object")
    Canvas.Tap(self, 1044, 269)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Lock/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Lock/Canvas.png", "./TestCases/Samples/Adorner/Text/Lock/Canvas.png"):
        adorner_log.logger.info("Case5-3: Lock Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-3 Pass!")


def Case5_4(self):
    adorner_log.logger.info("hyperlink skip")
    pass  # 超連結先跳過


def Case5_5(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornercopy'")
    Text.TypeText(self, "testadornercopy")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Copy Button")
    Adorner.buttonCopy(self)
    time.sleep(2)
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Copy/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Copy/Canvas.png", "./TestCases/Samples/Adorner/Text/Copy/Canvas.png"):
        adorner_log.logger.info("Case5-5: Copy Paste Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-5 Pass!")


def Case5_6(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornercut'")
    Text.TypeText(self, "testadornercut")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Cut Button")
    Adorner.buttonCut(self)
    time.sleep(2)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Cut/Canvas1.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Cut/Canvas1.png", "./TestCases/Samples/Adorner/Text/Cut/Canvas1.png"):
        adorner_log.logger.info("Case5-6: Cut Fail!")
        return
    adorner_log.logger.info("New a Page")
    FloatBar.NewPage(self)
    time.sleep(2)
    adorner_log.logger.info("Paste")
    FloatBar.Paste(self)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Cut/Canvas2.png")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Cut/Canvas2.png", "./TestCases/Samples/Adorner/Text/Cut/Canvas2.png"):
        adorner_log.logger.info("Case5-6: Paste Cut Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-6 Pass!")


def Case5_7(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornerreplicate'")
    Text.TypeText(self, "testadornerreplicate")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Replicate Button")
    Adorner.buttonReplicate(self)
    adorner_log.logger.info("Screenshot Object Box")
    Screenshot.screenshotObjectBox(
        self, "./TestCases/Screenshots/Adorner/Text/Replicate/Replicate.png")
    adorner_log.logger.info("Compare Object Box")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Replicate/Replicate.png", "./TestCases/Samples/Adorner/Text/Replicate/Replicate.png"):
        adorner_log.logger.info("Case5-7: Replicate Fail!")
        return
    time.sleep(2)
    adorner_log.logger.info("Replicate")
    Canvas.Swipe(self, Replicate_text)
    Canvas.Swipe(self, Replicate_text)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Replicate/Canvas.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Replicate/Canvas.png", "./TestCases/Samples/Adorner/Text/Replicate/Canvas.png"):
        adorner_log.logger.info("Case5-7: Paste Replicate Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-7 Pass!")


def Case5_8(self):
    adorner_log.logger.info("layer skip")
    pass  # 分層先跳過


def Case5_9(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornerflip'")
    Text.TypeText(self, "testadornerflip")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Flip Button")
    Adorner.buttonFlip(self)
    adorner_log.logger.info("Flip: dir Y")
    Adorner.doFlip(self, "Y")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Flip/FlipY.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Flip/FlipY.png", "./TestCases/Samples/Adorner/Text/Flip/FlipY.png"):
        adorner_log.logger.info("Case5-9: FlipY Fail!")
        return
    adorner_log.logger.info("Flip: dir X")
    Adorner.doFlip(self, "X")
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Flip/FlipX.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Flip/FlipX.png", "./TestCases/Samples/Adorner/Text/Flip/FlipX.png"):
        adorner_log.logger.info("Case5-9: FlipX Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-9 Pass!")


def Case5_10(self):
    time.sleep(5)
    adorner_log.logger.info("Click Text Button")
    Text.SelectTextBtn(self)
    Text.SelectTextBtn(self)
    adorner_log.logger.info("Tap canvas to open Text Editor")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Click to enable typing")
    Canvas.Tap(self, 900, 250)
    adorner_log.logger.info("Type : 'testadornermirror'")
    Text.TypeText(self, "testadornermirror")
    adorner_log.logger.info("Close Text Editor")
    Text.CloseEditor(self)
    adorner_log.logger.info("Click Select Button")
    ToolBar.SelectObject(self)
    adorner_log.logger.info("Select Object")
    Canvas.Swipe(self, Select_text)
    adorner_log.logger.info("Click Mirror Button")
    Adorner.buttonMirror(self)
    dirs = ["Top", "Bottom", "Left", "Right"]
    for dir in dirs:
        adorner_log.logger.info("Mirror: dir " + dir)
        Adorner.doMirror(self, dir)
    adorner_log.logger.info("Screenshot Canvas")
    Screenshot.screenshotCanvas(
        self, "./TestCases/Screenshots/Adorner/Text/Mirror/Mirror.png")
    adorner_log.logger.info("Compare Canvas")
    if not Compare.isImgEqual("./TestCases/Screenshots/Adorner/Text/Mirror/Mirror.png", "./TestCases/Samples/Adorner/Text/Mirror/Mirror.png"):
        adorner_log.logger.info("Case5-10: Mirror Fail!")
        return
    adorner_log.logger.info("Adorner Case 5-10 Pass!")