from django.conf.urls import patterns, url

from instance import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<VirtualMachine_id>\d+)/$', views.detail, name='detail'),
)
