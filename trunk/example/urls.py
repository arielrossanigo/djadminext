from django.conf.urls.defaults import *
from DjAdminExt.views import master_detail
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^MasterDetailCombo/(\d+)/(\w+)/(\w+)/(\w+)/(\w+)/$', master_detail),
)
