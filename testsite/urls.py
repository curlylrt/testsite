from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^places/', include('places.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trajectory/', include('trajectory.urls')),
)
