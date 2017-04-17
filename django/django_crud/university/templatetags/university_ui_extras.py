from django import template
from django.utils.html import format_html
from university.models import Department

register = template.Library()


@register.simple_tag
def department_drop_down(selected):
    html = '<select class="form-control apply-chosen" name="department" >'
    department_list = Department.objects.all()
    for item in department_list:
        if item.id == selected:
            html += '<option value="' + str(item.id) + '" selected>' + str(item.name) + '</option>'
        else:
            html += '<option value="' + str(item.id) + '">' + str(item.name) + '</option>'
    html += '</select>'
    return format_html(html)
