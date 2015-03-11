from django.conf.urls import patterns, url

from trajectory import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='trajectory'),
    url(r'^partition', views.partition, name='partition'),
    url(r'^route', views.route, name='route'),
    url(r'^test', views.test, name='test'),
)
