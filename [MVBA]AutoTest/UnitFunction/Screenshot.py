from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def screenshotShapesMenu(self,menu_save_path):
    #img_index = i
    #save_path = menuPath + str(img_index) + ".png"
    pattern_menu_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout"
    pattern_menu = self.driver.find_element_by_xpath(pattern_menu_xpath)
    pattern_menu.screenshot(menu_save_path)

def screenshotCanvas(self, canvas_save_path):
    #save_path = canvas_save_path + str(img_index) + ".png"
    canvas_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]"
    canvas = self.driver.find_element_by_xpath(canvas_xpath)
    canvas.screenshot(canvas_save_path)

def screenshotTextEditor(self, save_path):
    text_editor = self.driver.find_element_by_id("com.viewsonic.droid:id/parentTitleBar")
    text_editor.screenshot(save_path)

def screenshotStickyNoteCanvas(self, save_path):
    stCanvas = self.driver.find_element_by_id("com.viewsonic.droid:id/sticky_note_canvas_layout")
    stCanvas.screenshot(save_path)

def screenshotStickyNoteBar(self, save_path):
    stBar = self.driver.find_element_by_id("com.viewsonic.droid:id/titleBar")
    stBar.screenshot(save_path)

def screenshotPenMenu(self, save_path):
    pen_menu_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[10]/android.widget.LinearLayout"
    pen_menu = self.driver.find_element_by_xpath(pen_menu_xpath)
    pen_menu.screenshot(save_path)

def screenshotAdornerMenu(self, save_path):
    Adorner_Menu = self.driver.find_element_by_id("com.viewsonic.droid:id/layoutControlBar")
    Adorner_Menu.screenshot(save_path)

def screenshotObjectBox(self, save_path):
    Object_Box = self.driver.find_element_by_id("com.viewsonic.droid:id/layoutAdorner")
    Object_Box.screenshot(save_path)