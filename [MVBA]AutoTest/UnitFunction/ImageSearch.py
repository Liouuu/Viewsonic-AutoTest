from asyncio.log import logger
from re import search
from tkinter import Canvas
from unittest import result
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
from UnitFunction import Canvas, Adorner, MagicBox


def inputsearch(self, type):
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/searchEditText"))
    )
    self.driver.find_element_by_id(
        "com.viewsonic.droid:id/searchEditText").send_keys(type)
    WebDriverWait(self.driver, 15).until(
        EC.presence_of_element_located(
            (By.ID, "com.viewsonic.droid:id/search_icon"))
    )
    self.driver.find_element_by_id(
        "com.viewsonic.droid:id/search_icon").click()
    search = "搜尋 "+type+" Image"
    WebDriverWait(self.driver, 60, 1).until(
        EC.presence_of_element_located(
            (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]'))
    )
    time.sleep(10)
    return search


def Importimage(self, type):
    try:
        touch = TouchAction(self.driver)
        imagelist = [[791, 499], [945, 499], [1121, 492],
                     [787, 626], [952, 618], [1121, 618]]
        i = 0
        while True:
            imagetype = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['+str(1+i)+']/android.widget.TextView[1]').get_attribute("text")
            MOV = "touch.tap(x="+str(imagelist[i][0]) + \
                ",y="+str(imagelist[i][1])+").perform()"
            i += 1
            if imagetype[-3::] == type:
                break
            elif i >= 6:
                result = "暫時無法搜到" + type + "，請稍後再試~"
                return False, result
        time.sleep(10)
        for tap in range(3):
            exec(MOV)
        return True, imagetype
    except:
        Searchresult = "搜尋超時，請稍後再試~"
        return Searchresult, Searchresult


def Checktype(self, type):
    try:
        MagicBox.CloseMagicBox(self)
        Canvas.Select_Object(self, 77, 146, 315, 323)
        time.sleep(10)
        Adorner.buttonSaveResource(self)
        MagicBox.SelectStorage(self)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, "com.viewsonic.droid:id/textSaveResourceFormat"))
        )
        imagetype = self.driver.find_element_by_id(
            "com.viewsonic.droid:id/textSaveResourceFormat").get_attribute("text")

        if imagetype[-3::] == type:
            return True, imagetype
        else:
            return False, imagetype
    except:
        importresult = "點擊異常，請稍後再試~"
        return importresult, importresult
