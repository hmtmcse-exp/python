import datetime

from django import template
from django.utils.html import format_html

register = template.Library()


def concat_static_url(url):
    return "/static/" + url


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
