import cv2
import pyautogui
import numpy as np
import time
import random
from pynput.keyboard import Controller
from PIL import ImageGrab

keyboard = Controller()


def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.6  # Adjust the threshold as needed
    if max_val >= threshold:
        return max_loc

    return None


def match_location(temp):
    template = cv2.imread(f'templates/{temp}.png')
    found = True
    time.sleep(1)
    while found:
        screenshot = np.array(ImageGrab.grab())
        location = template_match(screenshot, template)
        if location is not None:
            click_x = location[0] + template.shape[1] // 2
            click_y = location[1] + template.shape[0] // 2
            pyautogui.moveTo(click_x, click_y)
            time.sleep(0.1)
            pyautogui.click()
            found = False



'''
1. Click on buddy bottom left
2. Click play
3. Click OK
4. Click photo
This x3:
    4.1 Click berry
    4.2 Select berry
    4.3 Swipe berry up
5. Exit
6. Press X to exit photo
7. Click on buddy bottom left
8. Swipe down to "Swap Buddy"
9. Click Swap Buddy
10. Confirm with YES
11. Click on search bar
12. Input Bud{x}
13. Select buddy
14. Close
'''


def open_buddy_page():
    buddy_x = 835
    buddy_y = 915
    pyautogui.moveTo(buddy_x, buddy_y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()


def swipe_down():
    time.sleep(1)
    swipe_x = 940
    swipe_start_y = 500
    pyautogui.moveTo(swipe_x, swipe_start_y)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    for val in range(500, 200, -20):
        pyautogui.moveTo(swipe_x, val)
    # pyautogui.moveTo(swipe_x, swipe_end_y)
    time.sleep(0.5)
    pyautogui.mouseUp()


def select_buddy():
    buddy_x = 810
    buddy_y = 330
    pyautogui.moveTo(buddy_x, buddy_y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()


def select_buddy_for_battle():
    buddy_x = 820
    buddy_y = 450
    pyautogui.moveTo(buddy_x, buddy_y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()


def search_and_select(buddy_x):
    match_location("search")
    time.sleep(2)
    keyboard.type(buddy_x)
    select_buddy()


def search_and_select_for_battle(buddy_x):
    match_location("search")
    time.sleep(2)
    keyboard.type(buddy_x)
    select_buddy_for_battle()


def throw_candy():
    time.sleep(1)
    swipe_x = 940
    swipe_start_y = 600
    pyautogui.moveTo(swipe_x, swipe_start_y)
    time.sleep(0.5)
    pyautogui.mouseDown()
    time.sleep(0.5)
    for val in range(600, 200, -50):
        pyautogui.moveTo(swipe_x, val)
    # pyautogui.moveTo(swipe_x, swipe_end_y)
    pyautogui.mouseUp()


def play():
    time.sleep(2)
    match_location("ok")
    time.sleep(5)
    match_location("camera")
    match_location("candy")
    for a in range(0, 3):
        time.sleep(2)
        screenshot = np.array(ImageGrab.grab())
        location = template_match(screenshot, cv2.imread('templates/banana.png'))
        if location is not None:
            match_location("banana")
        else:
            match_location("berry")
        throw_candy()
        time.sleep(5)
    time.sleep(8)
    match_location("leave_buddy")
    time.sleep(1)
    match_location("quitbuddy")


def heart_program(buddy):
    open_buddy_page()
    swipe_down()
    match_location("swapbuddies")
    match_location("yes")
    search_and_select(buddy)
    time.sleep(10)
    match_location("play")
    play()


def trainer_battle(buddy):
    trainers = ["blanche", "candela", "spark"]
    enter_battle = cv2.imread('templates/enter_battle.png')
    while template_match(np.array(ImageGrab.grab()), enter_battle) is None:
        match_location("main_screen")
        time.sleep(5)
    time.sleep(1)
    match_location("enter_battle")
    for i in range(0, 5):
        swipe_down()
    for trainer in trainers:
        check_for_battle_over = True
        match_location(trainer)
        match_location("train")
        match_location("mleague")
        if trainer == "blanche":
            time.sleep(0.5)
            pyautogui.moveTo(820, 720)
            time.sleep(0.5)
            pyautogui.click()
            search_and_select_for_battle(buddy)
            match_location("done")
        match_location("party")
        while check_for_battle_over:
            screenshot = np.array(ImageGrab.grab())
            location = template_match(screenshot, cv2.imread('templates/pass.png'))
            time.sleep(10)
            if location is not None:
                check_for_battle_over = False
                match_location("pass")
    match_location("close")


# MAIN PROGRAM

for number in range(15, 31):
    selected_buddy = f'bud{number}'
    print(f"Current buddy: {selected_buddy}")
    time.sleep(2)
    heart_program(selected_buddy)
    time.sleep(5)
    trainer_battle(selected_buddy)
