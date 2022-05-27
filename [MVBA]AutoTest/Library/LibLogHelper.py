from importlib.abc import InspectLoader
from itertools import count
from numpy import imag
from Library.LibData import LibData
from Library.LibExcel import LibExcel
from Params.SystemParams import SysPath, FileExt
from Params.LibParams import LogType
import datetime
from openpyxl.drawing.image import Image
import inspect


class CaseLogObj:
    """CaseLog欄位格式
    注:1. 更動欄位順序同時，也要調整Excel輸出格式的順序
       2. Step欄位永遠為空
    """

    def __init__(self, step: str = "", action: str = "", result: str = "", screenshot: Image = None):
        self.Time = datetime.datetime.now().strftime("%H:%M:%S")
        self.Step = ""
        self.Action = action
        self.Result = result
        self.Screenshot = screenshot


class UnitLogObj:
    """UnitLog欄位格式
    注:1. 更動欄位順序同時，也要調整Excel輸出格式的順序
    """

    def __init__(self, step: str = "", action: str = "", params: str = ""):
        self.Time = datetime.datetime.now().strftime("%H:%M:%S")
        self.Step = step
        self.Action = action
        self.Params = params
        self.Stack = str(inspect.stack())


class LogPackage:
    """Log包"""
# region Construct

    def __init__(self,  logName: str, srcFilePath=SysPath._SrcPath, srcFileName="", logPath=SysPath._ExcelPath,
                 logDict: dict = dict(), logType: LogType = LogType.excel):
        """建構函數
        :param str logName : 保存Log名稱 (注：檔名會自動加上現在時刻)
        :param str srcFilePath : 測試檔案路徑
        :param str srcFileName : 測試檔案名稱
        :param str logPath : 保存Log路徑
        :param dict caseLogDict : CaseLog資訊項目，Key值為SheetName,Value為List的CaseLogObj
        :param dict unitLogDict : UnitLog資訊項目，Key值為SheetName,Value為List的UnitLogObj
        :param str logType : 保存Log的形式(excel,txt...)
        """
        self.__LogPath = logPath
        self.__LogName = LibData.StringMerge(
            "-", logName, datetime.datetime.today().strftime("%Y-%m-%d %H：%M：%S"))
        self.__srcFilePath = srcFilePath
        self.__srcFileName = LibData.AddExtention(srcFileName, FileExt._xlsx)
        self.__LogDict = logDict
        self.__LogType = logType
# endregion

# region Public
    def CreateLog(self):
        """保存Log檔案
        """
        if self.__LogType == LogType.excel:
            self.__CreateExcelLog()
        else:
            pass

    def NewLogSheet(self, sheetName, logObj):
        """新增Log表
        :param str sheetName : 表名稱
        """
        logList = []
        logList.append(logObj)
        self.__LogDict[sheetName] = logList

    def AddCaseLog(self, sheetName, action, result: str = "", screenshot: Image = None):
        """插入Case步驟Log
        :param str sheetName : 表名稱
        :param str action : 執行的動作
        :param str  result : 執行結果
        :param Image screenshot : 圖片
        """
        caseLoglist = list(self.__LogDict[sheetName])
        caseLoglist.append(
            CaseLogObj(action=action, result=result, screenshot=screenshot))
        self.__LogDict[sheetName] = caseLoglist  # 確定下是否可以不用這句

    def AddUnitLog(self, sheetName, step, action, *params):
        """插入單元動作Log
        """
        # 這邊先做默認所有的Unit表叫Detail
        sheetName = LibData.AddExtention(sheetName, " Detail")
        unitLoglist = list(self.__LogDict[sheetName])
        if len(unitLoglist) > 1 and LibData.In(step, unitLoglist[len(unitLoglist)-1]):
            step = ""
        unitLoglist.append(UnitLogObj(step, action, str(*params)))
        self.__LogDict[sheetName] = unitLoglist  # 待確定是否可以不用這句
# endregion

# region Private
    def __CreateExcelLog(self):
        excel = LibExcel(self.__LogPath, self.__LogName)
        excel._AfterSetData = self.__ExcelImgAutoSizeFunc
        excel._Openfile(self.__srcFilePath, self.__srcFileName)
        excel._WriteDatas(self.__LogDict)
        excel._AutoSize()
        excel._SaveAs()

    def __ExcelAfterSetData(self, row, column, value):
        """自動調整Excel圖片欄位的長寬度"""
        row.height = value.height*3/4
        if value.width*3/20 > column.width:
            column.width = value.width*3/20

    def __ExcelImgAutoSizeFunc(self, row, column, value):
        if(value is Image):
            self.__ExcelAfterSetData(row, column, value)
        else:
            pass  # 之後設定：如果值為 什麼 的時候，也可以更改cell的顏色

# endregion
