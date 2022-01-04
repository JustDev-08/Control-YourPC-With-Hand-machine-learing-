import pyautogui

def program(pre):
    if pre == 'normal' :
        pass
    elif pre == 'left' :
        pyautogui.move(-40 , 0)
    elif pre == 'right' :
        pyautogui.move(40 , 0)
    elif pre == 'up' :
        pyautogui.move(0 , -40)
    elif pre == 'down' :
        pyautogui.move(0 , 40)
    elif pre == 'click' :
        pyautogui.click()

