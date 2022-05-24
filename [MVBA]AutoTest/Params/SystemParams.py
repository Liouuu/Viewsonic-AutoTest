from this import s


class c_sysPath:
    @property
    def __OutputPath(self): return "./Output"
    @property
    def _LogPath(self): return self.__OutputPath+"/Logs"
    @property
    def _SrcPath(self): return self.__OutputPath+"/Srcs"
    @property
    def _ExcelPath(self): return self.__OutputPath+"/Excels"


SysPath = c_sysPath()


class c_SysParam:
    @property
    def _Email(self): return "mvbaautotest2@gmail.com"
    @property
    def _Password(self): return "$Password1"


SysParams = c_SysParam()


class c_fileExt:
    @property
    def _xlsx(self): return ".xlsx"
    @property
    def _png(self): return ".png"


FileExt = c_fileExt()


class c_imgPath:
    @property
    def __TestCasesPath(self): return "./TestCases"
    @property
    def _ScreenshotsPath(self): return self.__TestCasesPath+"/Screenshots"
    @property
    def _TextPath(self): return self._ScreenshotsPath+"/Text"
    @property
    def _TextImgPath(self): return self._TextPath

ImgPath = c_imgPath()