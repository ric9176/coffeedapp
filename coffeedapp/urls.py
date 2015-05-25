from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')),
)
