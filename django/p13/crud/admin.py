from django.contrib import admin

from crud.models import Crud


class CrudAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
admin.site.register(Crud, CrudAdmin)
