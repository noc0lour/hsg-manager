from django.conf.urls import url, include
from django.conf import settings

from . import views

group_patterns = [
    url(r'details/(?P<pk>[0-9]+)$', views.detail_view, name='group-detail'),
    url(r'register/(?P<pk>[0-9]+)$', views.detail_view, name='group-register'),
]

urlpatterns = [
    url(r'^$', views.all_hsgs),
    url(r'^all/$', views.all_hsgs, name='group-all'),
    url(r'^list/([0-9]{4})/$', views.list_year, name='group-year'),
    url(r'^group/', include(group_patterns)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': "hsg/static/css/"}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': "hsg/static/js/"}),
    url(r'^pdfgen/(?P<registration_id>[0-9]+)$', views.gen_reg)
]
