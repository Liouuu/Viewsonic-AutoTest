from ast import Delete
from TestCases import *
from TestCases.CaseBase import CaseBase
from UnitFunction import UnitFunc
from UnitFunction import *
from UnitFunction.UnitFunc import *
from Library.LibLogHelper import LogPackage
from Library.LibWebDriver import LibWebDriver as LWD
from Library import *


class Step:
    """"Adorner測試共用步驟"""

    def __init__(self, driver: LWD, log: LogPackage):
        self.SelectObject = None  # 選筆
        self.Draw = []
        self.Select = []
        self.ReplicateObj = []
        self.Driver = driver
        self.Log = log

        self.Canvas = Canvas(driver, log)
        self.ToolBar = ToolBar(driver, log)
        self.Adorner = Adorner(driver, log)
        self.FloatBar = FloatBar(driver, log)
        self.Background = Background(driver, log)

    def CreateObject(self):
        self.SelectObject()
        self.Canvas.CreateObjectOnMarker(self.Draw)
        self.ToolBar.ClickLasso()
        self.Canvas.SelectObject(self.Select)

    def OpenAdorner(self):
        self.CreateObject()
        self.Driver.ScreenshotAndCheck()

    def Delete(self):
        self.CreateObject()
        self.Adorner.ClickDeleteBtn()
        self.Driver.ScreenshotAndCheck()

    def Lock(self):
        self.CreateObject()
        self.Adorner.ClickLockBtn()
        self.Driver.ScreenshotAndCheck()
        self.ToolBar.Eraser.ClickEraserBtn()
        self.Canvas.EraseObj(845, 549)  # ?
        self.Driver.ScreenshotAndCheck()

    def HyperLink(self):
        pass  # 2022-05-30 暫不測試

    def CopyPaste(self):
        self.CreateObject()
        self.Adorner.ClickCopyBtn()
        self.FloatBar.Paste()
        self.Driver.ScreenshotAndCheck()

    def CutPaste(self):
        self.CreateObject()
        self.Adorner.ClickCutBtn()
        self.Driver.ScreenshotAndCheck()
        self.FloatBar.CreateNewPage()
        self.FloatBar.Paste()
        self.Driver.ScreenshotAndCheck()

    def Replicate(self):
        Step.CreateObject()
        self.Adorner.ClickReplicateBtn()
        self.Driver.Screenshot()
        self.Driver.Swipe("SwipeObject")
        self.Driver.Swipe("SwipeObject")
        self.Driver.ScreenshotAndCheck()

    def Layer(self):
        pass

    def SetLineStroke(self):
        self.CreateObject()
        self.Adorner.ClickStrokeWidthBtn()
        self.Adorner.SetStrokeWidthBar(32)
        self.Adorner.ClickStrokeWidthBtn()
        self.Driver.ScreenshotAndCheck()

    def SetTransparency(self):
        self.CreateObject()
        self.Adorner.ClickOpacityBtn()
        self.Adorner.SetOpacityBar(128)
        self.Adorner.ClickOpacityBtn()
        self.Driver.ScreenshotAndCheck()

    def SetPalette(self):
        self.CreateObject()
        self.Adorner.ClickColorButton()
        self.Adorner.ChangeColorStandard(1)
        self.Driver.ScreenshotAndCheck()
        self.Adorner.ClickColorButton()
        # Action.SetColor 晚點調整
        self.Adorner.ColorMenu.ChangeColorByAdvanced(0, 255, 255, 200)
        # close color menu 待調整：關閉Color Menu
        self.Driver.Tap(1900, 500)
        self.Driver.ScreenshotAndCheck()

    def Flip(self):
        self.CreateObject()
        self.Adorner.ClickFlipButton()
        self.Adorner.doFlip("Y")
        self.Driver.ScreenshotAndCheck()
        self.Adorner.doFlip("X")
        self.Driver.ScreenshotAndCheck()

    def Mirror(self):
        self.CreateObject()
        self.Adorner.ClickMirrorButton()
        dirs = ["Top", "Bottom", "Left", "Right"]
        for dir in dirs:
            Adorner.doMirror(dir)
        self.Driver.ScreenshotAndCheck()

    def Fill(self):
        self.CreateObject()
        self.Adorner.buttonFill()


