import time
from IntegratedTest.IntergrateBase import IntergrateBase

from Library import Compare
from UnitBase import FloatBar

#


class ShapeTest(IntergrateBase):

    def run_shapes(self, start, end, shapeNum):
        """Start ShapeCase"""
        for i in range(start, end):
            Shape.OpenShapeMenu(self)
            time.sleep(2)
            Shape.SelectShape(self, shapeNum)
            time.sleep(2)
            if shapeNum == 1:
                self.ShapesTest(self, i)
            elif shapeNum == 2:
                shapes3DTest(self, i)
            else:
                LineTest(self, i)

    def runMenu(self, ThickNum, TransNum, Num):
        Shape.AdjustThickness(self, ThickNum)
        Shape.AdjustTransParency(self, TransNum)
        Shape.ChangeColor(self, Num)

    def finishMenu(self, num, menuPath):
        Shape.SelectPattern(self, num)
        Shape.OpenShapeMenu(self)
        Shape.CloseMenu(self)

    def ShapesTest(self, num):  # Nomal Test ##
        method = num % 3
        if method == 1:
            runMenu(self, 15, 100, 2)
            finishMenu(self, num, menuPath)
            if num == 10:
                Canva.Swipe(self, [[300, 520], [300, 620]])
            elif num > 10:
                Canva.Swipe(self, [[300, 520], [300, 720]])
            else:
                Canva.Swipe(self, [[100, 320], [320, 590]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        elif method == 2:
            runMenu(self, 20, 150, 8)
            ColorMenu.ChangeColorByStandard(self, 15)
            finishMenu(self, num, menuPath)
            if num > 10:
                Canva.Swipe(self, [[800, 520], [800, 720]])
            else:
                Canva.Swipe(self, [[800, 320], [1000, 590]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        else:
            runMenu(self, 30, 200, 8)
            ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
            Canva.Tap(self, 1900, 90)  # (1900,90) to touch blank place
            finishMenu(self, num, menuPath)
            if num == 9:
                self.Driver.Swipe(self, [[1400, 520], [1400, 620]])
            elif num == 3 or num > 10:
                self.Driver.Swipe(self, [[1400, 520], [1400, 720]])
            else:
                self.Driver.Swipe(self, [[1400, 320], [1800, 590]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
            FloatBar.NewPage(self)

    def shapes3DTest(self, num):
        method = num % 3
        if method == 1:
            runMenu(self, 15, 100, 2)
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[100, 320], [320, 590]])
            Screenshot.screenshotCanvas(self, canvasPath)
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        elif method == 2:
            runMenu(self, 20, 150, 8)
            ColorMenu.ChangeColorByStandard(self, 15)
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[800, 320], [1000, 590]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        else:
            runMenu(self, 30, 200, 8)
            ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
            Canva.Tap(self, 1900, 90)  # (1900,90) to touch blank place
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[1200, 320], [1800, 590]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
            FloatBar.CreateNewPage()

    def LineTest(self, num):
        method = num % 3
        if method == 1:
            runMenu(self, 15, 100, 2)
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[300, 300], [600, 600]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        elif method == 2:
            runMenu(self, 20, 150, 8)
            ColorMenu.ChangeColorByStandard(self, 15)
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[800, 300], [1100, 600]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
        else:
            runMenu(self, 30, 200, 8)
            ColorMenu.ChangeColorByAdvanced(self, 81, 76, 132, 200)
            Canva.Tap(self, 1900, 90)  # (1900,90) to touch blank place
            finishMenu(self, num, menuPath)
            Canva.Swipe(self, [[1300, 300], [1600, 600]])
            self.Driver.ScreenshotAndCompare()
            self.Driver.ScreenshotAndCompare()
            FloatBar.CreateNewPage()
