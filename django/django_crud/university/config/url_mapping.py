from django.conf.urls import url

from university.controllers import course, department
from university.controllers import home
from university.services import URL_CONSTANT

urlpatterns = [
    url(r'^' + URL_CONSTANT.COURSE_CREATE, course.create, name='course_create'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE, course.update, name='course_update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE, course.delete, name='course_delete'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX, course.index, name='course_index'),

    url(r'^' + URL_CONSTANT.DEPARTMENT_CREATE + "?$", department.create, name='department_create'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_SAVE + "?$", department.save, name='department_save'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_UPDATE, department.update, name='department_update'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_DELETE, department.delete, name='department_delete'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX + "?$", department.index, name='department_index'),

    url(r'^' + URL_CONSTANT.HOME_INDEX, home.home, name='home'),
]
