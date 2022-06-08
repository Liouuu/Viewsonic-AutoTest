import shape_func
import time
import canvas_compare
from PIL import Image
from selenium import webdriver
import write_log
import get_time
import logCheck
localTime = get_time.now()
def test_shape(driver):
    for i in range(1,8):
        content = "shape menu"
        content1 = "shape"
        logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
        shape_func.open_shape_menu(driver)
        time.sleep(1)
        shape_func.select_shape_type(driver,1)
        shape_func.select_shape(driver , i)
        shape_func.adjust_shape_thickness(driver,(i-1)*35/6)
        shape_func.adjust_shape_transparency(driver,(i-1)*35/6)
        shape_func.select_shape_up_color(driver,i)
        time.sleep(1.5)
        case_save_path = "./case_image/shape/shape_menu_" + str(i) + ".png"
        sample_save_path =  "./sample_image/shape/shape_menu_" + str(i) + ".png"
        shape_func.shape_menu_screenshot(driver,case_save_path)
        shape_func.shape_menu_screenshot(driver,sample_save_path)
        compare = canvas_compare.menu_compare(case_save_path,sample_save_path,i)
        if compare == True:
            print("Pass")
            write_log.log(content+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content+str(i)+ " Fail", logPath)
        shape_func.close_shape_menu(driver)
        
        shape_func.DrawLine(150+i*200 , 400+i/2 , 220+i*200 , 470+i/2)
        time.sleep(1.5)
        case_save_path1 = "./case_image/shape/shape_draw_" + str(i) + ".png"
        sample_save_path1 = "./sample_image/shape/shape_draw_" + str(i) + ".png"
        shape_func.canvas_screenshot(driver,case_save_path1)
        shape_func.canvas_screenshot(driver,sample_save_path1)
        compare1 = canvas_compare.canvas_compare(case_save_path1,sample_save_path1,i)
        if compare1 == True:
            print("Pass")
            write_log.log(content1+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content1+str(i)+ " Fail", logPath)
       
        
    shape_func.turn_page(driver)

def test_line(driver):
    for i in range (1,8):
        content = "line menu"
        content1 = "line"
        logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
        shape_func.open_shape_menu(driver)
        time.sleep(1)
        shape_func.select_shape_type(driver,2)
        shape_func.select_line(driver , i+1)
        shape_func.adjust_line_thickness(driver,(i-1)*35/18)
        shape_func.adjust_line_transparency(driver,(i-1)*35/6)
        shape_func.select_line_up_color(driver,i)
        time.sleep(1.5)
        case_save_path = "./case_image/line/line_menu_" + str(i) + ".png"
        sample_save_path =  "./sample_image/line/line_menu_" + str(i) + ".png"
        shape_func.shape_menu_screenshot(driver,case_save_path)
        shape_func.shape_menu_screenshot(driver,sample_save_path)
        compare = canvas_compare.menu_compare(case_save_path,sample_save_path,i)
        if compare == True:
            print("Pass")
            write_log.log(content+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content+str(i)+ " Fail", logPath)
        shape_func.close_shape_menu(driver)
        shape_func.DrawLine(150+i*180 , 400 , 150+i*180 , 700)
        time.sleep(1.5)
        case_save_path1 = "./case_image/line/line_draw_" + str(i) + ".png"
        sample_save_path1 = "./sample_image/line/line_draw_" + str(i) + ".png"
        shape_func.canvas_screenshot(driver,case_save_path1)
        shape_func.canvas_screenshot(driver,sample_save_path1)
        compare1 = canvas_compare.canvas_compare(case_save_path1,sample_save_path1,i)
        if compare1 == True:
            print("Pass")
            write_log.log(content1+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content1+str(i)+ " Fail", logPath)
        
    
    shape_func.turn_page(driver)
    
def test_3D (driver):
    for i in range (1,8):
        content = "3D shape menu"
        content1 = "3D shape"
        logPath ="./log/" + localTime + "_log.txt" #找位置生成空的txt檔案
        shape_func.open_shape_menu(driver)
        time.sleep(1)
        shape_func.select_shape_type(driver,3)
        shape_func.select_line(driver , i+1)
        shape_func.adjust_line_thickness(driver,(i-1)*35/6)
        shape_func.adjust_line_transparency(driver,(i-1)*35/6)
        shape_func.select_line_up_color(driver,i)
        time.sleep(1.5)
        case_save_path = "./case_image/3D/3D_menu_" + str(i) + ".png"
        sample_save_path =  "./sample_image/3D/3D_menu_" + str(i) + ".png"
        shape_func.shape_menu_screenshot(driver,case_save_path)
        shape_func.shape_menu_screenshot(driver,sample_save_path)
        compare = canvas_compare.menu_compare(case_save_path,sample_save_path,i)
        if compare == True:
            print("Pass")
            write_log.log(content+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content+str(i)+ " Fail", logPath)
        shape_func.close_shape_menu(driver)
        shape_func.DrawLine(100+i*180 , 500 , 250+i*180 , 700)
        time.sleep(1.5)
        case_save_path1 = "./case_image/3D/3D_draw_" + str(i) + ".png"
        sample_save_path1 = "./sample_image/3D/3D_draw_" + str(i) + ".png"
        shape_func.canvas_screenshot(driver,case_save_path1)
        shape_func.canvas_screenshot(driver,sample_save_path1)
        compare1 = canvas_compare.canvas_compare(case_save_path1,sample_save_path1,i)
        if compare1 == True:
            print("Pass")
            write_log.log(content1+str(i) + " Pass", logPath)
        else:
            print("Failed")
            write_log.log(content1+str(i)+ " Fail", logPath)
