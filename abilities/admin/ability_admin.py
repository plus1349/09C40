from django.contrib.admin import register, ModelAdmin

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
            queryset = queryset.order_by(*self.search_fields)
        return queryset, use_distinct
