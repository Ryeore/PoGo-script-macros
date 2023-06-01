import time

import pyautogui
import random

start_x = 1000
start_y = 400
profile_x = 1000
profile_y = 300
close_x = 950
close_y = 920
gift_x = 800
gift_y = 740
select_gift_x = 1000
select_gift_y = 350
confirm_x = 1000
confirm_y = 850
restart_x = 1120
restart_y = 920
rerun_x = 1120
rerun_y = 820


#How many gifts you have
gifts = 20

time.sleep(3)

# Move the mouse to the specified coordinates
for a in range(0, gifts):
    wait = random.random() + 2
    pyautogui.moveTo(start_x, start_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(profile_x, profile_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(close_x, close_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(gift_x, gift_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(select_gift_x, select_gift_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(confirm_x, confirm_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(close_x, close_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(restart_x, restart_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(rerun_x, rerun_y)
    time.sleep(wait)
    pyautogui.click()
    pyautogui.click()
    time.sleep(wait)