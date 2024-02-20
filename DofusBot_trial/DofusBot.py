import pyautogui
import time
import keyboard
import random
import win32api, win32con
import FarmWood
import Fight
import DestroyWood
# import CircleCreator

start_time = time.time()
count = 0
confidence_mapswitch = 0.66
farm_circle_key = 22
gathering_time = 10.4
time_each_map = 20
dofus_border_left = 303
dofus_border_top = 51
dofus_border_width = 1312
dofus_border_height = 978


def locateImg(img_name, conf, region = (dofus_border_left, dofus_border_top, dofus_border_width, dofus_border_height)):    
    #img_name includes '.png' , funtion returns tuple of coordinates x and y
    if pyautogui.locateCenterOnScreen(img_name,region = region, confidence = conf) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen(img_name, region = region, confidence = conf)
            return (x, y)
        except AttributeError:
            pass
        

def fightORfarm():
    if pyautogui.locateCenterOnScreen('OutOfFightBars.png', region = (1567, 901, 27, 113), confidence = 0.85) != None:
        return 'farm'
    if pyautogui.locateCenterOnScreen('InFightBars.png', region = (1567, 901, 27, 113), confidence = 0.85) != None:
        return 'fight'
    return 'dkWhatTODO'
    

def mouseover(x, y):
    win32api.SetCursorPos( (x,y) )

def click(x, y):
    mouseover(x,y)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def goUp():
    if pyautogui.locateCenterOnScreen('map_switch3.png', region = (375, 27, 1075, 100), confidence = confidence_mapswitch) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('map_switch3.png', region = (375, 27, 1075, 100), confidence = confidence_mapswitch)
            click(x, y)
            time.sleep(1)
            click(x, y)
            time.sleep(2)
        except AttributeError:
            pass
        time.sleep(0.5)
    else:
        print('I cant see the map_switch3.png')
        time.sleep(0.5)

def goDown():
    if pyautogui.locateCenterOnScreen('map_switch3.png', region = (375, 742, 1075, 100), confidence = confidence_mapswitch) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('map_switch3.png', region = (375, 742, 1075, 100), confidence = confidence_mapswitch)
            click(x, y)
            time.sleep(1)
            click(x, y)
            time.sleep(2)
        except AttributeError:
            pass
        time.sleep(0.5)
    else:
        print('I cant see the map_switch3.png')
        time.sleep(0.5)

def goRight():
    if pyautogui.locateCenterOnScreen('map_switch3.png', region = (1517,100,100,700), confidence = confidence_mapswitch) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('map_switch3.png', region = (1517,100,100,700), confidence = confidence_mapswitch)
            click(x, y)
            time.sleep(1)
            click(x, y)
            time.sleep(2)
        except AttributeError:
            pass
        time.sleep(0.5)
    else:
        print('I cant see the map_switch3.png')
        time.sleep(0.5)

def map_switch_astrub_walnut():
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord0,-25\img0,-25.png', confidence = 0.8) != None:
        click(822,78)
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord0,-26\img0,-26.png', confidence = 0.8) != None:
        click(821,791)

