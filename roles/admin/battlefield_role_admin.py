from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from roles.models import BattlefieldRole


@register(BattlefieldRole)
class BattlefieldRoleAdmin(ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("title",)
    list_per_page = 16
    ordering = ("id",)
    search_fields = ("title",)
