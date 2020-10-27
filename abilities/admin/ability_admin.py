from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from abilities.models import Ability


@register(Ability)
class AbilityAdmin(ModelAdmin):
    fields = ("title", "description",)
    list_display = ("id", "title",)
    list_display_links = ("title",)
    list_per_page = 16
    ordering = ("id",)
    search_fields = ("title",)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if request.GET:
            queryset = queryset.order_by("title")
        return queryset, use_distinct
