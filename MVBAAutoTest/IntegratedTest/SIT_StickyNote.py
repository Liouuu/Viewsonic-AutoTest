import time
from IntegratedTest import IntergrateBase
from UnitBase import ToolBar


class StickyNote(IntergrateBase.IntergrateBase):
    def Case1_PenOnNote(self):
        ToolBar.MagicBox.OpenMagicBox(self)
        StickyNote.ClickStickynote(self)
        StickyNote.StickynoteColor(self, 2)
        StickyNote.SelectPen(self)
        StickyNote.PenColor(self, "Red")
        StickyNote.PenThickness(self, 8)
        my_draw = [[1000, 350], [850, 350], [850, 650],
                   [1000, 650], [1000, 500], [850, 500]]
        self.Driver.Swipe(self, my_draw)
        StickyNote.CloseStickynote(self)
        self.Driver.ScreenshotAndCompare()
        self.Driver.ScreenshotAndCompare()

    def Case2_TextOnNote(self):
        ToolBar.MagicBox.OpenMagicBox(self)
        StickyNote.ClickStickynote(self)
        StickyNote.StickynoteColor(self, 4)
        StickyNote.SelectText(self)
        StickyNote.ChangeFont(self, 6)
        StickyNote.ChangeSize(self, 20)
        StickyNote.TextBold(self)
        StickyNote.TextItalic(self)
        StickyNote.TextUnderLine(self)
        StickyNote.TypeText(self, "teststickynote")
        StickyNote.SelectPen(self)
        time.sleep(3)
        StickyNote.CloseStickynote(self)
        self.Driver.ScreenshotAndCompare()
        self.Driver.ScreenshotAndCompare()
