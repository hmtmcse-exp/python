from django.forms import ModelForm
from django.shortcuts import render, redirect

from django_crud.parent.ModelSaver import ModelSaver
from university.models import Department
from university.services.DepartmentService import DepartmentService


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']


def index(request):
    departments = DepartmentService.get_all()
    return render(request, 'university/department/index.html', {'departments': departments})


def create(request):
    return render(request, 'university/department/form.html', {'data':{}})


def save(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():

        # for key in request.POST:
        #     print(key)
        #     value = request.POST[key]
        #     print(value)

        data = ModelSaver(Department, request.POST)

        if data.is_valid():
            data.save()

        # department = Department()
        # setattr(department, "description", "Added")
        # setattr(department, "name", "name")
        #
        # response = department.save()
        # if response is None:
        #     print("Not saved")
        # else:
        #     print("Saved")
        return redirect('department_index')
    else:
        return redirect('department_index')


def update(request):
    return render(request, 'university/home.html')


def delete(request):
    return render(request, 'university/home.html')

