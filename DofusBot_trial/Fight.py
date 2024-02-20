import pyautogui
import win32api, win32con
import time

locate_myChar_conf = 0.7

def mouseover(x, y):
    win32api.SetCursorPos( (x,y) )

def click(x, y):
    mouseover(x,y)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def ready():
    if pyautogui.locateCenterOnScreen('ReadyButton.png', confidence=0.66) != None:   
        try:
            x, y = pyautogui.locateCenterOnScreen('ReadyButton.png', confidence=0.66)
            click(x, y)
            time.sleep(0.2)
        except AttributeError:
            pass

def locateMyChar():
    if pyautogui.locateCenterOnScreen('advOmawuyela.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('advOmawuyela.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('advOmawuyela1.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('advOmawuyela1.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('advOmawuyela2.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('advOmawuyela2.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('advOmawuyela3.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('advOmawuyela3.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass
    if pyautogui.locateCenterOnScreen('gobOwamuyela.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('gobOwamuyela.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('gobOwamuyela1.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('gobOwamuyela1.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('gobOwamuyela2.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('gobOwamuyela2.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass 
    if pyautogui.locateCenterOnScreen('gobOwamuyela3.png', region = (300,50,1300,775), confidence = locate_myChar_conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('gobOwamuyela3.png', region = (300,50,1300,775), confidence = locate_myChar_conf)
            y += 30
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass
    time.sleep(0.5)
         
def clickAdjacentSE( cord_list ): #clicks adjacent south east square. Takes an array as parameter
    try:
        x = cord_list[0] + 50
        y = cord_list[1] + 25
        click(x, y)
        time.sleep(0.5)
    except TypeError:
        pass

def clickAdjacentSW( cord_list ): #clicks adjacent south east square. Takes an array as parameter
    try:
        x = cord_list[0] - 50
        y = cord_list[1] + 25
        click(x, y)
        time.sleep(0.5)
    except TypeError:
        pass

def clickAdjacentNW( cord_list ): #clicks adjacent south east square. Takes an array as parameter
    try:
        x = cord_list[0] - 50
        y = cord_list[1] - 25
        click(x, y)
        time.sleep(0.5)
    except TypeError:
        pass

def clickAdjacentNE( cord_list ): #clicks adjacent south east square. Takes an array as parameter
    try:
        x = cord_list[0] + 50
        y = cord_list[1] - 25
        click(x, y)
        time.sleep(0.5)
    except TypeError:
        pass

def clickSelf( cord_list ): #clicks adjacent south east square. Takes an array as parameter
    try:
        x = cord_list[0]
        y = cord_list[1]
        click(x, y)
        time.sleep(0.5)
    except TypeError:
        pass

def clickSecondSpell():
    click(1289, 934)
    time.sleep(0.5)

def passTurn():
    click(1173, 991)
    time.sleep(0.5)


def clickFourthSpell():
    click(1388, 933)
    time.sleep(0.5)

def locateTurnPointer():     # returns true if it is my turn false otherwise; assuming im on the right second order
    if pyautogui.locateCenterOnScreen('turnPointer.png', region = (900,690,750,55), confidence = 0.55) != None: ## scanning turn bar for turnPointerlocation
        try: 
            x, y = pyautogui.locateCenterOnScreen('turnPointer.png', region = (900,690,750,55), confidence = 0.55)
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass
def locateMyTurnBarIcon():
    if pyautogui.locateCenterOnScreen('turnBarAdvOwamuyela.png', region = (900,725,750,200), confidence = 0.8) != None: ## scanning turn bar for turnPointerlocation
        try: 
            x, y = pyautogui.locateCenterOnScreen('turnBarAdvOwamuyela.png', region = (900,725,750,200), confidence = 0.8)
            return [x, y]
        except AttributeError:
            pass 
        except TypeError:
            pass

def isMyTurn():
    pointerLoc = locateTurnPointer()   #returns a list of size 2 containing the coordinates
    myIconLoc = locateMyTurnBarIcon()   #returns a list of size 2 containing the coordinates
    try:
        pointer_x = pointerLoc[0]
    except TypeError:
        return False
    try:
        myIcon_x = myIconLoc[0]
    except TypeError:
        return False
    horizontal_dif_between_pointer_and_icon = pointer_x - myIcon_x
    if horizontal_dif_between_pointer_and_icon < 20 or horizontal_dif_between_pointer_and_icon > -20:
        return True
    else:
        return False


    
    