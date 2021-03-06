from django_filters import rest_framework as filters

from career.models import Career


class CareerFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Career
        fields = ["name", "remote", "office", "relocation", "direction", "country"]
