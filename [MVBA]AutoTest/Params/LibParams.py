from enum import Enum


class LogType(Enum):
    txt = 0
    excel = 1


class c_LogParam:
    @property
    def _Time(self): return "時間"
    @property
    def _Step(self): return "步驟"
    @property
    def _Action(self): return "執行動作"
    @property
    def _Result(self): return "結果"
    @property
    def _Picture(self): return "圖片"
    @property
    def _Picture(self): return "等級"
    # @property (記錄執行程式的Stack，未來再考慮)
    # def _Stack(self): return "堆疊"


LogParam = c_LogParam
