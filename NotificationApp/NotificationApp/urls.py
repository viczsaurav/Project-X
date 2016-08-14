from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns(
	'',
    url(r'^$', 'NotificationApp.notifyApp.views.notify', name = 'notify'),
    url(r'^notify/', include('NotificationApp.notifyApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
