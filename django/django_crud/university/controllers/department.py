from django.contrib import messages
from django.shortcuts import render, redirect
from django_crud.helper.ModelSaver import ModelSaver
from django_crud.helper.TmpMemory import TmpMemory
from university.models import Department
from university.services.DepartmentService import DepartmentService


def index(request):
    departments = DepartmentService.get_all()
    return render(request, 'university/department/index.html', {'departments': departments})


def create(request):
    return render(request, 'university/department/create.html', {'data': TmpMemory.get_redirect_tmp()})


def save(request):
    data = ModelSaver(Department, request.POST)
    if data.is_valid():
        data.save()
        messages.success(request, "Successfully Created.")
        return redirect('department_index')
    else:
        messages.error(request, data.get_error_message())
        TmpMemory.set_redirect_tmp(request.POST)
        return redirect('department_create')


def update(request):
    return render(request, 'university/home.html')


def delete(request):
    return render(request, 'university/home.html')

