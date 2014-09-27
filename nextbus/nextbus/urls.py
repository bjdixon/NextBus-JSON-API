from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('nb_json_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
