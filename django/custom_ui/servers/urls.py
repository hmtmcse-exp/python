from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.server_list, name='server_list'),
    url(r'^new$', views.server_create, name='server_new'),
    url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
    url(r'^touhid/', views.touhid_mia, name='touhid_mia'),
    url(r'^message/', views.message, name='message'),
    url(r'^message2/', views.message2, name='message2'),
]