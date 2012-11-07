from django.conf.urls.defaults import *
from django.conf import settings
from web.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'web.views.beranda', {'page': 'static/beranda.html'}),
    (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'media'}),
    (r'^admin/', include(admin.site.urls)),
)
