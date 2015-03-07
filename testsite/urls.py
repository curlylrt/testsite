from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from adminplus.sites import AdminSitePlus

#old = admin.site
admin.site= AdminSitePlus()
#admin.site._registry = copy.copy(old._registry)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('index.urls')),
    url(r'^menu$', include('menu.urls')),
    url(r'^places/', include('places.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trajectory/', include('trajectory.urls')),
    url(r'^accounts/', include('accounts.urls')),
)
