from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the my index.")


def register(request):
    request.session["touhid"] = "mia";
    return HttpResponse("Hello Register")


def logout(request):
    del request.session["touhid"]
    return HttpResponse("Hello Logout")