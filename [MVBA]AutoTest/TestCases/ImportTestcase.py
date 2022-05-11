
import time
import datetime
from UnitFunction import LoginAndActive, MagicBox, FloatBar, ToolBar, Screenshot, Compare, log
import sys
import os
sys.path.append(os.getcwd())

Import_log = log.Logger(
    './Output/Logs/Import'+datetime.datetime.now().strftime(' %Y%m%d %H_%M_%S') + '.log', level='info')
types = ["video", "audio", "img"]


def testImport(self, locate="Local"):
    try:
        Import_log.logger.info("登入MVBA")
        LoginAndActive.NormalLogin(
            self, "aiden.test2222@gmail.com", "$Cd069798")
        Import_log.logger.info("讓子彈飛一會唷~~大概20秒")
        time.sleep(20)
        for type in types:
            for i in range(3):  # 3 files each type
                Import_log.logger.info("Click Pen icon")
                ToolBar.SelectPenBtn(self)
                Import_log.logger.info("Open MagicBox")
                MagicBox.OpenMagicBox(self)
                if locate == "GoogleDrive":
                    Import_log.logger.info("Click GoogleDrive icon")
                    MagicBox.SelectGoogleDrive(self)
                elif locate == "OneDrive":
                    Import_log.logger.info("Click OneDrive icon")
                    MagicBox.SelectOneDrive(self)
                elif locate == "OneDriveForBusiness":
                    Import_log.logger.info("Click OneDriveForBusiness icon")
                    MagicBox.SelectOneDriveForBusiness(self)
                elif locate == "DropBox":
                    Import_log.logger.info("Click DropBox icon")
                    MagicBox.SelectDropBox(self)
                elif locate == "Box":
                    Import_log.logger.info("Click Box icon")
                    MagicBox.SelectBox(self)
                else:
                    Import_log.logger.info("Click Storage icon")
                    MagicBox.SelectStorage(self)
                Import_log.logger.info("Click " + type + " type icon")
                MagicBox.ChooseFileType(self, type)
                time.sleep(3)
                n = 0
                while self.driver.find_element_by_id("com.viewsonic.droid:id/titleTextView").get_attribute("text") != "Auto-test":
                    n += 1
                    Import_log.logger.info("打開第"+str(n)+"層文件夾")
                    MagicBox.SelectFile(self, 1)
                while self.driver.find_element_by_id("com.viewsonic.droid:id/btnLasso").get_attribute("selected") != "true":
                    Import_log.logger.info("Import " + type + " file")
                    MagicBox.SelectFile(self, i+1)
                    time.sleep(10)
                Import_log.logger.info("Close MagicBox")
                MagicBox.CloseMagicBox(self)
            screenshot_path = "./TestCases/Screenshots/MediaFiles/" + locate + "/" + type + '.png'
            Import_log.logger.info("擷取畫布")
            Screenshot.screenshotCanvas(self, screenshot_path)
            # compare imgs
            sample = "./TestCases/Samples/MediaFiles/" + locate + "/" + type + '.png'
            tar_img = "./TestCases/Screenshots/MediaFiles/" + locate + "/" + type + '.png'
            Import_log.logger.info("比對畫布")
            if not Compare.isImgEqual(sample, tar_img):
                Import_log.logger.info(
                    "Import " + type + " from " + str(locate) + " fail")
            else:
                Import_log.logger.info(
                    "Import " + type + " from " + str(locate) + " pass")
            if not type == "img":
                Import_log.logger.info("換頁唷!")
                FloatBar.NewPage(self)
        Import_log.logger.info("ImportCase for " + str(locate) + " Finish")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        Import_log.logger.error("系統運行錯誤，請重試", exc_info=True)
        Import_log.logger.info("Finish")
