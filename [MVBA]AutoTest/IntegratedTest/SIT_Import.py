
import time
import datetime
from IntegratedTest.IntergrateBase import IntergrateBase
from Library import Compare
from Params.ElementParams import ElementParam
from UnitBase import Canvas, FloatBar, ToolBar


class ImportTest(IntergrateBase):
    def testImport(self, locate="Local"):
        types = ["video", "audio", "img"]
        for type in types:
            for i in range(3):  # 3 files each type
                ToolBar.Pen.ClickPenBtn(self)
                ToolBar.MagicBox.OpenMagicBox(self)
                if locate == "GoogleDrive":
                    ToolBar.MagicBox.SelectGoogleDrive(self)
                elif locate == "OneDrive":
                    ToolBar.MagicBox.SelectOneDrive(self)
                elif locate == "OneDriveForBusiness":
                    ToolBar.MagicBox.SelectOneDriveForBusiness(self)
                elif locate == "DropBox":
                    ToolBar.MagicBox.SelectDropBox(self)
                elif locate == "Box":
                    ToolBar.MagicBox.SelectBox(self)
                else:
                    ToolBar.MagicBox.SelectStorage(self)
                ToolBar.MagicBox.ChooseFileType(self, type)
                time.sleep(3)
                n = 0
                while self.driver.find_element_by_id(ElementParam._Id_titleTextView).get_attribute(ElementParam._Attr_Text) != "Auto-test":
                    n += 1
                    ToolBar.MagicBox.SelectFile(self, 1)

                while self.driver.find_element_by_id(ElementParam._Id_btnLasso).get_attribute(ElementParam._Attr_Selected) != "true":
                    ToolBar.MagicBox.SelectFile(self, i+1)
                    time.sleep(10)
                Canvas.CloseMenu()
            self.Driver.ScreenshotAndCompare()
            FloatBar.CreateNewPage(self)
