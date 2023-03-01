import pyautogui

collectButton = pyautogui.locateCenterOnScreen('collect.png')
pyautogui.click(collectButton)

print(collectButton)