import requests

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.

def rooter(request):
    print(request.POST)
    data = "{\"heart_rate\": 77, \"humidty_level\": 88}"

    heart_rate = data.split(' ')[1]
    heart_rate = heart_rate.strip(',')
    humidty_level = data.split(' ')[3]
    humidty_level = humidty_level.strip('}')

    pattern = 0
    if 0 <= int(heart_rate) <= 32:
        pattern += 0
    elif 33 <= int(heart_rate) <= 66:
        pattern += 3
    else:
        pattern += 6

    if 0 <= int(humidty_level) <= 32 :
        pattern += 1
    elif 33 <= int(humidty_level) <= 66 :
        pattern += 2
    else:
        pattern += 3

    #url = "http://127.0.0.1:8000/"
    #requests.post(url, {"pattern": pattern})

    return render(request, 'sport_update/index.html', {"pattern": pattern, "heart_rate": heart_rate, "humidty_level": humidty_level})