def map_switch_jellyPen_walnut():
    headsortails = random.randint(1,2)
    if (pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord6,29\ss.png', confidence = 0.81) != None or 
        pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord6,29\ss2.png', confidence = 0.81) != None):
        click(1193,792)
        time.sleep(3)
    if (pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord6,30\ss.png', confidence = 0.81) != None or 
        pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord6,30\ss2.png', confidence = 0.81) != None):
        if headsortails == 1:
            click(1054,102)
            time.sleep(3)
        else:
            click(1520,435)
            time.sleep(3)
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord7,30\ss.png', confidence = 0.81) != None:
        if headsortails == 1:
            click(355,412)
            time.sleep(3)
        else:
            click(1568,745)
            time.sleep(3)
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord8,30\ss.png', confidence = 0.81) != None:
        if headsortails == 1:
            click(354,743)
            time.sleep(3)
        else:
            click(1568,269)
            time.sleep(3)
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Coord9,30\ss.png', confidence = 0.81) != None:
        click(354,222)
        time.sleep(3)


def map_switch_bombu():
    print("switching map...")
    coord_detect_conf = 0.84
    wait_time_after_map_switch_click = 2
    headsortails = random.randint(1,2)
    
    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-22\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-22 coordinates")
        if headsortails == 1:
            click(354,411)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-23\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-23 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if (pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-24\ss.png', confidence = coord_detect_conf) != None or
     pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-24\ss1.png', confidence = coord_detect_conf)):
        print("detected -8,-24 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(1007,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-25\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-25 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-26\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-26 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-27\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-27 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(1380,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-28\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-28 coordinates")
        if headsortails == 1:
            click(1380,791)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-29\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-29 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-30\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-30 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)
        
    if (pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-31\ss.png', confidence = coord_detect_conf) != None or
        pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-31\ss1.png', confidence = 0.75) != None):
        print("detected -8,-31 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(915,77)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-32\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-32 coordinates")
        if headsortails == 1:
            click(914,793)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(353,410)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-9,-22\ss.png', confidence = coord_detect_conf) != None:
        print("detected -9,-22 coordinates")
        if headsortails == 1:
            click(355,698)
            time.sleep(wait_time_after_map_switch_click)
        else:
            click(1567,412)
            time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-9,-32\ss.png', confidence = coord_detect_conf) != None:
        print("detected -9,-32 coordinates")
        click(1567,412)
        time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-10,-22\ss.png', confidence = coord_detect_conf) != None:
        print("detected -10,-22 coordinates")
        click(1568,745)
        time.sleep(wait_time_after_map_switch_click)

    if pyautogui.locateCenterOnScreen(r'C:\Users\Cem\Desktop\Dofus Database&Tools\Retro\DofusBot\Coordinates\Bombu\Coord-8,-21\ss.png', confidence = coord_detect_conf) != None:
        print("detected -8,-21 coordinates")
        click(1007,78)
        time.sleep(wait_time_after_map_switch_click)


    
    


        
def goLeft():
    if pyautogui.locateCenterOnScreen('map_switch3.png', region = (300,100,100,700), confidence = confidence_mapswitch) != None:
        try: 
            x, y = pyautogui.locateCenterOnScreen('map_switch3.png', region = (300,100,100,700), confidence = confidence_mapswitch)
            click(x, y)
            time.sleep(1)
            click(x, y)
            time.sleep(2)
        except AttributeError:
            pass
        time.sleep(0.5)
    else:
        print('I cant see the map_switch3.png')
        time.sleep(0.5)
    # click(354, 363)

def ok_level_up():
    if pyautogui.locateOnScreen('okButton.png', confidence=0.7) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('okButton.png', confidence=0.7).left + 3, pyautogui.locateOnScreen('okButton.png', confidence=0.7).top + 3)
            time.sleep(0.2)
        except AttributeError:
            pass

def close():
    if pyautogui.locateOnScreen('close.png', confidence=0.7) != None:   #returns Box(left=1551, top=110, width=32, height=50) if not none
        try:
            click(pyautogui.locateOnScreen('close.png', confidence=0.7).left + 3, pyautogui.locateOnScreen('close.png', confidence=0.7).top + 3)
            time.sleep(0.2)
        except AttributeError:
            pass

def farm():
    global start_time
    current_time = time.time()
    time_dif = current_time - start_time
    if time_dif > time_each_map:    #timer for map switch
        # mapswitch(farm_circle_key)
        # farm_circle_key += 1
        map_switch_bombu()
        start_time = time.time()
    random_integer = random.randint(1,10)           #for random stops
    print(random_integer)
    if random_integer < 10:
        FarmWood.farmBombu()
        ok_level_up()
        close()
    else:
        time.sleep(10)

def fight():
    onetofour = random.randint(1,4)
    Fight.ready()
    sleep_time = random.randint(10,25)
    myChar_Cords = Fight.locateMyChar()
    if sleep_time < 13:
        Fight.clickFourthSpell()
        Fight.clickSelf( myChar_Cords )
    if onetofour == 1:
        Fight.clickSecondSpell()
        Fight.clickAdjacentSE( myChar_Cords )
        Fight.passTurn()
    if onetofour == 2:
        Fight.clickSecondSpell()
        Fight.clickAdjacentSW( myChar_Cords )
        Fight.passTurn()
    if onetofour == 3:
        Fight.clickSecondSpell()
        Fight.clickAdjacentNE( myChar_Cords )
        Fight.passTurn()
    if onetofour == 4:
        Fight.clickSecondSpell()
        Fight.clickAdjacentNW( myChar_Cords )
        Fight.passTurn()
    if pyautogui.locateCenterOnScreen('tactical_mode_unchecked.png', confidence=0.9) != None:
        x, y = pyautogui.locateCenterOnScreen('tactical_mode_unchecked.png', confidence = 0.9)
        click(x, y)
    time.sleep(sleep_time)
    ok_level_up()
    close()


#test program
# while keyboard.is_pressed('q') == False:
#     mapswitch(farm_circle_key)

#main program   
while keyboard.is_pressed('q') == False:
    state = fightORfarm()
    print(state)
    time.sleep(0.5)
    while state == 'fight':
        fight()
        state = fightORfarm()
    print(state)
    while state == 'farm':
        farm()
        state = fightORfarm()
    
    


    

    
   