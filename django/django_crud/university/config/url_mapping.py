from django.conf.urls import url

from university.controllers import course
from university.controllers import home
from university.services import URL_CONSTANT

urlpatterns = [
    url(r'^' + URL_CONSTANT.COURSE_CREATE, course.create, name='create'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE, course.update, name='update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE, course.delete, name='delete'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX, course.index, name='index'),
    url(r'^' + URL_CONSTANT.HOME_INDEX, home.home, name='home'),
]
