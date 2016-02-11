from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Test.views.home', name='home'),
                        url(r'^web_calendar/', include('web_calendar.urls')),
                       url(r'^$', 'login.views.login', name='login'),
                       url(r'^loginuser/$', 'login.views.loginuser', name='loginuser'),
                       url(r'^logoutuser/$','login.views.logoutuser',name='logoutuser'),
                       url(r'^signup/$','login.views.signup',name='signup'),
                       url(r'^user_available/$','login.views.user_available',name='user_available'),

)
