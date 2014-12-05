from django.conf.urls import patterns, url

from trajectory import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^partition', views.partition, name='partition'),
)
