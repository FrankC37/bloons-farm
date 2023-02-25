import pyautogui
import time

#to do; 
# add logic for level gains mid run

#assumptions
    # set alch keybind to "A"
    # set village keybind to "V"
    # set sniper keybind to "S"
    # tower upgrade hotkeys are default "," "." "/"
    # Screen Size =  1440 x 900



pyautogui.PAUSE = 0.5
#define tower placement parameters
def sniper():
    pyautogui.moveTo(1154,437)
    pyautogui.press('S',presses=4)
    pyautogui.click(clicks=2,interval=0.5)
    pyautogui.press(".",presses=2)
    pyautogui.press("/",presses=4)

def village():
    pyautogui.moveTo(1178,521)
    pyautogui.press('V',presses=4)
    pyautogui.click(clicks=2,interval=0.5)
    pyautogui.press("/",presses=2)
    pyautogui.press(",",presses=2)

def alchemist():
    pyautogui.moveTo(1207,436)
    pyautogui.press('A',presses=4)
    pyautogui.click(clicks=2,interval=0.5)
    pyautogui.press(",",presses=4)
    pyautogui.press(".",presses=2)


#buffer time to swap to bloons window
time.sleep(5)

while True:
    ### setup the match for inferno deflation
    # play button = 616,771
    pyautogui.click(616,771)

    #expert map icon = 1031,812
    pyautogui.click(1031,812)

    #inferno map = 716,471
    pyautogui.click(716,471)


    # easy diff = 432,337
    pyautogui.click(432,337)

    # deflation mode = 975, 361
    pyautogui.click(975,361)
    time.sleep(7)

    # okay the popup for delflation
    pyautogui.click(704,621)

    # tower placements
    village()
    sniper()
    alchemist()

    # run map and set to fast speed
    pyautogui.click(1375,806,clicks=2,interval=1.0)

    # add logic for level up popup clear 
    # two clicks in middle of screen

    # runtime is approx 295 seconds, time added in for a buffer
    time.sleep(310)

    # clicking exit game
    pyautogui.click(710,775)
    time.sleep(3)

    # clicking home button
    pyautogui.click(517,708)
    time.sleep(3)