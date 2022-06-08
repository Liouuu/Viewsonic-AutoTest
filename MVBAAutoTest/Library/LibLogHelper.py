from io import BytesIO
from Library.LibData import LibData
from Library.LibExcel import LibExcel
from Params.SystemParams import SysPath, FileExt
from Params.LibParams import LogType
import datetime
from PIL import Image
import inspect


class LogPackage:
    """Log包"""
# region Property

    @property
    def LogDict(self):
        if self.__LogDict == None:
            self.__LogDict = dict()
        return self.__LogDict

    @property
    def LogName(self):
        """Log名稱"""
        return LibData.Merge("-", self.__LogName, datetime.datetime.today().strftime("%Y-%m-%d %H：%M：%S"))

    @LogName.setter
    def LogName(self, val: str):
        self.__LogName = val

    @property
    def LogPath(self):
        """Log擺放資料夾位置"""
        return self.__DestPath

    @LogPath.setter
    def LogPath(self, val: str):
        self.__DestPath = LibData.Merge("/", SysPath.DestPath, val)

    @property
    def SrcPath(self):
        """來源測試檔案資料夾位置"""
        return self.__SrcPath

    @SrcPath.setter
    def SrcPath(self, val: str):
        self.__SrcPath = LibData.Merge("/", SysPath.SrcPath, val)

    @property
    def SrcFile(self):
        """來源測試檔案"""
        return self.__SrcFile

    @SrcFile.setter
    def SrcFile(self, val: str):
        self.__SrcFile = LibData.AddExtention(val, FileExt._xlsx)

    @property
    def SheetName(self):
        """表名"""
        return self.__curSheetName

    @SheetName.setter
    def SheetName(self, value: str): self.__curSheetName = value

    @property
    def SubSheetName(self): return LibData.AddExtention(
        self.SheetName, " Detail")
# endregion

# region Construct
    def __init__(self,  logName: str,
                 srcPath="SampleDoc", srcFile="", logPath="Excels", logType: LogType = LogType.excel):
        """建構函數
        :param str logName : 保存Log名稱 (注：檔名會自動加上現在時刻)
        :param str srcFilePath : 測試檔案路徑
        :param str srcFileName : 測試檔案名稱
        :param str logPath : 保存Log路徑
        :param str logType : 保存Log的形式(excel,txt...)
        """
        self.LogPath = logPath
        self.LogName = logName
        self.SrcPath = srcPath
        self.SrcFile = srcFile
        self.__LogDict: dict() = None
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

    def AddCaseLog(self, action, result: str = "", srcPic: BytesIO = None, screenshot: BytesIO = None):
        """插入Case步驟Log
        :param str  : 表名稱
        :param str action : 執行的動作
        :param str  result : 執行結果
        :param Image screenshot : 圖片
        """
        if(not self.SheetName in self.LogDict.keys()):
            self.__NewLogSheet(self.SheetName, CaseLogObj())
        caseLoglist: list = self.LogDict[self.SheetName]
        caseLoglist.append(
            CaseLogObj(datetime.datetime.now().strftime("%H:%M:%S"), action, result, srcPic, screenshot))

    def AddUnitLog(self, step, action, *params):
        """插入單元動作Log
        """
        if(not self.SubSheetName in self.LogDict.keys()):
            self.__NewLogSheet(self.SubSheetName, UnitLogObj())
        unitLoglist: list = self.LogDict[self.SubSheetName]
        if len(unitLoglist) > 1 and LibData.In(step, unitLoglist[len(unitLoglist)-1]):
            step = ""
        unitLoglist.append(UnitLogObj(datetime.datetime.now().strftime(
            "%H:%M:%S"), step, action, "str(*params)", str(inspect.stack())))
# endregion

# region Private
    def __CreateExcelLog(self):
        excel = LibExcel(self.LogPath, self.LogName)
        excel._AfterSetData = self.__ExcelImgAutoSizeFunc
        excel._Openfile(self.SrcPath, self.SrcFile)
        excel._WriteDatas(self.__LogDict)
        excel._AutoSize()
        excel._SaveAs()

    def __NewLogSheet(self, sheetName, logObj):
        """新增Log表
        :param str  : 表名稱
        """
        logList = []
        logList.append(logObj)
        self.__LogDict[sheetName] = logList

    def __ExcelAfterSetData(self, row, column, value):
        """自動調整Excel圖片欄位的長寬度"""
        row.height = value.height*3/4
        if value.width*3/20 > column.width:
            column.width = value.width*3/20

    def __ExcelImgAutoSizeFunc(self, row, column, value):
        if(isinstance(value, Image.Image)):
            self.__ExcelAfterSetData(row, column, value)
        else:
            pass  # 之後設定：如果值為 什麼 的時候，也可以更改cell的顏色
# endregion


class CaseLogObj:
    """CaseLog欄位格式
    注:1. 更動欄位順序同時，也要調整Excel輸出格式的順序
       2. Step欄位永遠為空
    """

    def __init__(self, time: str = "", action: str = "", result: str = "", srcPic: BytesIO = None, screenshot: BytesIO = None):
        self.Time = time
        self.Step = ""
        self.Action = action
        self.Result = result
        self.SrcPic = srcPic
        self.Screenshot = screenshot


class UnitLogObj:
    """UnitLog欄位格式
    注:1. 更動欄位順序同時，也要調整Excel輸出格式的順序
    """

    def __init__(self, time: str = "", step: str = "", action: str = "", params: str = "", stack=""):
        self.Time = time
        self.Step = step
        self.Action = action
        self.Params = params
        self.Stack = stack