class AdornerTestCase:
    def __init__(self, driver: LWD = LWD.default(True, LogPackage("Adorner"))):
        self.PenCase = AdornerTestCase.Pen(driver, driver.Log)
        self.Shape_2dCase = AdornerTestCase.Shape_2D(driver, driver.Log)
        self.Shape_3dCase = AdornerTestCase.Shape_3D(driver, driver.Log)
        self.LineCase = AdornerTestCase.Line(driver, driver.Log)
        self.TextCase = AdornerTestCase.Text(driver, driver.Log)

    class Pen(Step):
        def __init__(self, driver: LWD, log: LogPackage):
            super().__init__(driver, log)
            self.Draw = [[929, 200], [764, 315], [741, 507], [
                845, 672], [991, 695], [1037, 564], [914, 484], [756, 534]]
            self.Select = [[522, 626], [1275, 607]]
            self.ReplicateObj = [[902, 568], [1586, 561]]
            self.SelectObject = self.ToolBar.pen.ClickPenBtn

        def ExecCase(self):
            self.Case01_OpenAdornerMenu()
            self.Case02_Delete()
            self.Case03_Lock()
            self.Case04_HyperLink()
            self.Case05_CopyPaste()
            self.Case06_CutPaste()
            self.Case07_Replicate()
            self.Case08_Layer()
            self.Case09_SetLineStroke()
            self.Case10_SetTransparency()
            self.Case11_SetPalette()
            self.Case12_Flip()
            self.Case13_Mirror()

        def Case01_OpenAdornerMenu(self):
            """Case 1-1: Adorner menu 正確顯示"""
            self.Log.SheetName = "Case 1"
            self.OpenAdorner()

        def Case02_Delete(self):
            """Case 1-2: Delete功能是否正確運作"""
            self.Log.SheetName = "Case 2"
            Step.Delete()

        def Case03_Lock(self):
            """Case 1-3: Lock 功能正確運作"""
            self.Log.SheetName = "Case 3"
            Step.Lock()

        def Case04_HyperLink(self):
            """超連結暫時略過測試-2022/05/26"""
            Step.HyperLink()

        def Case05_CopyPaste(self):
            """Copy &Paste 功能正確運作"""
            self.Log.SheetName = "Case 5"
            Step.CopyPaste()

        def Case06_CutPaste(self):
            """Cut & Paste功能正確運作"""
            self.Log.SheetName = "Case 6"
            Step.CutPaste()

        def Case07_Replicate(self):
            """Replicate 功能正確運作"""
            self.Log.SheetName = "Case 7"
            Step.Replicate()

        def Case08_Layer(self):
            pass  # 分層先跳過 2022-05-30

        def Case09_SetLineStroke(self):
            self.Log.SheetName = "Case 9"
            Step.SetLineStroke()

        def Case10_SetTransparency(self):
            self.Log.SheetName = "Case 10"
            Step.SetTransparency()

        def Case11_SetPalette(self):
            self.Log.SheetName = "Case 11"
            Step.SetPalette()

        def Case12_Flip(self):
            self.Log.SheetName = "Case 12"
            Step.Flip()

        def Case13_Mirror(self):
            self.Log.SheetName = "Case 13"
            Step.Mirror()

    class Shape_2D(Step):
        def __init__(self, driver: LWD, log: LogPackage):
            super().__init__(driver, log)
            self.Select = [[900, 400], [1000, 500]]
            self.ReplicateObj = [[950, 450], [1400, 650]]
            self.SelectObject = self.ToolBar.Shape.ClickShape

        def Case01_OpenAdornerMenu(self):
            """Case 1-1: Adorner menu 正確顯示"""
            self.Log.SheetName = "Case 1"
            Step.OpenAdorner()

        def Case02_Delete(self):
            """Case 1-2: Delete功能是否正確運作"""
            self.Log.SheetName = "Case 2"
            Step.Delete()

        def Case03_Lock(self):
            """Case 1-3: Lock 功能正確運作"""
            self.Log.SheetName = "Case 3"
            Step.Lock()

        def Case04_HyperLink(self):
            """超連結暫時略過測試-2022/05/26"""
            Step.HyperLink()

        def Case05_CopyPaste(self):
            """Copy &Paste 功能正確運作"""
            self.Log.SheetName = "Case 5"
            Step.CopyPaste()

        def Case06_CutPaste(self):
            """Cut & Paste功能正確運作"""
            self.Log.SheetName = "Case 6"
            Step.CutPaste()

        def Case07_Replicate(self):
            """Replicate 功能正確運作"""
            self.Log.SheetName = "Case 7"
            Step.Replicate()

        def Case08_Layer(self):
            pass  # 分層先跳過 2022-05-30

        def Case09_SetLineStroke(self):
            self.Log.SheetName = "Case 9"
            Step.SetLineStroke()

        def Case10_SetPalette(self):
            self.Log.SheetName = "Case 10"
            Step.SetPalette()

        def Case11_Flip(self):
            self.Log.SheetName = "Case 11"
            Step.Flip()

        def Case12_Mirror(self):
            self.Log.SheetName = "Case 12"
            Step.Mirror()

        def Case13_Fill(self):
            pass  # 暫時不測?
            self.Log.SheetName = "Case 13"
            Step.Fill()

        def Case14_SetTransparency(self):
            pass  # 暫時不測?
            self.Log.SheetName = "Case 14"
            Step.SetTransparency()

    class Shape_3D(Step):

        def __init__(self, driver: LWD, log: LogPackage):
            super().__init__(driver, log)
            self.Draw = []
            self.Select = [[900, 400], [1000, 500]]
            self.ReplicateObj = [[950, 450], [1400, 650]]
            self.SelectObject = self.ToolBar.Shape.SelectShape

        def Clcik3dShape(self):
            ToolBar.Shape.SelectShape(2)

        def Case01_OpenAdornerMenu(self):
            """Case 1-1: Adorner menu 正確顯示"""
            self.Log.SheetName = "Case 1"
            Step.OpenAdorner()

        def Case02_Delete(self):
            """Case 1-2: Delete功能是否正確運作"""
            self.Log.SheetName = "Case 2"
            Step.Delete()

        def Case03_Lock(self):
            """Case 1-3: Lock 功能正確運作"""
            self.Log.SheetName = "Case 3"
            Step.Lock()

        def Case04_HyperLink(self):
            """超連結暫時略過測試-2022/05/26"""
            Step.HyperLink()

        def Case05_CopyPaste(self):
            """Copy &Paste 功能正確運作"""
            self.Log.SheetName = "Case 5"
            Step.CopyPaste()

        def Case06_CutPaste(self):
            """Cut & Paste功能正確運作"""
            self.Log.SheetName = "Case 6"
            Step.CutPaste()

        def Case07_Replicate(self):
            """Replicate 功能正確運作"""
            self.Log.SheetName = "Case 7"
            Step.Replicate()

        def Case08_Layer(self):
            pass  # 分層先跳過 2022-05-30

        def Case09_SetLineStroke(self):
            self.Log.SheetName = "Case 9"
            Step.SetLineStroke()

        def Case10_SetPalette(self):
            self.Log.SheetName = "Case 10"
            Step.SetPalette()

        def Case11_Flip(self):
            self.Log.SheetName = "Case 11"
            Step.Flip()

        def Case12_Mirror(self):
            self.Log.SheetName = "Case 12"
            Step.Mirror()

        def Case13_Fill(self):
            pass  # 暫時不測?
            self.Log.SheetName = "Case 13"
            Step.Fill()

        def Case14_SetTransparency(self):
            pass  # 暫時不測?
            self.Log.SheetName = "Case 14"
            Step.SetTransparency()

    class Line(Step):
        def __init__(self, driver: LWD, log: LogPackage):
            super().__init__(driver, log)
            self.Draw = [[929, 200], [764, 315], [741, 507], [
                845, 672], [991, 695], [1037, 564], [914, 484], [756, 534]]
            self.Select = [[522, 626], [1275, 607]]
            self.ReplicateObj = [[902, 568], [1586, 561]]
            self.SelectObject = self.ToolBar.Shape.SelectShape

        def Case01_OpenAdornerMenu(self):
            """Case 1-1: Adorner menu 正確顯示"""
            self.Log.SheetName = "Case 1"
            Step.OpenAdorner()

        def Case02_Delete(self):
            """Case 1-2: Delete功能是否正確運作"""
            self.Log.SheetName = "Case 2"
            Step.Delete()

        def Case03_Lock(self):
            """Case 1-3: Lock 功能正確運作"""
            self.Log.SheetName = "Case 3"
            Step.Lock()

        def Case04_HyperLink(self):
            """超連結暫時略過測試-2022/05/26"""
            Step.HyperLink()

        def Case05_CopyPaste(self):
            """Copy &Paste 功能正確運作"""
            self.Log.SheetName = "Case 5"
            Step.CopyPaste()

        def Case06_CutPaste(self):
            """Cut & Paste功能正確運作"""
            self.Log.SheetName = "Case 6"
            Step.CutPaste()

        def Case07_Replicate(self):
            """Replicate 功能正確運作"""
            self.Log.SheetName = "Case 7"
            Step.Replicate()

        def Case08_Layer(self):
            pass  # 分層先跳過 2022-05-30

        def Case09_SetLineStroke(self):
            self.Log.SheetName = "Case 9"
            Step.SetLineStroke()

        def Case10_SetTransparency(self):
            self.Log.SheetName = "Case 10"
            Step.SetTransparency()

        def Case11_SetPalette(self):
            self.Log.SheetName = "Case 11"
            Step.SetPalette()

        def Case12_Flip(self):
            self.Log.SheetName = "Case 12"
            Step.Flip()

        def Case13_Mirror(self):
            self.Log.SheetName = "Case 13"
            Step.Mirror()

    class Text(Step):
        def __init__(self, driver: LWD, log: LogPackage):
            super().__init__(driver, log)
            self.Draw = []
            self.Select = [[960, 161], [956, 392]]
            self.ReplicateObj = [[1044, 269], [269, 549]]
            self.SelectObject = self.ToolBar.Text.SelectTextBtn

        def Case01_OpenAdornerMenu(self):
            """Case 1-1: Adorner menu 正確顯示"""
            self.Log.SheetName = "Case 1"
            Step.OpenAdorner()

        def Case02_Delete(self):
            """Case 1-2: Delete功能是否正確運作"""
            self.Log.SheetName = "Case 2"
            Step.Delete()

        def Case03_Lock(self):
            """Case 1-3: Lock 功能正確運作"""
            self.Log.SheetName = "Case 3"
            Step.Lock()

        def Case04_HyperLink(self):
            """超連結暫時略過測試-2022/05/26"""
            Step.HyperLink()

        def Case05_CopyPaste(self):
            """Copy &Paste 功能正確運作"""
            self.Log.SheetName = "Case 5"
            Step.CopyPaste()

        def Case06_CutPaste(self):
            """Cut & Paste功能正確運作"""
            self.Log.SheetName = "Case 6"
            Step.CutPaste()

        def Case07_Replicate(self):
            """Replicate 功能正確運作"""
            self.Log.SheetName = "Case 7"
            Step.Replicate()

        def Case08_Layer(self):
            pass  # 分層先跳過 2022-05-30

        def Case9_Flip(self):
            self.Log.SheetName = "Case 12"
            Step.Flip()

        def Case10_Mirror(self):
            self.Log.SheetName = "Case 13"
            Step.Mirror()
