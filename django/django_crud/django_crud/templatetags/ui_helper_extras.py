import datetime

from django import template
from django.utils.html import format_html

from django_crud.helper import SYSTEM_CONSTANT

register = template.Library()


def concat_static_url(url):
    return "/static/" + url


def number_between(n, start, end):
    if start <= n <= end:
        return True
    else:
        return False


def generate_pagination(total):
    loop = int(total / SYSTEM_CONSTANT.ITEMS_PER_PAGE)
    modulus = total % SYSTEM_CONSTANT.ITEMS_PER_PAGE
    html = '<ul class="pagination">'
    offset = 0
    limit = SYSTEM_CONSTANT.ITEMS_PER_PAGE
    n = 0
    for n in range(1, loop + 1):
        if number_between(n, offset, limit):
            html += '<li class="active"><a href="#">' + str(n) + '</a></li>'
        else:
            html += '<li><a href="?offset=' + str(offset) + '&limit=' + str(limit) + '">' + str(n) + '</a></li>'
        offset = offset + limit

    if modulus != 0:
        n += 1
        if number_between(n, offset, limit):
            html += '<li class="active"><a href="#">' + str(n) + '</a></li>'
        else:
            html += '<li><a href="?offset=' + str(offset) + '&limit=' + str(limit) + '">' + str(n) + '</a></li>'
    return html


@register.simple_tag
def load_css(file_name):
    url = concat_static_url("css/" + file_name)
    return format_html('<link rel="stylesheet" href="' + url + '">')


@register.simple_tag
def load_js(file_name):
    url = concat_static_url("js/" + file_name)
    return format_html('<script src="' + url + '"></script>')


@register.simple_tag
def image_url(file_name):
    url = concat_static_url("images/" + file_name)
    return url


@register.simple_tag(takes_context=True)
def make_pagination(context, toatal):
    request = context['request']
    return format_html(generate_pagination(toatal))


@register.simple_tag(takes_context=True)
def item_per_page(context):
    html = '<select class="form-control">'
    selected = SYSTEM_CONSTANT.ITEMS_PER_PAGE
    for item in [5, 10, 15, 25, 50, 100, 500]:
        if item == selected:
            html += '<option selected>' + str(item) + '</option>'
        else:
            html += '<option>' + str(item) + '</option>'
    html += '</select>'
    return format_html(html)


@register.simple_tag(takes_context=True)
def sortable_th(context, name):
    html = '<th><span class="glyphicon glyphicon-triangle-bottom"></span>  ' + name + '  <span class="glyphicon glyphicon-triangle-top"></span></th>'
    return format_html(html)