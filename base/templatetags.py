from django.conf import settings
from django.template.library import Library


register = Library()


@register.simple_tag(takes_context=True)
def languages(context):
    context['languages'] = settings.LANGUAGES
