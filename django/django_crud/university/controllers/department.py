from django.contrib import messages
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
    data = ModelSaver(Department, request.POST)
    if data.is_valid():
        data.save()
        messages.success(request, "Successfully Created.")
        return redirect('department_index')
    else:
        messages.error(request, data.get_error_message())
        return redirect('department_index')


def update(request):
    return render(request, 'university/home.html')


def delete(request):
    return render(request, 'university/home.html')

