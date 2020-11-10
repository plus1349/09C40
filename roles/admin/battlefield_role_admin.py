from django.contrib.admin import register, ModelAdmin, TabularInline

from roles.models import BattlefieldRole, BattlefieldRoleTranslation


class BattlefieldRoleTranslationInlineAdmin(TabularInline):
    extra = 0
    model = BattlefieldRoleTranslation


@register(BattlefieldRole)
class BattlefieldRoleAdmin(ModelAdmin):
    inlines = (BattlefieldRoleTranslationInlineAdmin,)
    list_display = ("id", "title",)
    list_display_links = ("title",)
    list_per_page = 9
    ordering = ("id",)
    search_fields = ("title", "translations__title")

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.GET:
            queryset = queryset.order_by(*self.search_fields)
        return queryset, use_distinct
