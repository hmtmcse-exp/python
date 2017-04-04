from django.forms import ModelForm
from django.shortcuts import render, redirect

from university.models import Department
from university.services.DepartmentService import DepartmentService


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']


def index(request):
    departments = DepartmentService.get_all()
    return render(request, 'university/department/index.html', {'departments': departments})


def create(request):
    return render(request, 'university/department/form.html')


def save(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department_index')
    else:
        return redirect('department_index')


def update(request):
    return render(request, 'university/home.html')


def delete(request):
    return render(request, 'university/home.html')

