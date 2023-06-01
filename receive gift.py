import time

import pyautogui
import random

start_x = 1000
start_y = 400
open_x = 1000
open_y = 820
close_x = 950
close_y = 920
restart_x = 1120
restart_y = 920
rerun_x = 1140
rerun_y = 750

time.sleep(3)

for a in range(0, 20):
    wait = random.random()+1
    pyautogui.moveTo(start_x, start_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait+2)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(open_x, open_y)
    time.sleep(wait+2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(wait+15)
    pyautogui.moveTo(close_x, close_y)
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
    time.sleep(2)