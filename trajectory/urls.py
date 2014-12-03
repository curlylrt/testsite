from django.conf.urls import patterns, url

from trajectory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
