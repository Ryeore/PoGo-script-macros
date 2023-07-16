import cv2
import pyautogui
import numpy as np
import time

from PIL import ImageGrab

# Set variables
start_x = 1000
start_y = 400
close_x = 1140
close_y = 950
close = cv2.imread('templates/close.png')
closegift = cv2.imread('templates/closegift.png')
isgift = cv2.imread('templates/isgift.png')
addfriend = cv2.imread('templates/addfriend.png')
opengift = cv2.imread('templates/open.png')
reroll_receive = cv2.imread('templates/reroll_receive.png')
reroll_send = cv2.imread('templates/reroll_send.png')
refresh_receive = cv2.imread('templates/refresh_receive.png')
refresh_send = cv2.imread('templates/refresh_send.png')
sendgift = cv2.imread('templates/sendgift.png')
firstgift = cv2.imread('templates/firstgift.png')
pressend = cv2.imread('templates/send.png')
quitgift = cv2.imread('templates/quitgift.png')
bonus = cv2.imread('templates/bonus.png')


def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  # Adjust the threshold as needed
    if max_val >= threshold:
        return max_loc

    return None


def match_location(template):
    time.sleep(2)
    # Capture screenshot of the screen
    found = True
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


def click_refresh_receive():
    match_location(reroll_receive)


def click_refresh_send():
    match_location(reroll_send)


def click_reroll_receive():
    time.sleep(2)
    screenshot = np.array(ImageGrab.grab())
    location = template_match(screenshot, reroll_receive)
    refresh_x = location[0] + reroll_receive.shape[1] // 2
    refresh_y = location[1] + reroll_receive.shape[0] // 2
    time.sleep(1)
    pyautogui.moveTo(refresh_x, refresh_y)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)


def click_reroll_send():
    time.sleep(1)
    screenshot = np.array(ImageGrab.grab())
    location = template_match(screenshot, refresh_send)
    refresh_x = location[0] + refresh_send.shape[1] // 2
    refresh_y = location[1] + refresh_send.shape[0] // 2
    time.sleep(1)
    pyautogui.moveTo(refresh_x, refresh_y)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)


def refresh_receive_gift():
    click_refresh_receive()
    time.sleep(1)
    click_reroll_receive()


def refresh_send_gift():
    time.sleep(1)
    click_refresh_send()
    time.sleep(1)
    click_reroll_send()


def first_in_list():
    screenshot = np.array(ImageGrab.grab())
    location = template_match(screenshot, addfriend)
    click_x = location[0] + addfriend.shape[1] // 2
    click_y = location[1] + addfriend.shape[0] // 2
    pyautogui.click(click_x, click_y + 200)


# set how many gifts you can send or receive
gifts_available = 20

# what you want to do receive/send gifts
job = "send"

time.sleep(3)

if job == "receive":
    for a in range(0, gifts_available):
        check = True
        match_location(isgift)
        time.sleep(2)
        pyautogui.click(1000, 700)
        match_location(opengift)
        while check is True:
            screenshot = np.array(ImageGrab.grab())
            location = template_match(screenshot, close)
            if location is not None:
                # Template disappeared, return
                check = False
        match_location(close)
        time.sleep(2)
        print(f"Gifts received: {a+1}")
        refresh_receive_gift()

if job == "send":
    for a in range(0, gifts_available):
        first_in_list()
        match_location(closegift)
        time.sleep(2)
        if template_match(np.array(ImageGrab.grab()), opengift):
            match_location(quitgift)
        if template_match(np.array(ImageGrab.grab()), bonus):
            match_location(close)
        match_location(sendgift)
        match_location(firstgift)
        match_location(pressend)
        match_location(close)
        refresh_send_gift()
