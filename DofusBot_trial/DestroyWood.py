import pyautogui
import win32api, win32con
import time

inventory_icon_loc = (1276, 842)
resources_icon_loc = (1468, 227)
close_inv_sign_loc = (1570, 108)


def locateImg_withRegion(img_name, region, conf):    #img_name includes '.png' , region is a tuple of size 2 , confidence is float
    #returns coordinates if it can locate the said image in given region with given confidence
    #returns False if it cannot locate the image
    if pyautogui.locateCenterOnScreen(img_name,region = region, confidence = conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen(img_name, region = region, confidence = conf)
            return (x, y)
        except AttributeError:
            pass

def locateImg(img_name, conf):     #returns a tuple
    if pyautogui.locateCenterOnScreen(img_name, confidence = conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen(img_name, confidence = conf)
            return (x, y)
        except AttributeError:
            pass

def mouseover(x, y):
    win32api.SetCursorPos( (x,y) )

def click(x, y):
    try:
        mouseover(x,y)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    except TypeError:
        pass
    except AttributeError:
        pass

def right_click(x, y):
    try:
        mouseover(x,y)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    except TypeError:
        pass
    except AttributeError:
        pass
    

# def destroyWood(wood_type):
#     click(inventory_icon_loc[0], inventory_icon_loc[1])     
#     click(resources_icon_loc[0], resources_icon_loc[1]) 
#     wood_png_loc = locateImg(f"{wood_type}_wood.png", conf = 0.9)
#     right_click(wood_png_loc[0],wood_png_loc[1])
#     destroy_the_item_loc = locateImg("destroy_the_item.png", conf = 0.9)
#     click(destroy_the_item_loc[0],destroy_the_item_loc[1])
#     max_loc = locateImg("max.png", conf = 0.9)
#     click(max_loc[0],max_loc[1])
#     tick_sign_loc = locateImg("tick_sign.png", conf = 0.9)
#     click(tick_sign_loc[0],tick_sign_loc[1])
#     click(close_inv_sign_loc[0], close_inv_sign_loc[1])

def destroyAsh():
    try:
        click(inventory_icon_loc[0], inventory_icon_loc[1])     
        click(resources_icon_loc[0], resources_icon_loc[1]) 
        wood_png_loc = locateImg("ash_wood.png", conf = 0.9)
        right_click(wood_png_loc[0],wood_png_loc[1])
        destroy_the_item_loc = locateImg("destroy_the_item.png", conf = 0.9)
        click(destroy_the_item_loc[0],destroy_the_item_loc[1])
        max_loc = locateImg("max.png", conf = 0.9)
        click(max_loc[0],max_loc[1])
        tick_sign_loc = locateImg("tick_sign.png", conf = 0.9)
        click(tick_sign_loc[0],tick_sign_loc[1])
        click(close_inv_sign_loc[0], close_inv_sign_loc[1])
    except TypeError:
        pass

