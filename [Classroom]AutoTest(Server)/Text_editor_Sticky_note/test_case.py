import pyautogui
import time
import canvas_compare
from PIL import Image
from selenium import webdriver
import TextEditor_func

english_text = 'Hello'
chinese_text = ['s','u','3','c','l','3']
textPosition = [530,370],[1200,370],[530,580],[1200,580]
stickynote_color = ''

def test_TextEditor_language(driver,language):
   
        TextEditor_func.open_TextEditor_Menu(driver)
        if language == 'English':
            TextEditor_func.enter_english_text(textPosition[0][0],textPosition[0][1],english_text)
        elif language == 'Chinese':
            TextEditor_func.enter_chinese_text(textPosition[2][0],textPosition[2][1],chinese_text)
        TextEditor_func.select_by_key()
        TextEditor_func.text_editor_func_select(driver,1)
        TextEditor_func.text_type(driver,1)
        TextEditor_func.text_editor_func_select(driver,2)
        TextEditor_func.text_size(driver,12)
        time.sleep(3)
        pyautogui.click(561,770,duration=0.3)
        time.sleep(1)
        TextEditor_func.open_TextEditor_Menu(driver)
        if language == 'English':
            TextEditor_func.enter_english_text(textPosition[1][0],textPosition[1][1],english_text)
        elif language == 'Chinese':
            TextEditor_func.enter_chinese_text(textPosition[3][0],textPosition[3][1],chinese_text)
        TextEditor_func.select_by_key()
        for i in range(3,8):
            TextEditor_func.text_editor_func_select(driver,i)
        TextEditor_func.text_color(driver,1,3)
        TextEditor_func.text_editor_func_select2(driver,1)
        TextEditor_func.text_color(driver,1,4)
        pyautogui.click(931,889,clicks=1)        
        time.sleep(3)

def test_StickyNote_language(driver,language,num): #num 1-5
    
    TextEditor_func.open_StickyNotes_Menu(driver,num)
    if language == 'English':
        TextEditor_func.enter_english_text(textPosition[0][0],textPosition[0][1],english_text)
    elif language == 'Chinese':
        TextEditor_func.enter_chinese_text(textPosition[2][0],textPosition[2][1],chinese_text)
    TextEditor_func.select_by_key()
    TextEditor_func.text_editor_func_select(driver,1)
    TextEditor_func.text_type(driver,1)
    TextEditor_func.text_editor_func_select(driver,2)
    TextEditor_func.text_size(driver,12)
    time.sleep(3)
    pyautogui.click(561,770,duration=0.3)
    time.sleep(1)
    TextEditor_func.open_StickyNotes_Menu(driver,num)
    if language == 'English':
        TextEditor_func.enter_english_text(textPosition[1][0],textPosition[1][1],english_text)
    elif language == 'Chinese':
        TextEditor_func.enter_chinese_text(textPosition[3][0],textPosition[3][1],chinese_text)
    TextEditor_func.select_by_key()
    for i in range(3,8):
        TextEditor_func.text_editor_func_select(driver,i)
    TextEditor_func.text_color(driver,1,3)
    TextEditor_func.text_editor_func_select2(driver,1)
    TextEditor_func.text_color(driver,1,4)
    pyautogui.click(931,889,clicks=1)        
    time.sleep(3)    


def test_TextEditor(driver):
    test_TextEditor_language(driver,'English')
    test_TextEditor_language(driver,'Chinese')
    #compare
    sample_image = './image/SampleImage1.png'
    result_image = './image/ResultImage1.png'
    TextEditor_func.canvas_screenshot(driver,sample_image)

    compare = canvas_compare.canvas_compare(sample_image,result_image,1)
    if compare == True:
        print("Pass")
    else:
        print("Failed")

    TextEditor_func.turn_page(driver)

def test_StickyNotes(driver):
    test_StickyNote_language(driver,'English',3)
    test_StickyNote_language(driver,'Chinese',5)
    #compare
    sample_image = './image/SampleImage2.png'
    result_image = './image/ResultImage2.png'
    TextEditor_func.canvas_screenshot(driver,sample_image)
    compare = canvas_compare.canvas_compare(sample_image,result_image,1)
    if compare == True:
        print("Pass")
    else:
        print("Failed")
