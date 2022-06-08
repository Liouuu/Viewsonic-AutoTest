from IntegratedTest.IntergrateBase import IntergrateBase
from Library import Compare
import time

from UnitBase import Canvas, ToolBar


class MarkerTest(IntergrateBase):
    Swipe_pen = [[929, 200], [764, 315], [741, 507], [845, 672],
                 [991, 695], [1037, 564], [914, 484], [756, 534]]

    def Case1_1(self):
        """調整Marker主menu的顏色/粗細/透明並畫出來"""
        ToolBar.Pen.ClickPenBtn()
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

        self.Driver.ScreenshotAndCompare()
        Canvas.CloseMenu()
        self.Driver.Swipe(self.Swipe_pen)
        self.Driver.ScreenshotAndCompare()

    def Case1_2(self):
        """調整Marker主menu上的”STANDARD”顏色/粗細/透明並畫出來"""
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

        self.Driver.ScreenshotAndCompare()
        Canvas.CloseMenu()
        self.Driver.Swipe(self, self.Swipe_pen)
        self.Driver.ScreenshotAndCompare()

    def Case1_3(self):
        """調整Marker主menu上的”ADVANCED”R/G/B/A並畫出來"""
        marker_log.logger.info("打開Marker menu")
        PenMenu.OpenPenMenu(self)
        marker_log.logger.info("點擊”+”icon")
        Marker.OpenMoreColor(self)
        marker_log.logger.info("點擊”ADVANCED”")
        ColorMenu.ChangeColorByAdvanced(self, 0, 230, 230, 200)
        marker_log.logger.info("關閉”ADVANCED Menu”")
        Canva.Tap(self, 1800, 900)  # to close menu
        marker_log.logger.info("調整粗細bar")
        Marker.AdjustThickness(self, 16)
        marker_log.logger.info("調整透明bar")
        Marker.AdjustTransParency(self, 190)
        marker_log.logger.info("選擇一個色域內的顏色icon")
        Marker.ChangeColor(self, 1)
        marker_log.logger.info("再次打開Marker menu")
        PenMenu.OpenPenMenu(self)

        self.Driver.ScreenshotAndCompare()
        Canvas.CloseMenu()
        self.Driver.Swipe(self, self.Swipe_pen)
        self.Driver.ScreenshotAndCompare()
