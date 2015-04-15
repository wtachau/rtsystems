from django.conf.urls import patterns, include, url
from django.contrib import admin
from home_page_app.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'home_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home),
    url(r'^service$', about),
    url(r'^whoweare', whoweare),
    url(r'^contact$', contact),
    url(r'^contactus$', contactus)
)
