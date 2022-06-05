import datetime
import time
import unittest
from Library import LibData
from Library.LibWebDriver import LibWebDriver
from Params.SystemParams import SysParams
from IntegratedTest import AdornerTest
# , BackgroundTestCase, EraserTestCase,
#                        HighlighterTestCase, ImagesearchCase, ImportTestcase,
#                        LoginAndActivateTestCase, MarkerTestCase, ShapeTestCase,
#                        StickyNoteTestCase, TextTestCase, TierTestCase)


class NoActivateTestCase(unittest.TestCase):

    # LibData.LibData.DynamicExecClassFunction(
    #     AdornerTestCase.AdornerTestCase.Pen.Case01_OpenAdornerMenu())

    p = AdornerTest.AdornerTest()
    # p.PenCase.Case01_OpenAdornerMenu()
    p.PenCase.ExecCase()

    def setUp(self):
        self.Driver = LibWebDriver(isActivate=False)

    def test_TierCase_NoActivate(self):
        TierTestCase.NoActivateCase(self)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Driver = LibWebDriver(isActivate=True)

    def test_Activate(self):
        LoginAndActivateTestCase.Case1(self, 'david.wz.jie@viewsonic.com')

    def test_NormalLogin(self):
        LoginAndActivateTestCase.Case2(
            self, SysParams._Email, SysParams._Password)

    def test_MarkerCase1_1(self):
        MarkerTestCase.Case1_1(self)

    def test_MarkerCase1_2(self):
        MarkerTestCase.Case1_2(self)

    def test_MarkerCase1_3(self):
        MarkerTestCase.Case1_3(self)

    def test_HighlighterCase1(self):
        HighlighterTestCase.Case1(self)

    def test_EraserCase1to1(self):
        EraserTestCase.Case1to1(self)

    def test_EraserCase1to2(self):
        EraserTestCase.Case1to2(self)

    def test_EraserCase1to3(self):
        EraserTestCase.Case1to3(self)

    def test_EraserCase2to1(self):
        EraserTestCase.Case2to1(self)

    def test_EraserCase2to2(self):
        EraserTestCase.Case2to2(self)

    def test_EraserCase2to3(self):
        EraserTestCase.Case2to3(self)

    def test_EraserCase3(self):
        EraserTestCase.Case3(self)

    def test_TextTestCase1(self):
        TextTestCase.testCase1(self)

    def test_TextTestCase2(self):
        TextTestCase.testCase2(self)

    def test_TextTestCase3(self):
        TextTestCase.testCase3(self)

    def test_StickyNote_pen(self):
        StickyNoteTestCase.TestStickyNote_Pen(self)

    def test_StickyNote_text(self):
        StickyNoteTestCase.TestStickyNote_Text(self)

    def test_Shapes(self):
        ShapeTestCase.run_shapes(self, 1, 19, 1)  # 19

    def test_3DShapes(self):
        ShapeTestCase.run_shapes(self, 1, 6, 2)  # 6

    def test_Lines(self):
        ShapeTestCase.run_shapes(self, 1, 13, 3)  # 13

    def test_BackgroundCase1_1(self):
        BackgroundTestCase.Case1_1(self)

    def test_BackgroundCase1_2(self):
        BackgroundTestCase.Case1_2(self)

    def test_BackgroundCase1_3(self):
        BackgroundTestCase.Case1_3(self)

    def test_BackgroundCase2_1(self):
        BackgroundTestCase.Case2_1(self)

    def test_BackgroundCase2_2(self):
        BackgroundTestCase.Case2_2(self)

    def test_BackgroundCase3_1(self):
        BackgroundTestCase.Case3_1(self)

    def test_BackgroundCase3_2(self):
        BackgroundTestCase.Case3_2(self)

    def test_BackgroundCase3_3(self):
        BackgroundTestCase.Case3_3(self)

    def test_AdornerCase1_1(self):
        AdornerTest.Case1_1(self)

    def test_AdornerCase1_2(self):
        AdornerTest.Case1_2(self)

    def test_AdornerCase1_3(self):
        AdornerTest.Case1_3(self)

    def test_AdornerCase1_4(self):
        AdornerTest.Case1_4(self)

    def test_AdornerCase1_5(self):
        AdornerTest.Case1_5(self)

    def test_AdornerCase1_6(self):
        AdornerTest.Case1_6(self)

    def test_AdornerCase1_7(self):
        AdornerTest.Case1_7(self)

    def test_AdornerCase1_8(self):
        AdornerTest.Case1_8(self)

    def test_AdornerCase1_9(self):
        AdornerTest.Case1_9(self)

    def test_AdornerCase1_10(self):
        AdornerTest.Case1_10(self)

    def test_AdornerCase1_11(self):
        AdornerTest.Case1_11(self)

    def test_AdornerCase1_12(self):
        AdornerTest.Case1_12(self)

    def test_AdornerCase1_13(self):
        AdornerTest.Case1_13(self)

    def test_AdornerCase2_1(self):
        AdornerTest.Case2_1(self)

    def test_AdornerCase2_2(self):
        AdornerTest.Case2_2(self)

    def test_AdornerCase2_3(self):
        AdornerTest.Case2_3(self)

    def test_AdornerCase2_4(self):
        AdornerTest.Case2_4(self)

    def test_AdornerCase2_5(self):
        AdornerTest.Case2_5(self)

    def test_AdornerCase2_6(self):
        AdornerTest.Case2_6(self)

    def test_AdornerCase2_7(self):
        AdornerTest.Case2_7(self)

    def test_AdornerCase2_8(self):
        AdornerTest.Case2_8(self)

    def test_AdornerCase2_9(self):
        AdornerTest.Case2_9(self)

    def test_AdornerCase2_10(self):
        AdornerTest.Case2_10(self)

    def test_AdornerCase2_11(self):
        AdornerTest.Case2_11(self)

    def test_AdornerCase2_12(self):
        AdornerTest.Case2_12(self)

    def test_AdornerCase2_13(self):
        AdornerTest.Case2_13(self)

    def test_AdornerCase2_14(self):
        AdornerTest.Case2_14(self)

    def test_AdornerCase3_1(self):
        AdornerTest.Case3_1(self)

    def test_AdornerCase3_2(self):
        AdornerTest.Case3_2(self)

    def test_AdornerCase3_3(self):
        AdornerTest.Case3_3(self)

    def test_AdornerCase3_4(self):
        AdornerTest.Case3_4(self)

    def test_AdornerCase3_5(self):
        AdornerTest.Case3_5(self)

    def test_AdornerCase3_6(self):
        AdornerTest.Case3_6(self)

    def test_AdornerCase3_7(self):
        AdornerTest.Case3_7(self)

    def test_AdornerCase3_8(self):
        AdornerTest.Case3_8(self)

    def test_AdornerCase3_9(self):
        AdornerTest.Case3_9(self)

    def test_AdornerCase3_10(self):
        AdornerTest.Case3_10(self)

    def test_AdornerCase3_11(self):
        AdornerTest.Case3_11(self)

    def test_AdornerCase3_12(self):
        AdornerTest.Case3_12(self)

    def test_AdornerCase3_13(self):
        AdornerTest.Case3_13(self)

    def test_AdornerCase3_14(self):
        AdornerTest.Case3_14(self)

    def test_AdornerCase4_1(self):
        AdornerTest.Case4_1(self)

    def test_AdornerCase4_2(self):
        AdornerTest.Case4_2(self)

    def test_AdornerCase4_3(self):
        AdornerTest.Case4_3(self)

    def test_AdornerCase4_4(self):
        AdornerTest.Case4_4(self)

    def test_AdornerCase4_5(self):
        AdornerTest.Case4_5(self)

    def test_AdornerCase4_6(self):
        AdornerTest.Case4_6(self)

    def test_AdornerCase4_7(self):
        AdornerTest.Case4_7(self)

    def test_AdornerCase4_8(self):
        AdornerTest.Case4_8(self)

    def test_AdornerCase4_9(self):
        AdornerTest.Case4_9(self)

    def test_AdornerCase4_10(self):
        AdornerTest.Case4_10(self)

    def test_AdornerCase4_11(self):
        AdornerTest.Case4_11(self)

    def test_AdornerCase4_12(self):
        AdornerTest.Case4_12(self)

    def test_AdornerCase4_13(self):
        AdornerTest.Case4_13(self)

    def test_AdornerCase5_1(self):
        AdornerTest.Case5_1(self)

    def test_AdornerCase5_2(self):
        AdornerTest.Case5_2(self)

    def test_AdornerCase5_3(self):
        AdornerTest.Case5_3(self)

    def test_AdornerCase5_4(self):
        AdornerTest.Case5_4(self)

    def test_AdornerCase5_5(self):
        AdornerTest.Case5_5(self)

    def test_AdornerCase5_6(self):
        AdornerTest.Case5_6(self)

    def test_AdornerCase5_7(self):
        AdornerTest.Case5_7(self)

    def test_AdornerCase5_8(self):
        AdornerTest.Case5_8(self)

    def test_AdornerCase5_9(self):
        AdornerTest.Case5_9(self)

    def test_AdornerCase5_10(self):
        AdornerTest.Case5_10(self)

    def test_TierCase_Preload(self):
        TierTestCase.TierPreloadCase(self)

    def test_TierCase_Standard(self):
        TierTestCase.TierStandardCase(self)

    def test_TierCase_Primium(self):
        TierTestCase.TierPremiumCase(self)

    def test_TierCase_Entity(self):
        TierTestCase.TierEntityCase(self)

    def test_ImageSearchCase1(self):
        ImagesearchCase.ImportimagetypeCase(self, "png")

    def test_ImageSearchCase2(self):
        ImagesearchCase.ImportimagetypeCase(self, "svg")

    def test_ImageSearchCase3(self):
        ImagesearchCase.ImportimagetypeCase(self, "gif")

    def test_LocalStorage(self):
        ImportTestcase.testImport(self, "Local")

    def test_GoogleDrive(self):
        ImportTestcase.testImport(self, "GoogleDrive")

    def test_OneDrive(self):
        ImportTestcase.testImport(self, "OneDrive")

    def test_OneDriveForBusiness(self):
        ImportTestcase.testImport(self, "OneDriveForBusiness")

    def test_DropBox(self):
        ImportTestcase.testImport(self, "DropBox")

    def test_Box(self):
        ImportTestcase.testImport(self, "Box")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    # ogCheck.logAmountCheck()
    # logCheck.excelAmountCheck()

    suite_login_and_activate = unittest.TestSuite()
    suite_login_and_activate.addTest(MyTestCase("test_Activate"))
    suite_login_and_activate.addTest(MyTestCase("test_NormalLogin"))

    suite_pen = unittest.TestSuite()
    suite_pen.addTest(MyTestCase("test_MarkerCase1_1"))
    suite_pen.addTest(MyTestCase("test_MarkerCase1_2"))
    suite_pen.addTest(MyTestCase("test_MarkerCase1_3"))
    suite_pen.addTest(MyTestCase("test_HighlighterCase1"))

    suite_eraser = unittest.TestSuite()
    suite_eraser.addTest(MyTestCase("test_EraserCase1to1"))
    suite_eraser.addTest(MyTestCase("test_EraserCase1to2"))
    suite_eraser.addTest(MyTestCase("test_EraserCase1to3"))
    suite_eraser.addTest(MyTestCase("test_EraserCase2to1"))
    suite_eraser.addTest(MyTestCase("test_EraserCase2to2"))
    suite_eraser.addTest(MyTestCase("test_EraserCase2to3"))
    suite_eraser.addTest(MyTestCase("test_EraserCase3"))

    suite_text = unittest.TestSuite()
    suite_text.addTest(MyTestCase("test_TextTestCase1"))
    # suite_text.addTest(MyTestCase("test_TextTestCase2"))
    # suite_text.addTest(MyTestCase("test_TextTestCase3"))

    suite_StickyNote = unittest.TestSuite()
    suite_StickyNote.addTest(MyTestCase("test_StickyNote_pen"))
    suite_StickyNote.addTest(MyTestCase("test_StickyNote_text"))

    suite_Shapes = unittest.TestSuite()
    suite_Shapes.addTest(MyTestCase("test_Shapes"))
    # suite_Shapes.addTest(MyTestCase("test_3DShapes"))
    # suite_Shapes.addTest(MyTestCase("test_Lines"))

    suite_background = unittest.TestSuite()
    suite_background.addTest(MyTestCase("test_BackgroundCase1_1"))
    suite_background.addTest(MyTestCase("test_BackgroundCase1_2"))
    suite_background.addTest(MyTestCase("test_BackgroundCase1_3"))
    suite_background.addTest(MyTestCase("test_BackgroundCase2_1"))
    suite_background.addTest(MyTestCase("test_BackgroundCase2_2"))
    suite_background.addTest(MyTestCase("test_BackgroundCase3_1"))
    suite_background.addTest(MyTestCase("test_BackgroundCase3_2"))
    suite_background.addTest(MyTestCase("test_BackgroundCase3_3"))

    suite_Adorner = unittest.TestSuite()
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_1"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_2"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_3"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_4"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_5"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_6"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_7"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_8"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_9"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_10"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_11"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_12"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase1_13"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_1"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_2"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_3"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_4"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_5"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_6"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_7"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_8"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_9"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_10"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_11"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_12"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_13"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase2_14"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_1"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_2"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_3"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_4"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_5"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_6"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_7"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_8"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_9"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_10"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_11"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_12"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_13"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase3_14"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_1"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_2"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_3"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_4"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_5"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_6"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_7"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_8"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_9"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_10"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_11"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_12"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase4_13"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_1"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_2"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_3"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_4"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_5"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_6"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_7"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_8"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_9"))
    suite_Adorner.addTest(MyTestCase("test_AdornerCase5_10"))

    suite_Tier = unittest.TestSuite()
    suite_Tier.addTest(NoActivateTestCase("test_TierCase_NoActivate"))
    suite_Tier.addTest(MyTestCase("test_Activate"))
    suite_Tier.addTest(MyTestCase("test_TierCase_Preload"))
    suite_Tier.addTest(MyTestCase("test_TierCase_Standard"))
    suite_Tier.addTest(MyTestCase("test_TierCase_Primium"))
    suite_Tier.addTest(MyTestCase("test_TierCase_Entity"))

    suite_ImageSearch = unittest.TestSuite()
    suite_ImageSearch.addTest(MyTestCase("test_ImageSearchCase1"))
    suite_ImageSearch.addTest(MyTestCase("test_ImageSearchCase2"))
    suite_ImageSearch.addTest(MyTestCase("test_ImageSearchCase3"))

    suite_Import = unittest.TestSuite()
    # suite_Import.addTest(MyTestCase("test_LocalStorage"))
    suite_Import.addTest(MyTestCase("test_GoogleDrive"))
    suite_Import.addTest(MyTestCase("test_OneDrive"))
    suite_Import.addTest(MyTestCase("test_OneDriveForBusiness"))
    suite_Import.addTest(MyTestCase("test_DropBox"))
    suite_Import.addTest(MyTestCase("test_Box"))

    runner = unittest.TextTestRunner(verbosity=2)

    # All_log.logger.error("PenTestCase: " + str(runner.run(suite_pen)))
    # All_log.logger.error("ShapesTestCase: " + str(runner.run(suite_Shapes)))
    # All_log.logger.error("EraserTestCase: " + str(runner.run(suite_eraser)))
    # All_log.logger.error("StickyNoteTestCase: " + str(runner.run(suite_StickyNote)))
    # All_log.logger.error("BackgroundTestCase: " + str(runner.run(suite_background)))
    # All_log.logger.error("AdornerTestCase: " + str(runner.run(suite_Adorner)))
    # All_log.logger.error("ImageSearchTestCase: " + str(runner.run(suite_ImageSearch)))
    # All_log.logger.error("ImportTestCase: " + str(runner.run(suite_Import)))
    # All_log.logger.error("TierTestCase: " + str(runner.run(suite_Tier)))
