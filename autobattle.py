import cv2
import pyautogui
import numpy as np
import time

from PIL import ImageGrab

battle = cv2.imread('templates/battle.png')
great = cv2.imread('templates/great.png')
party = cv2.imread('templates/party.png')
exit_battle = cv2.imread('templates/exit.png')
yes = cv2.imread('templates/yes.png')
vs = cv2.imread('templates/vs.png')
next_battle = cv2.imread('templates/next_battle.png')
passed = cv2.imread('templates/pass.png')
letsgo = cv2.imread('templates/letsgo.png')
claim = cv2.imread('templates/claim.png')
ultra = cv2.imread('templates/ultra.png')


def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.6  # Adjust the threshold as needed
    if max_val >= threshold:
        return max_loc

    return None


def match_location(template):
    time.sleep(2)
    # Capture screenshot of the screen
    screenshot = np.array(ImageGrab.grab())
    # Find the location of the template match
    location = template_match(screenshot, template)
    # Calculate the coordinates to click on
    click_x = location[0] + template.shape[1] // 2
    click_y = location[1] + template.shape[0] // 2
    # Click on the element
    pyautogui.moveTo(click_x, click_y)
    time.sleep(0.5)
    pyautogui.click()


def wait_for_fight():
    while True:
        position = pyautogui.locateOnScreen(vs)
        if position is None:
            # Template disappeared, return
            return


def exit_fight():
    while True:
        position = pyautogui.locateOnScreen(exit_battle)
        if position is not None:
            # Template disappeared, return
            return


for a in range(0, 3):
    check = True
    wait_vs = True
    print(f"Starting {a + 1} battle")
    print("Starting new battle")
    match_location(battle)
    # if a % 5 == 0:
    #     match_location(letsgo)
    print("Battle entered")
    match_location(ultra)
    print("League selected")
    match_location(party)
    print("Party selected")
    time.sleep(1)
    while wait_vs is True:
        screenshot = np.array(ImageGrab.grab())
        location = template_match(screenshot, vs)
        if location is None:
            # Template disappeared, return
            wait_vs = False
    while check is True:
        # pys
        pyautogui.moveTo(770, 170)
        # pysia
        # pyautogui.moveTo(760, 210)
        time.sleep(0.1)
        pyautogui.click()
        # pys
        pyautogui.moveTo(940, 540)
        # pysia
        # pyautogui.moveTo(1000, 550)
        time.sleep(0.1)
        pyautogui.click()
        screenshot = np.array(ImageGrab.grab())
        location = template_match(screenshot, battle)
        location2 = template_match(screenshot, passed)
        loc3 = template_match(screenshot, claim)
        if location is not None:
            check = False
        if location2 is not None:
            match_location(passed)
            check = False
        if loc3 is not None:
            check = False
    print("Battle finished")
    time.sleep(10)
