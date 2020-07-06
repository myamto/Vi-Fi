# -*- coding: utf-8 -*-
import requests
heart_rate="190"
humidty_level="58"

pattern = 0
if 60 <= int(heart_rate) <= 80:
    pattern = 1
elif 81 <= int(heart_rate) <= 130:
    pattern = 2
elif 131 <= int(heart_rate) <= 200:
    pattern = 4
elif int(heart_rate) < 60 or int(heart_rate) > 190:
    pattern = 0

if pattern == 2 and 56 <= int(humidty_level) <= 90:
    pattern = 3


url = "http://184a4a286849.ngrok.io/arduino/" + str(pattern)
response=requests.get(url)

print(response)
