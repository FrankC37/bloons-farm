import pyautogui
import time
screenSizeX, screenSizeY = pyautogui.size()

if screenSizeX != 1440 and screenSizeY != 900:
    print('Resolution is Incorrect for this scripts parameters, you will need to make customizations to make this fit your resolution.')
    print(f"Your screen resolution is {screenSizeX},{screenSizeY}")
    exit()
else:
    pyautogui.PAUSE = 0.5
    #define tower placement parameters
    # hero placement if farming hero achievement
    def hero():
        pyautogui.moveTo(610,284)
        pyautogui.press('U',presses=2,interval=0.5)
        pyautogui.click()
        
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

    #define functions for game controls
    def startMap():
        # play button
        pyautogui.click(616,785)
        #expert map icon
        pyautogui.click(1031,812)
        #inferno map
        pyautogui.click(716,471)
        # easy diff
        pyautogui.click(432,337)
        # deflation mode
        pyautogui.click(975,361)
        time.sleep(4)
        # clear deflation popup
        pyautogui.click(704,621)

    def runMap():
        pyautogui.click(1375,806,clicks=2,interval=1.0)

    def endOfMatch():
        pyautogui.click(725,750)
        pyautogui.click(517,708)

    #buffer time to swap to bloons window
    time.sleep(3)
    cash = 0
    # main loop
    while True:
        startMap()

        # tower placements
        village()
        sniper()
        alchemist()

        runMap()
        time.sleep(297)

        endOfMatch()
        time.sleep(3)
        cash = cash + 66
        print(f"Est Cash Gained: {cash}")