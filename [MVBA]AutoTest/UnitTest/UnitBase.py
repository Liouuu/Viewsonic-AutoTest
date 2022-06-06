from msilib.schema import Class
import time
from appium.webdriver.common.touch_action import TouchAction
from Library import LibLogHelper
from Library.LibWebDriver import LibWebDriver
from Params.ElementParams import ElementParam, c_ElementParam
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FuncBase:
    def __init__(self, driver: LibWebDriver, log: LibLogHelper.LogPackage):
        self.Driver = driver
        self.Log = log


class Canvas(FuncBase):
    def CreateObjectOnMarker(self, positions: list):
        """以Marker在畫布上新增物件"""
        _Action = "以Marker在畫布上新增物件"
        self.Log.AddCaseLog(_Action)
        self.Driver.Swipe(positions)

    def SelectObject(self, positions):
        """選取物件"""
        action = "選取物件"
        self.Log.AddCaseLog(action)
        self.Driver.Swipe(positions)

    def CloseMenu(self):
        """關閉工具箱"""
        action = "關閉工具箱"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonMenuClose, By.ID)

    def EraseObj(self, x, y):
        """以Eraser點擊物件"""
        action = "以Eraser點擊物件"
        self.Log.AddCaseLog(action)
        self.Driver.Tap(x, y)


class Adorner(FuncBase):
    def ClickDeleteBtn(self):
        """點擊Delete按鈕"""
        action = "點擊”Delete按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonDelete, By.ID)

    def ClickLockBtn(self):
        """點擊Lock按鈕"""
        action = "點擊Lock按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonLocked, By.ID)

    def ClickCopyBtn(self):
        """點擊複製按鈕"""
        action = "以複製點擊物件"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonCopy, By.ID)

    def ClickCutBtn(self):
        """點擊剪下按鈕"""
        action = "點擊剪下按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonCut, By.ID)

    def ClickReplicateBtn(self):
        """點擊貼上按鈕"""
        action = "點擊貼上按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonReplicate, By.ID)

    def ClickStrokeWidthBtn(self):
        """點擊線條粗細按鈕"""
        action = "點擊線條粗細按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonStrokeWidth, By.ID)

    def SetStrokeWidthBar(self, val: int):
        """調整粗細"""
        action = "調整粗細，值:{val}"
        self.Log.AddCaseLog(action)
        self.Driver.ElementSetValue(
            action, val, ElementParam._Id_seekBarStrokeWidth, By.ID)

    def ClickOpacityBtn(self):
        """點擊透明度按鈕"""
        action = "點擊透明度按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonAlpha, By.ID)

    def SetOpacityBar(self, val: int):
        """調整透明度"""
        action = "調整透明度，值:{val}"
        self.Log.AddCaseLog(action)
        self.Driver.ElementSetValue(
            action, val, ElementParam._Id_seekBarAlpha, By.ID)

    def ClickColorBtn(self):
        """點擊顏色按鈕"""
        action = "點擊顏色按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_buttonColor, By.ID)

    def ChangeColorStandard(self, index):
        """切換成標準顏色"""
        action = "切換成標準顏色"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonStandard, By.ID)
        # 這邊晚一點調整
        self.Driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(index)+']').click()

    def ClickFlipBtn(self):
        """點擊翻動按鈕"""
        action = "點擊翻動按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonFlip, By.ID)

    def ClickMirrorBtn(self):
        """點擊鏡像按鈕"""
        action = "點擊鏡像按鈕"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonMirror, By.ID)

# 以下待維修

    def buttonSaveResource(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonSaveResource, By.ID)

    def buttonCrop(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonCrop, By.ID)

    def buttonFitToScreen(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonFitToScreen, By.ID)

    def buttonSetAsBackground(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonSetAsBackground, By.ID)

    def buttonFill(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonFill, By.ID)

    def buttonSnapshot(self):
        """ """
        action = ""
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(ElementParam._Id_buttonSnapshot, By.ID)

    def doFlip(self, dir="X"):  # dir = "X" or "Y"
        if not (dir == "X" or dir == "Y"):
            print("Function doFlip parameter wrong!")
            return
        tar = ElementParam._Id_buttonFlip + dir
        self.Driver.ElementClick(tar, By.ID)

    def doMirror(self, dir="Right"):  # dir = "Top", "Bottom", "Left", "Right"
        if not (dir == "Right" or dir == "Left" or dir == "Top" or dir == "Bottom"):
            print("Function doMirror parameter wrong!")
            return
        tar = ElementParam._Id_buttonMirror + dir
        self.Driver.ElementClick(tar, By.ID)


