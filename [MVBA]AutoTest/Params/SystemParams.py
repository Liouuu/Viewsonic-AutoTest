class c_sysPath:
    @property
    def _LogPath(self): return "./Output/Logs/Background"
    @property
    def __OutputPath(self): return "./Output"
    @property
    def _LogPath(self): return self.__OutputPath+"/Logs"
    @property
    def _ExcelPath(self): return self.__OutputPath+"/Excels"


sysPath = c_sysPath()


class c_SysParam:
    @property
    def _Email(self): return "mvbaautotest2@gmail.com"
    @property
    def _Password(self): return "$Password1"


SysParams = c_SysParam()
