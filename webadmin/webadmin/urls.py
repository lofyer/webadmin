from django.conf.urls import patterns, include, url
from django.contrib import admin

import xadmin
xadmin.autodiscover()

from webadmin import views as views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^', views.index),
    url(r'^xadmin/', include(xadmin.site.urls)),
    # url(r'^', include(xadmin.site.urls)),
    # url(r'^', include(xadmin.site.urls)),
)
