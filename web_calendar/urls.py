from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^home/$', 'web_calendar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
)
