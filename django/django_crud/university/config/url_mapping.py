from django.conf.urls import url

from university.controllers import course, department, student
from university.controllers import home
from university.services import URL_CONSTANT

urlpatterns = [
    url(r'^' + URL_CONSTANT.COURSE_CREATE, course.create, name='course_create'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE, course.update, name='course_update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE, course.delete, name='course_delete'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX, course.index, name='course_index'),

    url(r'^' + URL_CONSTANT.DEPARTMENT_EDIT + "(?P<pk>\d+)/?$", department.edit, name='department_edit'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_CREATE + "?$", department.create, name='department_create'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_SAVE + "?$", department.save, name='department_save'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_UPDATE + "?$", department.update, name='department_update'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_DELETE + "(?P<pk>\d+)/?$", department.delete, name='department_delete'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_DETAILS + "(?P<pk>\d+)/?$", department.details, name='department_details'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX + "?$", department.index, name='department_index'),

    url(r'^' + URL_CONSTANT.STUDENT_EDIT + "(?P<pk>\d+)/?$", student.edit, name='student_edit'),
    url(r'^' + URL_CONSTANT.STUDENT_CREATE + "?$", student.create, name='student_create'),
    url(r'^' + URL_CONSTANT.STUDENT_SAVE + "?$", student.save, name='student_save'),
    url(r'^' + URL_CONSTANT.STUDENT_UPDATE + "?$", student.update, name='student_update'),
    url(r'^' + URL_CONSTANT.STUDENT_DELETE + "(?P<pk>\d+)/?$", student.delete, name='student_delete'),
    url(r'^' + URL_CONSTANT.STUDENT_DETAILS + "(?P<pk>\d+)/?$", student.details, name='student_details'),
    url(r'^' + URL_CONSTANT.STUDENT_INDEX + "?$", student.index, name='student_index'),

    url(r'^' + URL_CONSTANT.COURSE_EDIT + "(?P<pk>\d+)/?$", course.edit, name='course_edit'),
    url(r'^' + URL_CONSTANT.COURSE_CREATE + "?$", course.create, name='course_create'),
    url(r'^' + URL_CONSTANT.COURSE_SAVE + "?$", course.save, name='course_save'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE + "?$", course.update, name='course_update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE + "(?P<pk>\d+)/?$", course.delete, name='course_delete'),
    url(r'^' + URL_CONSTANT.COURSE_DETAILS + "(?P<pk>\d+)/?$", course.details, name='course_details'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX + "?$", course.index, name='course_index'),


    url(r'^' + URL_CONSTANT.HOME_INDEX, home.home, name='home'),
]
