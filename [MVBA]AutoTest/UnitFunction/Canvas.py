from appium.webdriver.common.touch_action import TouchAction
from Params.ElementParams import ElementParam


def Click_On_Selector(self):
    self.driver.find_element_by_id('com.viewsonic.droid:id/btnLasso').click()


def Select_Object(self, begin_x, begin_y, end_x, end_y):
    touch = TouchAction(self.driver)
    touch.press(x=begin_x, y=begin_y).move_to(
        x=end_x, y=end_y).release().perform()


def Tap(self, pos_x, pos_y):
    try:
        touch = TouchAction(self.driver)
        touch.press(x=pos_x, y=pos_y).release().perform()
    except:
        pass
        #print("Tap error")


# args are a list of points: [[292,346],[117,238],[108,353],[265,457],[204,572],[115,518]]
def Swipe(self, args: list):
    touch = TouchAction(self.driver)
    T = True
    MOV = "touch.press(x="+str(args[0][0])+",y="+str(args[0][1])+")"
    i = 1
    while T == True:
        MOV = MOV+".move_to(x="+str(args[i][0])+",y="+str(args[i][1])+")"
        # print(i)
        # print(MOV)
        i += 1
        if i >= len(args):
            MOV = MOV+".release().perform()"
            break
    exec(MOV)
