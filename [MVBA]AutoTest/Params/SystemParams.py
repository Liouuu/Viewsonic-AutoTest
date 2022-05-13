class c_sysPath:
    @property
    def __OutputPath(self): return "./Output"
    @property
    def _LogPath(self): return self.__OutputPath+"/Logs"
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


FileExt = c_fileExt()
