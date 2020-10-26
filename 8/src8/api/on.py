import os
import requests

USERNAME = os.getenv("USERNAME")
IP = os.getenv("IP")
URL = f"http://{IP}/api/{USERNAME}/lights/1/state"

body = {
    "bri": 254,
    "on": True,
    "sat": 0
}

requests.put(URL, json=body)
