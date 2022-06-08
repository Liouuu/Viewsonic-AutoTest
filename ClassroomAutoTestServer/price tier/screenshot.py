def canvas_screenshot(driver,Screenshot_location,save_path):
    canvas = driver.find_element_by_xpath(Screenshot_location) #截圖畫面位置
    canvas.screenshot(save_path)  #存檔位置