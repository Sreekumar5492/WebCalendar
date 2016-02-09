from django.contrib import admin
from web_calendar import models
# Register your models here.
admin.site.register(models.userprofile)
admin.site.register(models.events)