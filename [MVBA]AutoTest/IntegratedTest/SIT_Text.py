from IntegratedTest import IntergrateBase
from Params.ElementParams import ElementParam
from UnitBase import Canvas, ToolBar
from selenium.webdriver.common.by import By


class TextTest(IntergrateBase.IntergrateBase):

    def testCase1(self):
        """在畫布建立文字編輯器，然後更改Font跟Size並套用Bold，接著輸入文字。"""
        ToolBar.Text.SelectTextBtn()
        ToolBar.Text.SelectTextBtn()
        self.Driver.Tap(900, 250)
        self.Driver.Tap(900, 250)
        ToolBar.Text.SetTextFont(3)
        ToolBar.Text.SetTextFont(9)
        ToolBar.Text.Bold()
        ToolBar.Text.TypeText("testcaseone")
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()
        self.Driver.ScreenshotAndCompare()

    def testCase2(self):
        """在畫布建立文字編輯器，然後更改Font跟Size並套用Italic，接著更改文字顏色(“Advanced”)以及底色(“STANDARD”)，再輸入文字。"""
        ToolBar.Text.SelectTextBtn()
        self.Driver.Tap(self, 900, 500)
        self.Driver.Tap(self, 900, 500)
        ToolBar.Text.SetTextFont(6)
        ToolBar.Text.SetTextSize(13)
        ToolBar.Text.Italic()
        ToolBar.Text.SetTextColor(R=130, G=107, B=70)
        ToolBar.Text.SetBGColor(R=130, G=107, B=70)
        ToolBar.Text.TypeText("testcasetwo")
        self.Driver.ScreenshotAndCompare()
        self.Driver.ScreenshotAndCompare()

    def testCase3(self):
        """在畫布建立文字編輯器，然後更改Font跟Size並套用UnderLine，接著更改文字顏色(“STANDARD”)以及底色(“Advanced”)，再輸入文字。"""
        ToolBar.Text.SelectTextBtn()
        ToolBar.Text.SelectTextBtn()
        self.Driver.Tap(self, 900, 750)
        self.Driver.Tap(self, 900, 750)
        ToolBar.Text.SetTextFont(9)
        ToolBar.Text.SetTextSize(15)
        ToolBar.Text.UnderLine()
        ToolBar.Text.SetTextColor(ColorNum=6)
        ToolBar.Text.SetBGColor("Advanced", R=110, G=200, B=90)
        ToolBar.Text.TypeText("testcasethree")
        Canvas.CloseMenu()
        self.Driver.ScreenshotAndCompare()
        self.Driver.ScreenshotAndCompare()
