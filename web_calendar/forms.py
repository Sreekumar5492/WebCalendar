#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from django.forms import ModelForm
from web_calendar.models import userprofile
from web_calendar.models import events

class userprofileform(ModelForm):
    class Meta:
        model = userprofile
        fields =['name','email']
        
class eventsform(ModelForm):
    class Meta:
        model = events
        exclude =['Location','Location_lat','Location_long']