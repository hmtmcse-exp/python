from django.shortcuts import render


def index(request):
    return render(request, 'university/home.html')


def create(request):
    return render(request, 'university/form.html')


def update(request):
    return render(request, 'university/home.html')


def delete(request):
    return render(request, 'university/home.html')
