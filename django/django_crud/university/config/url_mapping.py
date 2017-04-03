from django.conf.urls import url

from university.controllers import course
from university.controllers import home
from university.services import URL_CONSTANT

urlpatterns = [
    url(r'^', home.home, name='home'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX, course.index, name='index'),
    url(r'^' + URL_CONSTANT.COURSE_CREATE, course.create, name='create'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE, course.update, name='update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE, course.delete, name='delete'),
]