from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt
from web_calendar.models import *
import json

# Create your views here.
@login_required
def home(request):
    return render(request,'web_calendar/home.html')
@login_required
@csrf_exempt
def get_events(request):
    user = request.user
    events_all = events.objects.filter(user=user).values('name','start','end','allday')
    args = []
    for event in events_all:
        name = event['name']
        start = event['start'].strftime('%Y-%m-%dT%H:%M:%S')
        end  = event['end'].strftime('%Y-%m-%dT%H:%M:%S')
        allday = event['allday']
        eventdict = {'name':name,
                    'start':start,
                    'end':end,
                    'allday':allday
        }
        args.append(eventdict)
    return HttpResponse(json.dumps(args))