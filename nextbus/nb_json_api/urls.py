from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
        url(r'^agency_list/$', 'nb_json_api.views.view_agency_list', name='agency_list'),
)

