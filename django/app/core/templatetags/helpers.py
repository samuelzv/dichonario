from django import template
from django.urls import reverse

from pattern_library.monkey_utils import override_tag

register = template.Library()


# to be deleted
@register.simple_tag
def get_url(button):
    return reverse(button["url"]) + "?action=" + button["id"]


override_tag(register, "get_url", "")
