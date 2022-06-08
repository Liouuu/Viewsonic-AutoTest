import time
from IntegratedTest.IntergrateBase import IntergrateBase
from Library import Compare
from UnitBase import Background, Canvas, FloatBar


class BackgroundTest(IntergrateBase):

    def Case1_1(self):
        """調整Background主menu的顏色"""
        Background.OpenBackgroundManagement(self)
        Background.SelectBackgroundMenu("color")
        Background.PureColor.ChangeByColor(17)
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

    def Case1_2(self):
        """調整Background上的”STANDARD”顏色"""
        Background.OpenBackgroundManagement(self)
        Background.SelectBackgroundMenu(self, "color")
        Background.PureColor.OpenMoreColor()
        Background.PureColor.ChangeColorByStandard(9)
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

    def Case1_3(self):
        """調整Background上的”ADVANCED”顏色"""
        Background.OpenBackgroundManagement()
        Background.SelectBackgroundMenu("color")
        Background.PureColor.OpenMoreColor()
        Background.PureColor.ChangeColorByAdvanced(229, 169, 222, 255)
        """Tap coordinate (300,360) to close advanced color menu")"""
        Canvas.Tap(self, 300, 360)
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

    def Case2_1(self):
        """主題Background套用所有頁面"""
        Background.OpenBackgroundManagement()
        Background.SelectBackgroundMenu("preinstalled")
        Background.Preset.ChangeByPreinstalled(4, "all pages")
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

        FloatBar.CreateNewPage()
        self.Driver.ScreenshotAndCompare()

    def Case2_2(self):
        """主題Background套用這一頁"""
        Background.OpenBackgroundManagement()
        Background.SelectBackgroundMenu("preinstalled")
        Background.Preset.ChangeByPreinstalled(6, "this page")
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

        FloatBar.CreateNewPage()
        self.Driver.ScreenshotAndCompare()

    def Case3_1(self):
        """套用網格"""
        Background.OpenBackgroundManagement()
        Background.ClickGridBtn()
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()

    def Case3_2(self):
        """套用浮水印"""
        Background.OpenBackgroundManagement(self)
        Background.ClickWatermarkBtn(self)
        Canvas.CloseMenu(self)
        self.Driver.ScreenshotAndCompare()

    def Case3_3(self):
        """套用網格+浮水印"""
        Background.OpenBackgroundManagement(self)
        Background.ClickGridBtn(self)
        Background.ClickWatermarkBtn(self)
        Canvas.CloseMenu(self)
        self.Driver.ScreenshotAndCompare()
