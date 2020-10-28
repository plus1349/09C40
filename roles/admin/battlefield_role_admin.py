from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin, TabularInline

from roles.models import BattlefieldRole, BattlefieldRoleTranslation


class BattlefieldRoleTranslationInlineAdmin(TabularInline):
    model = BattlefieldRoleTranslation


@register(BattlefieldRole)
class BattlefieldRoleAdmin(ModelAdmin):
    inlines = (BattlefieldRoleTranslationInlineAdmin,)
    list_display = ("id", "title",)
    list_display_links = ("title",)
    list_per_page = 16
    ordering = ("id",)
    search_fields = ("title",)
