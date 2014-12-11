from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('menu.urls')),
    url(r'^places/', include('places.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^trajectory/', include('trajectory.urls')),
) #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
