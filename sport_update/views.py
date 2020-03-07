import requests

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.

def rooter(request):
    print(request.POST)
    data = request.POST.get('data')
    print(data)

    heart_rate = data.split(' ')[1]
    heart_rate = heart_rate.strip(',')
    humidty_level = data.split(' ')[3]
    humidty_level = humidty_level.strip('}')

    print(heart_rate)
    print(humidty_level)

    pattern = 0
    if 60 <= int(heart_rate) <= 80:
        pattern += 0
    elif 81 <= int(heart_rate) <= 130:
        pattern += 2
    elif 131 <= int(heart_rate) <= 200:
        pattern += 4

    if 0 <= int(humidty_level) <= 55 :
        pattern += 1
    elif 56 <= int(humidty_level) <= 90 :
        pattern += 2


    if not pattern == 0:
        url = "https://5f52fbf7.ngrok.io/arduino/" + str(pattern)
        requests.get(url)

    dict = {
        "pattern": pattern,
        "heart_rate": heart_rate,
        "humidty_level": humidty_level
    }

    return render(request, 'sport_update/index.html', dict)


def playerSelect(request):
    print(request.POST)
    data = request.POST.get('data')

    return render(request, 'sport_update/select.html')
