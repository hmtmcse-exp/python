from django import template
from django.template import Context, Template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def test():
    return "Touhid"


@register.simple_tag
def html_template_context_tag():
    t = Template('<br> This is your <span>{{ message }}</span>.')
    c = Context({'message': 'Your message'})
    html = t.render(c)
    return html


@register.simple_tag
def html_tag():
    return format_html("<h1>Hello</h1>")