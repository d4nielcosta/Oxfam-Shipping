from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteer import views

urlpatterns = patterns('',
                       url(r'^volunteer/', include('volunteer.urls')),
                       url(r'^manager/', include('manager.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', views.index, name='index'),

                       )
