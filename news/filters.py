from django_filters.rest_framework import FilterSet, NumberFilter, CharFilter

from news.models import News


class NewsFilters(FilterSet):
    infolevel = NumberFilter(field_name="infolevel", lookup_expr="gte")
    category = CharFilter(field_name="category",)

    class Meta:
        model = News
        fields = ("infolevel", "category")
