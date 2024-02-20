import pyautogui
import time
import win32api, win32con

confidence_tree_images = 0.6

def mouseover(x, y):
    win32api.SetCursorPos( (x,y) )

def click(x, y):
    mouseover(x,y)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def farmAsh():
    if pyautogui.locateOnScreen('ash2.png', confidence=confidence_tree_images) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('ash2.png', confidence=confidence_tree_images).left + 3, pyautogui.locateOnScreen('ash2.png', confidence=confidence_tree_images).top + 3)
            time.sleep(0.8)
        except AttributeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass

def farmChestnut():
    if pyautogui.locateOnScreen('chestnut.png', confidence=confidence_tree_images) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('chestnut.png', confidence=confidence_tree_images).left + 3, pyautogui.locateOnScreen('chestnut.png', confidence=confidence_tree_images).top + 3)
            time.sleep(0.8)
        except AttributeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass

def farmChestnut2():
    if pyautogui.locateOnScreen('chestnut2.png', confidence=confidence_tree_images) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('chestnut2.png', confidence=confidence_tree_images).left + 23, pyautogui.locateOnScreen('chestnut2.png', confidence=confidence_tree_images).top + 15)
            time.sleep(0.8)
        except AttributeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass

def farmWalnut(): 
    if pyautogui.locateOnScreen('walnut2.png', confidence=confidence_tree_images) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('walnut2.png', confidence=confidence_tree_images).left + 3, pyautogui.locateOnScreen('walnut2.png', confidence=confidence_tree_images).top + 3)
            time.sleep(0.8)
        except AttributeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass
    
def farmWalnut2(): 
    if pyautogui.locateOnScreen('walnut3.png', confidence=confidence_tree_images) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('walnut3.png', confidence=confidence_tree_images).left + 7, pyautogui.locateOnScreen('walnut3.png', confidence=confidence_tree_images).top + 6)
            time.sleep(0.8)
        except AttributeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass

def farmBombu():
    if (pyautogui.locateCenterOnScreen('bombu.png', confidence=confidence_tree_images) != None or
        pyautogui.locateCenterOnScreen('bombu1.png', confidence=confidence_tree_images) != None or
        pyautogui.locateCenterOnScreen('bombu2.png', confidence=confidence_tree_images) != None or
        pyautogui.locateCenterOnScreen('bombu5.png', confidence=confidence_tree_images) != None):
        print("found bombu tree")
        try:
            x, y = pyautogui.locateCenterOnScreen('bombu.png'  , confidence=confidence_tree_images )
            click(x, y)
        except AttributeError:
            pass
        except TypeError:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('bombu1.png', confidence=confidence_tree_images)
            click(x, y)
        except AttributeError:
            pass
        except TypeError:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('bombu2.png' , confidence=confidence_tree_images)
            click(x, y)
        except AttributeError:
            pass
        except TypeError:
            pass
        try:
            x, y = pyautogui.locateCenterOnScreen('bombu5.png' , confidence=confidence_tree_images)
            click(x, y)
        except AttributeError:
            pass
        except TypeError:
            pass
    if pyautogui.locateOnScreen('cut.png', confidence=0.9) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('cut.png', confidence=0.9).left + 3, pyautogui.locateOnScreen('cut.png', confidence=0.9).top + 3)
            time.sleep(0.5)
        except AttributeError:
            pass
            



     