class ToolBar(FuncBase):
    """底下的工具Bar"""

    def __init__(self, driver: LibWebDriver, log: LibLogHelper.LogPackage):
        super().__init__(driver, log)
        self.folder = self.Folder(driver, log)
        self.magicBox = self.MagicBox(driver, log)
        self.browser = self.Browser(driver, log)
        self.pen = self.Pen(driver, log)
        self.eraser = self.Eraser(driver, log)
        self.shape = self.Shape(driver, log)
        self.text = self.Text(driver, log)

    class Folder(FuncBase):
        def OpenFileManagement(self):
            """點擊資料夾"""
            action = "點擊資料夾"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(ElementParam._Id_btnFile, By.ID)

        def ChooseOpenFile(self):
            """選擇檔案"""
            action = "選擇檔案"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(ElementParam._Id_radioFileOpen, By.ID)

        def SelectFile(self, index):
            """選擇檔案(待處理這段)"""
            action = "選擇檔案"
            tar_path = '(//android.widget.ImageView[@content-desc="Whiteboard"])'
            tar_index = '['+str(index)+']'
            tar_path += tar_index
            WebDriverWait(self.Driver, 15).until(
                EC.presence_of_element_located((By.XPATH, tar_path))
            )
            tar = self.Driver.find_element_by_xpath(tar_path)
            tar.click()
            tar.click()
            time.sleep(2)

        def NewFile(self):
            pass

        def Save(self):
            pass

        def SaveAs(self):
            pass

        def Export(self, type: str):
            pass

        def QRcodeShare(self):
            pass

    class MagicBox(FuncBase):
        """百寶箱"""

        def OpenMagicBox(self):
            """打開百寶箱"""
            action = "打開百寶箱"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(ElementParam._Id_btnResource, By.ID)

        # Select a file or a folder, the parameter index is the file index in current folder

        def SelectFile(self, index):
            tar_path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout"
            tar_index = '['+str(index)+']'
            tar_path += tar_index
            WebDriverWait(self.Driver, 15).until(
                EC.presence_of_element_located((By.XPATH, tar_path))
            )
            tar = self.Driver.find_element_by_xpath(tar_path)
            double_click = TouchAction(self.Driver)
            double_click.tap(tar, count=2).perform()
            # time.sleep(2)

        def LastFolder(self):
            WebDriverWait(self.Driver, 15).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_currentFolder))
            )
            cur_folder = self.Driver.find_element_by_id(
                ElementParam._Id_currentFolder)
            double_click = TouchAction(self.Driver)
            double_click.tap(element=cur_folder, count=2).perform()

        # Import all img files under current folder #Files can only be audio, video, img

        def ImportAllFiles(self):
            # time.sleep(5)
            # all_files = self.Driver.find_elements_by_class_name("android.widget.LinearLayout")
            WebDriverWait(self.Driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"))
            )
            all_files = self.Driver.find_elements_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/*")
            # print(len(all_files))
            for i in range(len(all_files)):
                ToolBar.MagicBox.SelectFile(self, i+1)

        def SelectStorage(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioLocalStorage))
            )
            self.Driver.find_element_by_id(
                ElementParam._Id_radioLocalStorage).click()

        def SelectGoogleDrive(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioGoogleDrive))
            )
            self.Driver.find_element_by_id(
                ElementParam._Id_radioGoogleDrive).click()

        def SelectOneDrive(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioOneDrive))
            )
            self.Driver.find_element_by_id(
                ElementParam._Id_radioOneDrive).click()

        def SelectOneDriveForBusiness(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioOneDriveBusiness))
            )
            self.Driver.find_element_by_id(
                ElementParam._Id_radioOneDriveBusiness).click()

        def SelectDropBox(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioDropBox))
            )
            self.Driver.find_element_by_id(
                ElementParam._Id_radioDropBox).click()

        def SelectBox(self):
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located(
                    (By.ID, ElementParam._Id_radioBox))
            )
            self.Driver.find_element_by_id(ElementParam._Id_radioBox).click()

        # the parameter type is a string: 'img', 'video' or 'audio'
        def ChooseFileType(self, type):
            if type == "img":
                self.Driver.find_element_by_id(
                    ElementParam._Id_radioImage).click()
            elif type == "video":
                self.Driver.find_element_by_id(
                    ElementParam._Id_radioVideo).click()
            elif type == "audio":
                self.Driver.find_element_by_id(
                    ElementParam._Id_radioAudio).click()
            else:
                print("CooseFileType wrong")

        class Image:

            def SelectImageSearch(self):
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_radioImageSearch))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_radioImageSearch).click()

            def InputSearch(self, type):
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_searchEditText)))
                self.driver.find_element_by_id(
                    ElementParam._Id_searchEditText).send_keys(type)

                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_search_icon)))
                self.driver.find_element_by_id(
                    ElementParam._Id_search_icon).click()

                search = "搜尋 "+type+" Image"
                WebDriverWait(self.driver, 60, 1).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]'))
                )
                time.sleep(10)
                return search

            def ImportImage(self, type):
                touch = TouchAction(self.driver)
                imagelist = [[791, 499], [945, 499], [1121, 492],
                             [787, 626], [952, 618], [1121, 618]]
                i = 0
                while True:
                    imagetype = self.driver.find_element_by_xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['+str(1+i)+']/android.widget.TextView[1]').get_attribute("text")
                    MOV = "touch.tap(x="+str(imagelist[i][0]) + \
                        ",y="+str(imagelist[i][1])+").perform()"
                    i += 1
                    if imagetype[-3::] == type:
                        break
                    elif i >= 6:
                        result = "暫時無法搜到" + type + "，請稍後再試~"
                        return False, result
                for tap in range(3):
                    exec(MOV)
                return True, imagetype

            def CheckType(self, type):
                MagicBox.CloseMagicBox(self)
                Canva.Select_Object(self, 77, 146, 315, 323)
                time.sleep(10)
                Adorner.buttonSaveResource(self)
                MagicBox.SelectStorage(self)
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_textSaveResourceFormat))
                )
                imagetype = self.driver.find_element_by_id(
                    ElementParam._Id_textSaveResourceFormat).get_attribute("text")

                if imagetype[-3::] == type:
                    return True, imagetype
                else:
                    return False, imagetype

    class Browser(FuncBase):
        """瀏覽器"""
        pass

    def Move():
        pass

    def ClickLasso(self):
        """選擇Lasso工具"""
        action = "選擇Lasso工具"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_btnLasso, By.ID)

    class Pen(FuncBase):
        def ClickPenBtn(self):
            """選擇 筆 工具"""
            action = "選擇 筆 工具"
            self.Log.AddCaseLog(action)
            # self.Driver.ElementClick(action, ElementParam._Id_btnPen, By.ID)
            self.Driver.ElementClcikNotMenu(
                action, ElementParam._Id_btnPen, By.ID)

        def SelectPenType():
            pass

    class Eraser(FuncBase):
        def ClickEraserBtn(self):
            """選擇橡皮擦工具"""
            action = "選擇橡皮擦工具"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action, ElementParam._Id_btnEraser, By.ID)

        def OpenEraserMenu(self):
            """開啟橡皮擦工具目錄"""
            action = "開啟橡皮擦工具目錄"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClcikMenu(
                action, ElementParam._Id_btnEraser, By.ID)

        def ChooseRegularEraser(self):
            """常規橡皮擦?"""
            action = ""
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action, ElementParam._Id_btnEraser, By.ID)

        def ChooseCircleEraser(self):
            """圓圈橡皮擦?"""
            action = ""
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonEraseSelector, By.ID)

        def ClearCanvas(self):
            """清空畫布"""
            action = "清空畫布"
            self.Log.AddCaseLog(self. action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonEraseAll, By.ID)

        # in main bar after click eraser btn one time
        def ChooseRegularEraser_Sub(self):
            """常規橡皮擦2?"""
            action = ""
            self.Log.AddCaseLog(self. action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_btnSubEraserEraser, By.ID)

        # in main bar after click eraser btn one time
        def ChooseCircleEraser_Sub(self):
            """選擇橡皮擦工具"""
            action = "選擇橡皮擦工具"
            self.Log.AddCaseLog(self. action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_btnSubEraserSelector, By.ID)

        # in main bar after click eraser btn one time
        def ClearCanvas_Sub(self):
            """清空畫布"""
            action = "清空畫布"
            self.Log.AddCaseLog(self. action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_btnSubEraserEraserAll, By.ID)

        def SetEraserSize(self, val: int):
            """調整橡皮擦大小"""
            action = "點擊”Lock button”"
            self.Log.AddCaseLog(action)
            self.Driver.ElementSetValue(action,
                                        action, val, ElementParam._Id_seekBar, By.ID)

    class Shape(FuncBase):
        def ClickShape(self):
            """選擇多邊形工具"""
            action = "選擇多邊形工具"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_btnShape, By.ID)

        def OpenShapeMenu(self):
            """開啟多邊形工具目錄"""
            action = "開啟多邊形工具目錄"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClcikMenu(action,
                                         action, ElementParam._Id_btnShape, By.ID)

        # ShapeNum: 1 for shape, 2 for 3D shape, 3 for lines
        def SelectShape(self, ShapeNum):
            """選擇多邊形類型"""
            ToolBar.Shape.OpenShapeMenu()
            action = "選擇多邊形類型"
            self.Log.AddCaseLog(self. action)
            if ShapeNum == 1:  # Shape ##
                self.Driver.ElementClick(
                    ElementParam._Id_radioShape, By.ID)
            elif ShapeNum == 2:  # 3D Shape ##
                self.Driver.ElementClick(
                    ElementParam._Id_radioPseudo3DShape, By.ID)
            elif ShapeNum == 3:  # Lines ##
                self.Driver.ElementClick(
                    ElementParam._Id_radioLines, By.ID)
            Canvas.CloseMenu()

        def SelectPattern(self, Num):  # Num 1-18
            # 待處理
            try:
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']'))
                )
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()
            except:
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()

        # ColorNum: 1 for red, 2 for orange, 3 for yellow...(the third line colors in menu)  #When Colornum = 8, it equals MoreColor() function
        def ChangeColor(self, ColorNum):
            # 待處理
            Num = ColorNum + 16     # Red = 17,Orange = 18, Yellow = 19 ......)
            try:
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()
            except:
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView['+str(Num)+']').click()

        # Use MoreColor() to open color menu, then you can use functions in ColorMenu.py to adjust color.

        def MoreColor(self):
            # 待處理
            try:
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView[24]').click()
            except:
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[9]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView[24]').click()

        def SetThinckness(self, val: int):  # 0~32 ##
            """調整粗細"""
            action = "調整多邊形粗細，值:{val}"
            self.Log.AddCaseLog(action)
            self.Driver.ElementSetValue(action,
                                        action, val, ElementParam._Id_seekBarWidth, By.ID)

    class Text(FuncBase):
        def SelectTextBtn(self):
            """選擇文字輸入工具"""
            action = "選擇文字輸入工具"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_btnTypingText, By.ID)

        def TypeText(self, string: str):
            """輸入文字"""
            action = "輸入文字"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_editText, By.ID)
            for char in string:
                if char >= 'a' and char <= 'z':
                    keycode = str(29 + (ord(char)-ord('a')))
            self.Driver.Driver.press_keycode(keycode)

        def SetTextFont(self, index: int):  # index of font is 1~9
            """設置字形"""
            action = "設置字形"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_spinnerFontName, By.ID)
            time.sleep(1)
            font_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(
                index) + "]"
            self.Driver.find_element_by_xpath(font_xpath).click()

        def SetTextSize(self, index: int):  # index of size is 1~
            """設置字體大小"""
            action = "設置字體大小"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_spinnerFontSize, By.ID)
            time.sleep(1)
            size_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[" + str(
                index) + "]"
            self.Driver.find_element_by_xpath(size_xpath).click()

        def Bold(self):
            """設置粗體"""
            action = "設置粗體"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkBold, By.ID)

        def Italic(self):
            """設置斜體"""
            action = "設置斜體"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkItalic, By.ID)

        def UnderLine(self):
            """設置底線"""
            action = "設置底線"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkUnderline, By.ID)

        def EditTextClear(self, text):
            """清空文字框"""
            self.Driver.press_keycode('123')
            for i in range(0, len(text)):
                self.Driver.press_keycode('67')

        def SetTextColor(self, type: str = "Standard", ColorNum: int = 1, R=255, G=255, B=255, A=255):
            """設置字體顏色"""
            action = "設置字體顏色"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonColor, By.ID)
            if type == "Standard":
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonStandard))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_buttonStandard).click()
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
            elif type == "Advanced":
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonAdvanced))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_buttonAdvanced).click()
                for i in range(4):
                    pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + \
                        "[" + str(i+1) + "]" + \
                        "/android.view.ViewGroup/android.widget.EditText"
                    pattern = self.Driver.find_element_by_xpath(
                        pattern_xpath)
                    if str(i+1) == "1":
                        pattern.click()
                        context1 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context1)
                        pattern.send_keys(R)
                        self.Driver.press_keycode('66')

                    elif str(i+1) == "2":
                        pattern.click()
                        context2 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context2)
                        pattern.send_keys(G)
                        self.Driver.press_keycode('66')
                    elif str(i+1) == "3":
                        pattern.click()
                        context3 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context3)
                        pattern.send_keys(B)
                        self.Driver.press_keycode('66')
                    else:
                        pattern.click()
                        context4 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context4)
                        pattern.send_keys(A)
                        self.Driver.press_keycode('66')
                        self.Driver.Tap(self, 1900, 500)

        def SetBGColor(self, type: str = "Standard", ColorNum: int = 1, R=255, G=255, B=255, A=255):
            """設置字體顏色"""
            action = "設置字體顏色"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonColorBg, By.ID)

            if type == "Standard":
                self.Driver.ElementClick(action,
                                         ElementParam._Id_buttonStandard, By.ID)
                self.Driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.GridView/android.view.View['+str(ColorNum)+']').click()
            elif type == "Advanced":
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonAdvanced))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_buttonAdvanced).click()
                for i in range(4):
                    pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + \
                        "[" + str(i+1) + "]" + \
                        "/android.view.ViewGroup/android.widget.EditText"
                    pattern = self.Driver.find_element_by_xpath(
                        pattern_xpath)
                    if str(i+1) == "1":
                        pattern.click()
                        context1 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context1)
                        pattern.send_keys(R)
                        self.Driver.press_keycode('66')
                    elif str(i+1) == "2":
                        pattern.click()
                        context2 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context2)
                        pattern.send_keys(G)
                        self.Driver.press_keycode('66')
                    elif str(i+1) == "3":
                        pattern.click()
                        context3 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context3)
                        pattern.send_keys(B)
                        self.Driver.press_keycode('66')
                    else:
                        pattern.click()
                        context4 = pattern.get_attribute('text')
                        ToolBar.Text.EditTextClear(self, context4)
                        pattern.send_keys(A)
                        self.Driver.press_keycode('66')
                self.Driver.Tap(self, 1900, 500)

        def Superscript(self):
            """設置上標"""
            action = "設置上標"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkUpscript, By.ID)

        def Subscript(self):
            """設置下標"""
            action = "設置下標"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkDownscript, By.ID)

        def AlignLeft(self):
            """設置靠左對齊"""
            action = "設置靠左對齊"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkAlignLeft, By.ID)

        def AlignRight(self):
            """設置靠右對齊"""
            action = "設置靠右對齊"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkAlignRight, By.ID)

        def Center(self):  # 置中
            """設置靠右對齊"""
            action = "設置靠右對齊"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkAlignCenter, By.ID)

        def List(self):
            """設置條列項目"""
            action = "設置條列項目"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_checkBulleted, By.ID)

        def AddIdent(self):
            """設置縮排"""
            action = "設置縮排"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonIncIndent, By.ID)

        def ReduceIdent(self):
            """設置條列項目"""
            action = "設置條列項目"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(action,
                                     ElementParam._Id_buttonDecIndent, By.ID)

    def BackStep():
        pass

    def NextStep():
        pass


class FloatBar(FuncBase):
    def CreateNewPage(self):
        """新增頁面"""
        action = "新增頁面"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_btnPageAdd, By.ID)

    def Paste(self):
        """資料夾"""
        action = "貼上"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_btnPaste, By.ID)

    def NextPage(self):
        """下一頁"""
        action = "下一頁"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_btnPageNext, By.ID)

    def LastPage(self):
        """上一頁"""
        action = "上一頁"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_btnPagePrev, By.ID)


class Background(FuncBase):
    def OpenBackgroundManagement(self):
        """開啟背景圖管理介面"""
        action = "開啟背景圖管理介面"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_btnBackground, By.ID)

    def SelectBackgroundMenu(self, menu: c_ElementParam):
        """選擇背景圖"""
        action = "選擇背景圖"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, menu, By.ID)

    class FollowMe:
        pass

    class PureColor:
        def ChangeByColor(self, index):
            color_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(
                index)+"]"
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, color_xpath))
            )
            self.Driver.find_element_by_xpath(color_xpath).click()

        def OpenMoreColor(self):
            self.ChangeByColor(self, 24)

        # color_num: 1~17, 1 is blue, 2 is cyan...
        def ChangeColorByStandard(self, color_num):
            """開啟背景圖管理介面"""
            action = "開啟背景圖管理介面"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(
                action, ElementParam._Id_buttonStandard, By.ID)

        def ChangeColorByAdvanced(self, R, G, B, A):
            """開啟背景圖管理介面"""
            action = "開啟背景圖管理介面"
            self.Log.AddCaseLog(action)
            self.Driver.ElementClick(
                action, ElementParam._Id_buttonAdvanced, By.ID)

            for i in range(4):
                pattern_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup" + \
                    "[" + str(i+1) + "]" + \
                    "/android.view.ViewGroup/android.widget.EditText"
                pattern = self.Driver.find_element_by_xpath(pattern_xpath)
                if str(i+1) == "1":
                    pattern.click()
                    context1 = pattern.get_attribute('text')
                    ToolBar.Text.EditTextClear(self, context1)
                    pattern.send_keys(R)
                    self.Driver.press_keycode('66')
                elif str(i+1) == "2":
                    pattern.click()
                    context2 = pattern.get_attribute('text')
                    ToolBar.Text.EditTextClear(self, context2)
                    pattern.send_keys(G)
                    self.Driver.press_keycode('66')
                elif str(i+1) == "3":
                    pattern.click()
                    context3 = pattern.get_attribute('text')
                    ToolBar.Text.EditTextClear(self, context3)
                    pattern.send_keys(B)
                    self.Driver.press_keycode('66')
                else:
                    pattern.click()
                    context4 = pattern.get_attribute('text')
                    ToolBar.Text.EditTextClear(self, context4)
                    pattern.send_keys(A)
                    self.Driver.press_keycode('66')

    class Preset:
        def ChangeByPreinstalled(self, index, mode="this page"):
            bg_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.GridView/android.widget.ImageView["+str(
                index)+"]"
            WebDriverWait(self.Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, bg_xpath))
            )
            self.Driver.find_element_by_xpath(bg_xpath).click()
            if mode == "this page":
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonNeutral))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_buttonNeutral).click()
            if mode == "all pages":
                WebDriverWait(self.Driver, 10).until(
                    EC.presence_of_element_located(
                        (By.ID, ElementParam._Id_buttonCancel))
                )
                self.Driver.find_element_by_id(
                    ElementParam._Id_buttonCancel).click()

    class MyViewBoardOriginal:
        def ChangeByOriginals(self, index, mode="this page"):
            Background.Preset.ChangeByPreinstalled(self, index, mode)

    class Saved:
        def ChangeBySaved(self, index, mode="this page"):
            pass

    class Customize:
        pass

    def DeleteSavedBackgound(self, index):
        pass

    def AddBackgroundImg(self):
        pass

    def ClickGridBtn(self):
        """啟用浮水印"""
        action = "啟用浮水印"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(action, ElementParam._Id_checkGridLine, By.ID)

    def ClickWatermarkBtn(self):
        """啟用浮水印"""
        action = "啟用浮水印"
        self.Log.AddCaseLog(action)
        self.Driver.ElementClick(
            action, ElementParam._Id_checkWaterMark, By.ID)
