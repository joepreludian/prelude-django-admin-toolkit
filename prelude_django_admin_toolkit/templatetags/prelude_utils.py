from django import template


register = template.Library()

@register.simple_tag
def full_url_without_tags(request, *args):
    """Removes all values of arg from the given string"""

    full_path = request.get_full_path  # @todo work with todopart

    request.GET.pop('q')
    
    return request.get_full_path()