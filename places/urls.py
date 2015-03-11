from django.conf.urls import patterns, url

from places import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='places'),
    url(r'^(?P<place_id>\d+)/$', views.detail, name='detail'),
    )
