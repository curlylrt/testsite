from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^$', 'accounts.views.login', name='login'),
    url(r'^register$', 'accounts.views.register', name='register'),
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),
    url(r'^loggedin$', 'accounts.views.loggedin', name='loggedin'),
    url(r'^invalid_loggedin$', 'accounts.views.invalid_login', name='login'),
    url(r'^register_success$', 'accounts.views.register_success', name='register_success'),
)
