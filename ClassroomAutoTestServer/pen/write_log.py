from threading import local
from webbrowser import get
import get_time

def log(content,  path):
    # 檔名 + 要寫進Log的內容 + 做這個Case跟log檔產生的時間
    f = open(path, 'a+') #用附加的方式寫檔
    data = [get_time.now(), "\t" ,content, "\n"] #這裡的get_time.now()是我用time函式抓當前時間做的
    f.writelines(data)
    f.close()
    