from django.conf.urls import url
from university.controllers import home

urlpatterns = [
    url(r'^', home.home, name='home'),
]