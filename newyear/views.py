import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request,'newyear/index.html', {
        "newyear": now.month ==1 and now.day == 1,
        "title": 'Good evening, my sleepy user' if now.hour >= 20 or now.hour <= 6  else 'Good day, my happy user'
        })