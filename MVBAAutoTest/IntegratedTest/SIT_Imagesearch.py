import time

from IntegratedTest.IntergrateBase import IntergrateBase
from UnitBase import ToolBar


class ImagesearchTest(IntergrateBase):

    def ImportimagetypeCase(self, type="svg"):  # Image type:"png" , "svg" , "gif"
        LoginAndActive.NormalLogin(
            self, "mvbaautotest2@gmail.com", "$Password1")

        ToolBar.MagicBox.OpenMagicBox()
        ToolBar.MagicBox.Image.SelectImageSearch()
        ToolBar.MagicBox.Image.InputSearch()
        result, result2 = ToolBar.MagicBox.Image.ImportImage(type)

        if result == "搜尋超時，請稍後再試~":
            sheet['C7'] = result
            return
        elif result == True:
            sheet['C7'] = "搜索到Image參數:" + result2
            sheet['C8'] = "搜索到Image檔案格式:" + result2[-3::]
            sheet['B9'] = "Try import image!"
        else:
            sheet['C8'] = result2
            return

        result3, result4 = ToolBar.MagicBox.Image.CheckType(
            self, type)
        if result3 == "Import異常，請稍後再試~":
            sheet['C9'] = result3
            return
        elif result3 == True:
            sheet['B10'] = "Check Imported Image type"
            sheet['C9'] = "成功import"
            sheet['C10'] = "成功import的image為:" + result4
            sheet['C11'] = "Check Image type Pass!"
        else:
            sheet['C10'] = "成功import的Image為:" + \
                result4 + "! 與實際Type不匹配，請稍後再試~"
