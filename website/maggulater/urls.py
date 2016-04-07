from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^result/(?P<author_id>[0-9]+)/$', views.result , name = 'result'),
	url(r'^getallauthors/$', views.getallauthors, name = 'getallauthors'),
	url(r'^getresult/$', views.getresult, name = 'getresult'),
	url(r'^getid/$', views.getid, name = 'getid'),
	url(r'^$', views.home, name = 'home'),
]
