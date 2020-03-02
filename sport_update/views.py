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

    dict = {
        "pattern": pattern,
        "heart_rate": heart_rate,
        "humidty_level": humidty_level
    }

    return render(request, 'sport_update/index.html', dict)
