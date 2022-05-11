from UnitFunction import Eraser, Canvas, FileManagement, FloatBar, Screenshot, Compare, log
import time
import datetime
import sys
import os
sys.path.append(os.getcwd())


Eraser_log = log.Logger(
    './Output/Logs/Eraser'+datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S') + '.log', level='info')
# For Case 1-1
T_list = [[60, 218], [326, 202]]
E_list = [[431, 171], [661, 159]]
S_list = [[1026, 187], [894, 159], [882, 268],
          [1049, 408], [1034, 482], [847, 466]]
T2_list = [[1166, 179], [1582, 148]]
LOCK_list = [[377, 692], [1718, 707]]

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

# For case 2-2, 1~8 means page 1 ~ page 8
circle_eraser_2to2 = {
    1: [[357, 538], [349, 845], [710, 852], [707, 538], [369, 534]],
    2: [[420, 173], [409, 505], [817, 505], [810, 166], [416, 147]],
    3: [[1006, 559], [1022, 894], [1376, 871], [1369, 532], [1080, 544]],
    4: [[1022, 339], [628, 66], [447, 517], [921, 467]],
    5: [[204, 131], [247, 605], [883, 594], [891, 135], [266, 123]],
    6: [[251, 517], [254, 894], [1033, 867], [1018, 486], [339, 490]],
    7: [[166, 166], [170, 455], [632, 443], [605, 112], [154, 104]],
    8: [[204, 131], [247, 605], [883, 594], [891, 135], [266, 123]],
}

# For case 2-3
circle_eraser_2to3 = [[30, 87], [30, 932],
                      [1876, 910], [1898, 127], [100, 105]]


def OpenOLF(self):  # Open the test file
    FileManagement.CloseFileManagement(self)
    FileManagement.OpenFileManagement(self)
    FileManagement.ChooseOpenFile(self)
    FileManagement.SelectFile(self, 4)
    FileManagement.SelectFile(self, 3)
    FileManagement.SelectFile(self, 3)
    FileManagement.SelectFile(self, 3)
    time.sleep(8)


def Case1to1(self):
    try:
        Eraser_log.logger.info(
            "Start Case1-1: move regular eraser over strokes")
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Regular Eraser")
        Eraser.ChooseRegularEraser(self)
        Eraser_log.logger.info("Adjust Eraser Size: value 40")
        Eraser.AdjustEraserSize(self, 40)
        Eraser_log.logger.info("Close Eraser Menu")
        Eraser.CloseEraserMenu(self)
        Eraser_log.logger.info("Erase Strokes")
        Eraser.Swipe(self, T_list, 1500)
        Eraser.Swipe(self, E_list, 1500)
        Eraser.Swipe(self, S_list, 1500)
        Eraser.Swipe(self, T2_list, 1500)
        Eraser_log.logger.info("Erase Locked Strokes")
        Eraser.Swipe(self, LOCK_list, 1500)
        Eraser_log.logger.info("Screenshot Canvas")
        Screenshot.screenshotCanvas(
            self, "./TestCases/Screenshots/Eraser/Eraser Case 1-1.png")
        Eraser_log.logger.info("Compare Canvas")
        if not Compare.isImgEqual("./TestCases/Samples/Eraser/Eraser Case 1-1.png", "./TestCases/Screenshots/Eraser/Eraser Case 1-1.png"):
            Eraser_log.logger.info("Eraser Case 1-1 Fail!")
        else:
            Eraser_log.logger.info("Eraser Case 1-1 Pass!")
        Eraser_log.logger.info("Case1-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case1to2(self):
    try:
        Eraser_log.logger.info(
            "Start Case1-2: move regular eraser over non-stroke objects")
        time.sleep(2)
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("to Next Page")
        FloatBar.NextPage(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Regular Eraser")
        Eraser.ChooseRegularEraser(self)
        Eraser_log.logger.info("Adjust Eraser Size: value 40")
        Eraser.AdjustEraserSize(self, 40)
        Eraser_log.logger.info("Close Eraser Menu")
        Eraser.CloseEraserMenu(self)
        count = 0
        page = 2
        for i in regular_eraser_1to2:
            Eraser_log.logger.info("Erase object: page " + str(page))
            Eraser.Swipe(self, regular_eraser_1to2[i], 1500)
            time.sleep(2)
            count += 1
            if count % 2 == 0:
                path = "./TestCases/Screenshots/Eraser/Eraser Case 1-2 page" + \
                    str(page) + ".png"
                sample_path = "./TestCases/Samples/Eraser/Eraser Case 1-2 page" + \
                    str(page) + ".png"
                Eraser_log.logger.info("Screenshot Canvas: page " + str(page))
                Screenshot.screenshotCanvas(self, path)
                Eraser_log.logger.info("Compare Canvas: page " + str(page))
                if not Compare.isImgEqual(sample_path, path):
                    Eraser_log.logger.info(
                        "Eraser Case 1-2 page " + str(page) + " Fail!")
                else:
                    Eraser_log.logger.info(
                        "Eraser Case 1-2 page " + str(page) + " Pass!")
                Eraser_log.logger.info("to Next Page")
                FloatBar.NextPage(self)
                page += 1
                time.sleep(1)
        path = "./TestCases/Screenshots/Eraser/Eraser Case 1-2 page" + \
            str(page) + ".png"
        sample_path = "./TestCases/Samples/Eraser/Eraser Case 1-2 page" + \
            str(page) + ".png"
        Eraser_log.logger.info("Screenshot Canvas: page " + str(page))
        Screenshot.screenshotCanvas(self, path)
        Eraser_log.logger.info("Compare Canvas: page " + str(page))
        if not Compare.isImgEqual(sample_path, path):
            Eraser_log.logger.info(
                "Eraser Case 1-2 page " + str(page) + " Fail!")
        else:
            Eraser_log.logger.info(
                "Eraser Case 1-2 page " + str(page) + " Pass!")
        Eraser_log.logger.info("Case1-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case1to3(self):
    try:
        Eraser_log.logger.info(
            "Start Case1-3: Use eraser to click non-stroke objects")
        time.sleep(2)
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("to Next Page")
        FloatBar.NextPage(self)
        Eraser_log.logger.info("Open Erase Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Regular Eraser")
        Eraser.ChooseRegularEraser(self)
        Eraser_log.logger.info("Adjust Eraser Size: value 40")
        Eraser.AdjustEraserSize(self, 40)
        Eraser_log.logger.info("Close Eraser Menu")
        Eraser.CloseEraserMenu(self)
        time.sleep(1)
        for page in regular_eraser_1to3:
            Eraser_log.logger.info("Erase object: page " + str(page))
            Canvas.Tap(
                self, regular_eraser_1to3[page][0][0], regular_eraser_1to3[page][0][1])
            time.sleep(1)
            Canvas.Tap(
                self, regular_eraser_1to3[page][1][0], regular_eraser_1to3[page][1][1])
            time.sleep(1)
            Canvas.Tap(
                self, regular_eraser_1to3[page][2][0], regular_eraser_1to3[page][2][1])
            time.sleep(1)
            Canvas.Tap(
                self, regular_eraser_1to3[page][3][0], regular_eraser_1to3[page][3][1])
            time.sleep(1)
            path = "./TestCases/Screenshots/Eraser/Eraser Case 1-3 page" + \
                str(page) + ".png"
            sample_path = "./TestCases/Samples/Eraser/Eraser Case 1-3 page" + \
                str(page) + ".png"
            Eraser_log.logger.info("Screenshot Canvas: page " + str(page))
            Screenshot.screenshotCanvas(self, path)
            Eraser_log.logger.info("Compare Canvas: page " + str(page))
            if not Compare.isImgEqual(sample_path, path):
                Eraser_log.logger.info(
                    "Eraser Case 1-3 page " + str(page) + " Fail!")
            else:
                Eraser_log.logger.info(
                    "Eraser Case 1-3 page " + str(page) + " Pass!")
            Eraser_log.logger.info("to Next Page")
            FloatBar.NextPage(self)
            time.sleep(1)
        Eraser_log.logger.info("Case1-3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case2to1(self):
    try:
        Eraser_log.logger.info(
            "Start Case2-1: Circle erase for single unlocked object")
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Circle Eraser")
        Eraser.ChooseCircleEraser(self)
        for page in circle_eraser_2to1:
            Eraser_log.logger.info("Erase object: page " + str(page))
            Canvas.Swipe(self, circle_eraser_2to1[page])
            path = "./TestCases/Screenshots/Eraser/Eraser Case 2-1 page" + \
                str(page) + ".png"
            sample_path = "./TestCases/Samples/Eraser/Eraser Case 2-1 page" + \
                str(page) + ".png"
            Eraser_log.logger.info("Screenshot Canvas: page " + str(page))
            Screenshot.screenshotCanvas(self, path)
            Eraser_log.logger.info("Compare Canvas: page " + str(page))
            if not Compare.isImgEqual(sample_path, path):
                Eraser_log.logger.info(
                    "Eraser Case 2-1 page " + str(page) + " Fail!")
            else:
                Eraser_log.logger.info(
                    "Eraser Case 2-1 page " + str(page) + " Pass!")
            Eraser_log.logger.info("to Next Page")
            FloatBar.NextPage(self)
            time.sleep(1)
        Eraser_log.logger.info("Case2-1 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case2to2(self):
    try:
        Eraser_log.logger.info(
            "Start Case2-2: Circle erase for single locked object")
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Circle Eraser")
        Eraser.ChooseCircleEraser(self)
        for page in circle_eraser_2to2:
            Eraser_log.logger.info("Erase object: page " + str(page))
            Canvas.Swipe(self, circle_eraser_2to2[page])
            path = "./TestCases/Screenshots/Eraser/Eraser Case 2-2 page" + \
                str(page) + ".png"
            sample_path = "./TestCases/Samples/Eraser/Eraser Case 2-2 page" + \
                str(page) + ".png"
            Eraser_log.logger.info("Screenshot Canvas: page " + str(page))
            Screenshot.screenshotCanvas(self, path)
            Eraser_log.logger.info("Compare Canvas: page " + str(page))
            if not Compare.isImgEqual(sample_path, path):
                Eraser_log.logger.info(
                    "Eraser Case 2-2 page " + str(page) + " Fail!")
            else:
                Eraser_log.logger.info(
                    "Eraser Case 2-2 page " + str(page) + " Pass!")
            Eraser_log.logger.info("to Next Page")
            FloatBar.NextPage(self)
            time.sleep(1)
        Eraser_log.logger.info("Case2-2 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case2to3(self):
    try:
        Eraser_log.logger.info(
            "Start Case2-3: Circle erase for multiple objects")
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Choose Circle Eraser")
        Eraser.ChooseCircleEraser(self)
        for i in range(8):
            Eraser_log.logger.info("Erase object: page " + str(i+1))
            Canvas.Swipe(self, circle_eraser_2to3)
            path = "./TestCases/Screenshots/Eraser/Eraser Case 2-3 page" + \
                str(i+1) + ".png"
            sample_path = "./TestCases/Samples/Eraser/Eraser Case 2-3 page" + \
                str(i+1) + ".png"
            Eraser_log.logger.info("Screenshot Canvas: page " + str(i+1))
            Screenshot.screenshotCanvas(self, path)
            Eraser_log.logger.info("Compare Canvas: page " + str(i+1))
            if not Compare.isImgEqual(sample_path, path):
                Eraser_log.logger.info(
                    "Eraser Case 2-3 page " + str(i+1) + " Fail!")
            else:
                Eraser_log.logger.info(
                    "Eraser Case 2-3 page " + str(i+1) + " Pass!")
            Eraser_log.logger.info("to Next Page")
            FloatBar.NextPage(self)
            time.sleep(1)
        Eraser_log.logger.info("Erase object: page " + str(9))
        Canvas.Swipe(self, circle_eraser_2to3)
        path = "./TestCases/Screenshots/Eraser/Eraser Case 2-3 page" + \
            str(9) + ".png"
        sample_path = "./TestCases/Samples/Eraser/Eraser Case 2-3 page" + \
            str(9) + ".png"
        Eraser_log.logger.info("Screenshot Canvas: page " + str(i+1))
        Screenshot.screenshotCanvas(self, path)
        Eraser_log.logger.info("Compare Canvas: page " + str(i+1))
        if not Compare.isImgEqual(sample_path, path):
            Eraser_log.logger.info("Eraser Case 2-3 page " + str(9) + " Fail!")
        else:
            Eraser_log.logger.info("Eraser Case 2-3 page " + str(9) + " Pass!")
        Eraser_log.logger.info("Case2-3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")


def Case3(self):
    try:
        Eraser_log.logger.info("Start Case3: Clear all")
        Eraser_log.logger.info("Open an OLF")
        OpenOLF(self)
        for i in range(8):
            Eraser_log.logger.info("Open Eraser Menu")
            Eraser.OpenEraserMenu(self)
            Eraser_log.logger.info("Clear Canvas")
            Eraser.ClearCanvas(self)
            path = "./TestCases/Screenshots/Eraser/Eraser Case 3 page" + \
                str(i+1) + ".png"
            sample_path = "./TestCases/Samples/Eraser/Eraser Case 3 page" + \
                str(i+1) + ".png"
            Eraser_log.logger.info("Screenshot Canvas: page " + str(i+1))
            Screenshot.screenshotCanvas(self, path)
            Eraser_log.logger.info("Compare Canvas: page " + str(i+1))
            if not Compare.isImgEqual(sample_path, path):
                Eraser_log.logger.info(
                    "Eraser Case 3 page " + str(i+1) + " Fail!")
            else:
                Eraser_log.logger.info(
                    "Eraser Case 3 page " + str(i+1) + " Pass!")
            Eraser_log.logger.info("to Next Page")
            FloatBar.NextPage(self)
        Eraser_log.logger.info("Open Eraser Menu")
        Eraser.OpenEraserMenu(self)
        Eraser_log.logger.info("Clear Canvas")
        Eraser.ClearCanvas(self)
        path = "./TestCases/Screenshots/Eraser/Eraser Case 3 page" + \
            str(9) + ".png"
        sample_path = "./TestCases/Samples/Eraser/Eraser Case 3 page" + \
            str(9) + ".png"
        Eraser_log.logger.info("Screenshot Canvas: page " + str(i+1))
        Screenshot.screenshotCanvas(self, path)
        Eraser_log.logger.info("Compare Canvas: page " + str(i+1))
        if not Compare.isImgEqual(sample_path, path):
            Eraser_log.logger.info("Eraser Case 3 page " + str(9) + " Fail!")
        else:
            Eraser_log.logger.info("Eraser Case 3 page " + str(9) + " Pass!")
        Eraser_log.logger.info("Case3 Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Eraser_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Eraser_log.logger.info("Finish")
