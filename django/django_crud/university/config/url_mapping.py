from django.conf.urls import url

from university.controllers import course, department
from university.controllers import home
from university.controllers.StudentController import StudentController
from university.services import URL_CONSTANT

urlpatterns = [
    url(r'^' + URL_CONSTANT.COURSE_CREATE, StudentController.instance().create(), name='create'),
    url(r'^' + URL_CONSTANT.COURSE_UPDATE, course.update, name='update'),
    url(r'^' + URL_CONSTANT.COURSE_DELETE, course.delete, name='delete'),
    url(r'^' + URL_CONSTANT.COURSE_INDEX, course.index, name='index'),

    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX, department.create, name='create'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX, department.update, name='update'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX, department.delete, name='delete'),
    url(r'^' + URL_CONSTANT.DEPARTMENT_INDEX, department.index, name='index'),

    url(r'^' + URL_CONSTANT.HOME_INDEX, home.home, name='home'),
]
