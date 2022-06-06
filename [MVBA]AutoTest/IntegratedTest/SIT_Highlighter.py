from IntegratedTest.IntergrateBase import IntergrateBase
from Library import Compare
from UnitTest import UnitFunc


class HighlighterTest(IntergrateBase):

    def Case1(self):
        UnitFunc.ToolBar.Pen.SelectPenType()

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

        self.Driver.ScreenshotAndCompare()
        UnitFunc.Canvas.CloseMenu()
        my_draw = [[1000, 350], [850, 350], [850, 650],
                   [1000, 650], [1000, 500], [850, 500]]
        self.Driver.Swipe(my_draw)
        self.Driver.Screenshot()
