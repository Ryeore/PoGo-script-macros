import requests
import json
import re

def extract_matching_strings(text):
    pattern = r'\b\d{4} \d{4} \d{4}\b'
    # pattern = r'\b\d{4}\d{4}\d{4}\b'
    matches = re.findall(pattern, text)
    return matches

def retrieve_messages(channelid):
    headers = {
        "authorization": "MjQ2NzA0MzcyODI4OTk1NTk0.Gt68FV.iyZ97z7mNnXGe83YXVhjWU32TMjdHNSYgYKzmM"
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    json_object = json.loads(r.text)
    for value in json_object:
        # message = value['content']
        # print(extract_matching_strings(message))
        print(value['content'], '\n')


retrieve_messages(459446258411503616


