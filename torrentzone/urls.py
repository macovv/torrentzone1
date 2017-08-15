from django.conf.urls import  include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^create/', views.create, name="create"),
    url(r'^delete_torrent/(?P<pk>\d+)/$', views.delete_torrent, name='delete_torrent'),
    url(r'^torrent_details/(?P<pk>\d+)/$', views.torrent_details, name='torrent_details'),
    url(r'^about/', views.about, name ='about'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
