from django_filters import FilterSet, DateFilter #ModelChoiceFilter
from .models import Product, News_All
from django.forms import DateInput
# from .models import Material
class ProductFilter(FilterSet):
    # material = ModelChoiceFilter(
    #     filter_name = 'productmaterial__material',
    #     queryset= Material.objects.all(),
    #     label = 'Material',
    #     empty_label = 'Любой'
    # )
    class Meta:
        model = Product
        fields = {
            # 'productmaterial__material': ['exact'],
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': [
                'lt',
                'gt',
            ]
        }


class NewsFilter(FilterSet):
    time_in=DateFilter(
    field_name = 'time_in',
    widget = DateInput(attrs={'type':'date'}),
    label= 'Дата',
    lookup_expr = 'date__gte',
    )
    class Meta:
        model = News_All
        fields = {
            # 'productmaterial__material': ['exact'],
            'name': ['icontains'],
            'text': ['icontains'],
            # 'time_in': ['day__gt', 'month__gt', 'year__gt']

        }