import time
import unittest
from IntegratedTest import SIT_Adorner
from Library.LibWebDriver import LibWebDriver
from Params.SystemParams import SysParams

if __name__ == '__main__':

    adorner = SIT_Adorner.AdornerTest()
    adorner.PenCase.ExecCase()
    ###
    suite_Import = unittest.TestSuite()
    # suite_Import.addTest(MyTestCase("test_LocalStorage"))
    # suite_Import.addTest(SIT_Adorner.AdornerTest.Pen("ExecCase"))
    suite_Import.addTest(MyTestCase("test_OneDrive"))
    suite_Import.addTest(MyTestCase("test_OneDriveForBusiness"))
    suite_Import.addTest(MyTestCase("test_DropBox"))
    suite_Import.addTest(MyTestCase("test_Box"))

    runner = unittest.TextTestRunner(verbosity=2)
