from django.contrib import messages
from django.shortcuts import render, redirect
from django_crud.helper.CRUDHelper import CRUDHelper
from django_crud.helper.TmpMemory import TmpMemory
from university.models import Department


def index(request):
    crud_helper = CRUDHelper(Department, request.GET)
    departments = crud_helper.get_list()
    total_count = crud_helper.get_total()
    return render(request, 'university/department/index.html', {'departments': departments, 'total_count': total_count})


def create(request):
    return render(request, 'university/department/create.html', {'data': TmpMemory.get_redirect_tmp()})


def save(request):
    data = CRUDHelper(Department, request.POST)
    if data.is_valid():
        data.save()
        messages.success(request, "Successfully Created.")
        return redirect('department_index')
    else:
        messages.error(request, data.get_error_message())
        TmpMemory.set_redirect_tmp(request.POST)
        return redirect('department_create')


def edit(request, pk):
    crud_helper = CRUDHelper(Department)
    data = crud_helper.get_by_id(pk)
    return render(request, 'university/department/edit.html', {"data": data})


def update(request):
    data = CRUDHelper(Department, request.POST)
    if data.is_valid():
        data.save()
        messages.success(request, "Successfully Updated.")
        return redirect('department_index')
    else:
        messages.error(request, data.get_error_message())
        TmpMemory.set_redirect_tmp(request.POST)
        return redirect('department_edit')


def delete(request):
    return render(request, 'university/home.html')

