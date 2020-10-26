import json
import os
import requests
import time

USERNAME = os.getenv("USERNAME")
IP = os.getenv("IP")
URL = f"http://{IP}/api/{USERNAME}/lights/1/state"

on = {
    "on": True,
    "bri": 254,
}

off = {
    "on": False
}

while True:
    requests.put(URL, data=json.dumps(on))
    time.sleep(1)
    requests.put(URL, data=json.dumps(off))
    time.sleep(1)
