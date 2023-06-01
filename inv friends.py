import time

import pyautogui
import random
import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://pokemongo.gishan.net/friends/codes/"  # Replace with the URL of the website you want to scrape
lista = []
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the <strong> tags
strong_tags = soup.find_all("strong")

# Extract the text within the <strong> tags
strong_text = [tag.get_text() for tag in strong_tags]

# Print the extracted text
for text in strong_text:
    text = text.replace(" ", "")
    if text == "Thereareongoingraids!":
        print("header skip")
    else:
        lista.append(text)

print(lista)


time.sleep(3)

# Example coordinates (change these according to your needs)
add_friend_X = 890
add_friend_Y = 240
insert_code_x = 900
insert_code_y = 600
send_inv_x = 980
send_inv_y = 400
confirm_inv_x = 1000
confirm_inv_y = 450
# Move the mouse to the specified coordinates
pyautogui.moveTo(add_friend_X, add_friend_Y)
# Perform a left click
pyautogui.click()
wait = random.random()+3

for code in lista:
    time.sleep(wait)
    pyautogui.moveTo(insert_code_x, insert_code_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    #loop for entering code
    for num in code:
        waits = random.random()
        pyautogui.press(num)
        time.sleep(waits)
    time.sleep(wait)
    pyautogui.moveTo(send_inv_x, send_inv_y)
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(confirm_inv_x, confirm_inv_y)
    pyautogui.click()
    time.sleep(wait)
    pyautogui.moveTo(1000, 550)
    pyautogui.click()
    time.sleep(wait)


