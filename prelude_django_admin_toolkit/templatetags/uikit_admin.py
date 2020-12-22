# Using example inspired on the github below: Thanks!
# https://github.com/nathanbigaignon/django-uikit-admin/blob/master/uikit_admin/templatetags/uikit_admin.py

from django import template
from django.forms.boundfield import BoundField
from django.utils.html import format_html

from django.forms.widgets import Select
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

register = template.Library()


@register.simple_tag
def uka_form_row_stacked(element, errors='', extra_classes=''):
    label = BoundField.label_tag(element, "", {'class': 'uk-form-label'}, label_suffix='')
    
    if errors:
        extra_classes = f'{extra_classes} uk-form-danger uk-clearfix'
    
    # Trying to infer if I'm dealing with a select
    
    uk_select = ''
    if issubclass(element.field.widget.__class__, Select):
        uk_select = ' uk-select'
    
    if issubclass(element.field.widget.__class__, RelatedFieldWidgetWrapper):
        uk_select = ' uk-select'
    
    element = element.as_widget(attrs={'class': f'uk-input {extra_classes}{uk_select}'})
    
    html_error = format_html(f'<div class="uk-text-danger uk-margin-top">{errors}</div>')
    
    html = format_html(f'<div class="uk-form-row"><div>{label} {html_error}</div>'
                       f'<div class="uk-form-controls">{element}</div></div>')
    return html

@register.simple_tag
def uk_element (element, class_override=None):
    element = element.as_widget(attrs={'class': 'uk-input' if class_override is None else class_override })
    
    return format_html(element)
    

@register.simple_tag
def uka_form_row_stacked_button(text, classes=None):
    if classes is None:
        classes = ''
    html = format_html(
        '<div class="uk-form-row"><div class="uk-form-controls"><button class="uk-button {}">{}</button></div></div>',
        classes, text)
    return html


@register.simple_tag
def uka_button(text, classes=None, type_name=None, name=None):
    if classes is None:
        classes = ''
    if type_name is None:
        type_name = ''
    if name is None:
        name = ''
    html = format_html(
        '<button class="uk-button {}" type="{}" name="{}">{}</button>',
        classes, type, name, text)
    return html


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})