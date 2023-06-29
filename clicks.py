import pyautogui

# Example coordinates (change these according to your needs)
#770,170
start_x = 940
start_y = 540

# Move the mouse to the specified coordinates
# pyautogui.moveTo(760, 210)

# Perform a left click
# pyautogui.click()

import re

def extract_matching_strings(text):
    pattern = r'\b\d{4}\d{4}\d{4}\b'
    matches = re.findall(pattern, text)
    return matches

# Example usage
text = "Lorem ipsum 123412341234 dolor sit amet, consectetur adipiscing 5678 5678 5678 elit."

matching_strings = extract_matching_strings(text)

print("Matching strings:", matching_strings)