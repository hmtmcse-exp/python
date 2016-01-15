from django.shortcuts import render
from django.http import Http404

from crud.models import Crud


def index(request):
    crudList = Crud.objects.all()
    return render(request, 'crud/index.html', {
        'items': crudList,
    })


def item_detail(request, id):
    try:
        item = Crud.objects.get(id=id)
    except Crud.DoesNotExist:
        raise Http404('This item does not exist')
    return render(request, 'crud/crud_detail.html', {
        'item': item,
    })
