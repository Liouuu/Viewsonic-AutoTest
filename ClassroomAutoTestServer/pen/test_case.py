import pen_func
import time
from PIL import Image
from selenium import webdriver
import canvas_compare
import write_log
import get_time
import logCheck
import pyautogui
localTime = get_time.now()
def test_marker(driver):
    for i in range(1,8):
        content = "marker menu"
        content1 = "marker"
        logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案    
        pen_func.open_menu(driver)
        time.sleep(1)
        pen_func.select_pen_type(driver,1)
        pen_func.adjust_marker_thickness(driver,(i-1)*35/6)
        pen_func.adjust_marker_transparency(driver,(i-1)*35/6)
        pen_func.select_marker_up_color(driver,i)
        sample_image = "./sample/marker/marker_menu_" + str(i) + ".png"
        case_image = "./case_img/marker/marker_menu_" + str(i) + ".png"
        pen_func.menu_screenshot(driver,case_image)
        # pen_func.menu_screenshot(driver,sample_image)
        result = canvas_compare.canvas_compare(sample_image,case_image,i)
        if result == True:
            print("marker_menu"+str(i)+"   Pass")
            write_log.log(content+str(i) + " Pass", logPath)
        else:
            print("marker_menu"+str(i)+"   Failed")
            write_log.log(content+str(i)+ " Fail", logPath)
            
        time.sleep(1.5)
        pen_func.close_pen_menu(driver)
        pen_func.DrawLine(210+i*50,290,330+i*50,450)
        time.sleep(1.5)
        sample1_image = "./sample/marker/marker_draw_" + str(i) + ".png"
        case1_image = "./case_img/marker/marker_draw_" + str(i) + ".png"
        pen_func.canvas_screenshot(driver,case1_image)
        # pen_func.canvas_screenshot(driver,sample1_image)
        result = canvas_compare.canvas_compare(sample1_image,case1_image,i)
        if result == True:
            print("marker_canvas"+str(i)+"   Pass")
            write_log.log(content1+str(i) + " Pass", logPath)
        else:
            print("marker_canvas"+str(i)+"   Failed")
            write_log.log(content1+str(i)+ " Fail", logPath)
      
def test_highlighter(driver):
    for i in range(1,6):
        content = "highlighter menu"
        content1 = "highlighterr"
        logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案 
        pen_func.open_menu(driver)
        time.sleep(1)
        pen_func.select_pen_type(driver,2)
        pen_func.adjust_highlighter_thickness(driver,(i-1)*35/4)
        pyautogui.moveTo(1573,577,0.4)
        pyautogui.moveTo(1625,516,0.4)
        pen_func.select_highlighter_color(driver,i)
        
        time.sleep(1.5)
        sample_image = "./sample/highlighter/highlighter_menu_" + str(i) + ".png"
        case_image = "./case_img/highlighter/highlighter_menu_" + str(i) + ".png"
        pen_func.menu_screenshot(driver,case_image)
        # pen_func.menu_screenshot(driver,sample_image)
        result = canvas_compare.canvas_compare(sample_image,case_image,i)
        if result == True:
            print("highlighter_menu"+str(i)+"   Pass")
            write_log.log(content+str(i) + " Pass", logPath)
        else:
            print("highlighter_menu"+str(i)+"   Failed")
            write_log.log(content+str(i) + " Pass", logPath)
        
        pen_func.close_pen_menu(driver)
        pen_func.DrawLine(210+i*50,500,330+i*50,660)
        time.sleep(1.5)
        sample1_image = "./sample/highlighter/highlighter_draw_" + str(i) + ".png"
        case1_image = "./case_img/highlighter/highlighter_draw_" + str(i) + ".png"
        pen_func.canvas_screenshot(driver,case1_image)
        # pen_func.canvas_screenshot(driver,sample1_image)
        result = canvas_compare.canvas_compare(sample1_image,case1_image,i)
        if result == True:
            print("highlighter_canvas"+str(i)+"   Pass")
            write_log.log(content1+str(i) + " Pass", logPath)
        else:
            print("highlighter_canvas"+str(i)+"   Failed")
            write_log.log(content1+str(i) + " Pass", logPath)