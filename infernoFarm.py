import pyautogui
import time

#to do; 
# add logic for level gains mid run, needs screen coords 

# Screen Size =  1440 x 900
#buffer time to swap to bloons
time.sleep(5)

pyautogui.PAUSE = 1.0

while True:
    ### setup the match for inferno deflation
    # play button = 616,771
    pyautogui.click(616,771)

    # # expert map icon = 1031,812
    pyautogui.click(1031,812)

    # # inferno map = 716,471
    pyautogui.click(716,471)


    # # easy diff = 432,337
    pyautogui.click(432,337)

    # # deflation mode = 975, 361
    pyautogui.click(975,361)
    time.sleep(7)

    #okay the popup
    pyautogui.click(704,621)


    ### towers
    ## Hot Keys Village = V, Sniper = S, Alch = A


    # village = 1183,543
    # place "V" and send upgrade commands
    # // && ,,
    pyautogui.moveTo(1178,521)
    pyautogui.press('V',presses=4)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press("/",presses=2)
    pyautogui.press(",",presses=2)

    # sniper = 1154,437
    # place "S" and send upgrade commands
    # .. & ////
    pyautogui.moveTo(1154,437)
    pyautogui.press('S',presses=4)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press(".",presses=2)
    pyautogui.press("/",presses=4)

    # alch = 1207,436
    # place "A" and send upgrade commands
    # ,,,, && ..
    pyautogui.moveTo(1207,436)
    pyautogui.press('A',presses=4)
    pyautogui.click()
    pyautogui.click()
    pyautogui.press(",",presses=4)
    pyautogui.press(".",presses=2)

    # run map and set to fast speed
    # play button = 1375,806 (two clicks)
    pyautogui.click(1375,806,clicks=2,interval=1.0)

    # add logic for level up popup clear 
    # two clicks in middle of screen

    # runtime is approx 295 seconds
    time.sleep(310)
    # exit game = 710,775
    pyautogui.click(710,775)
    time.sleep(3)

    # home = 517,708
    pyautogui.click(517,708)
    time.sleep(3)