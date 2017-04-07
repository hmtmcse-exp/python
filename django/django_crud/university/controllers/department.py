from django.contrib import messages
from django.shortcuts import render, redirect
from django_crud.helper.CRUDHelper import CRUDHelper
from django_crud.helper.TmpMemory import TmpMemory
from university.models import Department
from university.services import URL_CONSTANT


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
    data = TmpMemory.get_redirect_tmp()
    if data is None:
        crud_helper = CRUDHelper(Department)
        data = crud_helper.get_by_id(pk)
    return render(request, 'university/department/edit.html', {"data": data})


def details(request, pk):
    crud_helper = CRUDHelper(Department)
    data = crud_helper.get_by_id(pk)
    if data is None:
        messages.error(request, "Invalid Recored.")
        return redirect('department_index')
    return render(request, 'university/department/details.html', {"data": data})


def update(request):
    data = CRUDHelper(Department, request.POST)
    if data.is_valid():
        data.save()
        messages.success(request, "Successfully Updated.")
        return redirect('department_index')
    else:
        messages.error(request, data.get_error_message())
        TmpMemory.set_redirect_tmp(request.POST)
        return redirect("/" + URL_CONSTANT.DEPARTMENT_EDIT + "0")


def delete(request, pk):
    crud_helper = CRUDHelper(Department)
    is_deleted = crud_helper.delete_by_id(pk)
    if is_deleted:
        messages.success(request, "Successfully Deleted.")
        return redirect('department_index')
    else:
        messages.error(request, crud_helper.get_error_message())
        return redirect('department_index')


