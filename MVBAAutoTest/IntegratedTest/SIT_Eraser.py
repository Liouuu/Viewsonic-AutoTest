from lib2to3.pgen2 import driver
import ElementParams
from Library import Compare
from Library.LibLogHelper import LogPackage
from UnitBase import Canvas, FloatBar, ToolBar
from . import Canva
import time
from Library.LibWebDriver import LibWebDriver as LWD
from Params.SampleFileParam import *


def OpenOLF(self):  # Open the test file
    FileManagement.CloseFileManagement(self)
    FileManagement.OpenFileManagement(self)
    FileManagement.ChooseOpenFile(self)
    FileManagement.SelectFile(self, 4)
    FileManagement.SelectFile(self, 3)
    FileManagement.SelectFile(self, 3)
    FileManagement.SelectFile(self, 3)
    time.sleep(8)


class EraserTest:

    def __init__(self, driver: LWD = LWD.default(True, LogPackage("Adorner", srcFile="Adorner_Pen"))):
        self.Driver = driver

    def Case1_xxx(self):
        ToolBar.Folder.OpenFileManagement()
        OpenOLF(self)
        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ChooseRegularEraser()
        ToolBar.Eraser.SetEraserSize(40)
        Canvas.CloseMenu()
        T_list = [[60, 218], [326, 202]]
        E_list = [[431, 171], [661, 159]]
        S_list = [[1026, 187], [894, 159], [882, 268],
                  [1049, 408], [1034, 482], [847, 466]]
        T2_list = [[1166, 179], [1582, 148]]
        self.Driver.Swipe(self, T_list, 1500)
        self.Driver.Swipe(self, E_list, 1500)
        self.Driver.Swipe(self, S_list, 1500)
        self.Driver.Swipe(self, T2_list, 1500)
        LOCK_list = [[377, 692], [1718, 707]]
        self.Driver.Swipe(self, LOCK_list, 1500)
        self.Driver.ScreenshotAndCompare(
            SamplePicParam.EraserCase1, ElementParams._XPath_Canvas, By.XPATH)

    def Case2_yyy(self):
        OpenOLF(self)

        FloatBar.NextPage()
        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ChooseRegularEraser()
        ToolBar.Eraser.SetEraserSize(40)
        Canvas.CloseMenu()

        count = 0
        page = 2
        # For Case 1-2
        regular_eraser_1to2 = {
            "Movepage2_list1": [[309, 321], [1795, 305]],
            "Movepage2_list2": [[263, 789], [1878, 797]],
            "Movepage3_list1": [[229, 237], [1710, 249]],
            "Movepage3_list2": [[354, 726], [1505, 713]],
            "Movepage4_list1": [[467, 330], [1707, 342]],
            "Movepage4_list2": [[296, 760], [1741, 781]],
            "Movepage5_list1": [[330, 363], [1690, 380]],
            "Movepage5_list2": [[330, 810], [1557, 818]],
            "Movepage6_list1": [[346, 355], [1736, 367]],
            "Movepage6_list2": [[309, 781], [1757, 781]],
            "Movepage7_list1": [[127, 300], [1171, 280]],
            "Movepage7_list2": [[584, 657], [1705, 657]],
            "Movepage8_list1": [[303, 319], [1793, 288]],
            "Movepage8_list2": [[664, 691], [1517, 680]],
            "Movepage9_list1": [[96, 472], [1697, 453]],
        }
        for i in regular_eraser_1to2:
            Eraser.Swipe(self, regular_eraser_1to2[i], 1500)
            time.sleep(2)
            count += 1
            if count % 2 == 0:
                self.Driver.ScreenshotAndCompare(
                    srcPic, ElementParams._XPath_Canvas, By.XPATH)
                FloatBar.NextPage(self)
                page += 1
                time.sleep(1)
            self.Driver.ScreenshotAndCompare(
                srcPic, ElementParams._XPath_Canvas, By.XPATH)

    def Case3_zzz(self):
        OpenOLF(self)
        FloatBar.NextPage()
        ToolBar.Eraser.OpenEraserMenu()

        ToolBar.Eraser.ChooseRegularEraser()
        ToolBar.Eraser.SetEraserSize(40)
        Canvas.CloseMenu()

        # For Case 1-3
        regular_eraser_1to3 = {
            2: [[603, 296], [1137, 300], [438, 726], [1486, 714]],
            3: [[561, 288], [1194, 323], [549, 707], [1198, 722]],
            4: [[703, 319], [1313, 326], [403, 722], [1417, 695]],
            5: [[601, 355], [1411, 380], [547, 789], [1302, 797]],
            6: [[584, 307], [1321, 300], [611, 699], [1386, 730]],
            7: [[357, 288], [887, 284], [925, 657], [1475, 664]],
            8: [[564, 311], [1597, 300], [1110, 687], [1475, 664]],  # [1475,664]除錯用
            9: [[303, 472], [707, 465], [1083, 476], [1482, 472]],
        }

        for page in regular_eraser_1to3:
            Canva.Tap(
                self, regular_eraser_1to3[page][0][0], regular_eraser_1to3[page][0][1])
            time.sleep(1)
            Canva.Tap(
                self, regular_eraser_1to3[page][1][0], regular_eraser_1to3[page][1][1])
            time.sleep(1)
            Canva.Tap(
                self, regular_eraser_1to3[page][2][0], regular_eraser_1to3[page][2][1])
            time.sleep(1)
            Canva.Tap(
                self, regular_eraser_1to3[page][3][0], regular_eraser_1to3[page][3][1])
            time.sleep(1)

            self.Driver.ScreenshotAndCompare()
            FloatBar.NextPage(self)
            time.sleep(1)

    def Case4_xxx(self):
        OpenOLF(self)

        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ChooseCircleEraser()
        # For case 2-1
        circle_eraser_2to1 = {
            1: [[756, 96], [768, 526], [1133, 526], [1083, 96], [841, 100]],
            2: [[979, 138], [983, 518], [1286, 500], [1317, 127], [1029, 111]],
            3: [[380, 580], [360, 850], [726, 864], [695, 530], [370, 553]],
            4: [[215, 515], [200, 887], [1025, 956], [956, 538], [357, 511]],
            5: [[215, 515], [200, 887], [1025, 956], [956, 538], [357, 511]],
            6: [[349, 100], [353, 495], [829, 492], [814, 115], [461, 108]],
            7: [[687, 154], [672, 438], [1160, 330], [891, 115]],
            8: [[1382, 119], [1847, 146], [1816, 500], [1359, 484], [1340, 242]],
            9: [[499, 296], [922, 292], [906, 700], [530, 676], [507, 411]]
        }
        for page in circle_eraser_2to1:
            Canva.Swipe(self, circle_eraser_2to1[page])
            self.Driver.ScreenshotAndCompare()
            FloatBar.NextPage(self)
            time.sleep(1)

    def Case5_ZZZ(self):
        OpenOLF(self)
        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ChooseCircleEraser()
        # For case 2-2, 1~8 means page 1 ~ page 8
        circle_eraser_2to2 = {
            1: [[357, 538], [349, 845], [710, 852], [707, 538], [369, 534]],
            2: [[420, 173], [409, 505], [817, 505], [810, 166], [416, 147]],
            3: [[1006, 559], [1022, 894], [1376, 871], [1369, 532], [1080, 544]],
            4: [[1022, 339], [628, 66], [447, 517], [921, 467]],
            5: [[204, 131], [247, 605], [883, 594], [891, 135], [266, 123]],
            6: [[251, 517], [254, 894], [1033, 867], [1018, 486], [339, 490]],
            7: [[166, 166], [170, 455], [632, 443], [605, 112], [154, 104]],
            8: [[204, 131], [247, 605], [883, 594], [891, 135], [266, 123]]}
        for page in circle_eraser_2to2:
            Canva.Swipe(self, circle_eraser_2to2[page])
            self.Driver.ScreenshotAndCompare()
            FloatBar.NextPage(self)

    def Case6_yyy(self):
        OpenOLF(self)
        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ChooseCircleEraser()
        # For case 2-3
        circle_eraser_2to3 = [[30, 87], [30, 932],
                              [1876, 910], [1898, 127], [100, 105]]

        for i in range(8):
            Canva.Swipe(self, circle_eraser_2to3)

            self.Driver.ScreenshotAndCompare()
            FloatBar.NextPage(self)
            time.sleep(1)
        Canva.Swipe(self, circle_eraser_2to3)
        self.Driver.ScreenshotAndCompare()

    def Case7_xx(self):
        OpenOLF(self)
        for i in range(8):
            ToolBar.Eraser.OpenEraserMenu()
            ToolBar.Eraser.ClearCanvas()
            self.Driver.ScreenshotAndCompare()
            FloatBar.NextPage(self)

        ToolBar.Eraser.OpenEraserMenu()
        ToolBar.Eraser.ClearCanvas()
        self.Driver.ScreenshotAndCompare()
