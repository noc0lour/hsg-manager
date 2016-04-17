from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hsg/', include('hsg.urls', namespace='hsg', app_name='hsg')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
