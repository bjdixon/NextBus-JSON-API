from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^agency_list/$', 'nb_json_api.views.view_agency_list', name='agency_list'),
        url(r'^routes_list/(?P<agency_id>[-\w]+)/$', 'nb_json_api.views.view_routes_list', name='routes_list'),
        url(r'^stops_list/(?P<agency_id>[-\w]+)/(?P<route_number>\w+)/$', 'nb_json_api.views.view_stops_list', name='stops_list'),
        url(r'^predictions/(?P<agency_id>[-\w]+)/(?P<route_number>\w+)/(?P<stop_id>\d+)/$', 'nb_json_api.views.view_predictions', name='predictions'),
)

