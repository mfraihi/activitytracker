from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'activitytracker.views.home', name='home'),
    url(r'^runtracker/', include('runtracker.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
