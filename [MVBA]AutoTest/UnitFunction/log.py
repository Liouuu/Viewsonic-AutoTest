import logging
import logging.config
import datetime

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日誌級別關係對映

    def __init__(self,filename,level='info',fmt='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#設定日誌格式
        format_str.datefmt = '%Y%m%d %H:%M:%S'#日期標準化
        self.logger.setLevel(self.level_relations.get(level))#設定日誌級別
        sh = logging.StreamHandler()#往螢幕上輸出
        sh.setFormatter(format_str) #設定螢幕上顯示的格式
        th = logging.FileHandler(filename=filename, encoding='utf-8')
        th.setFormatter(format_str)#設定檔案裡寫入的格式
        self.logger.addHandler(sh) #把物件加到logger裡
        self.logger.addHandler(th)