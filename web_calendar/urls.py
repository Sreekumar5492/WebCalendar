from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home/$', 'web_calendar.views.home', name='home'),
     url(r'^get_events/$','web_calendar.views.get_events', name='get_calendar')
    # url(r'^blog/', include('blog.urls')),

    
)
