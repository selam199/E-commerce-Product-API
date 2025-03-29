import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = django_filters.CharFilter(field_name="category", lookup_expr="iexact")
    stock_available = django_filters.BooleanFilter(method='filter_stock')

    class Meta:
        model = Product
        fields = ['category', 'price_min', 'price_max', 'stock_available','name','description','created_by','price']

    def filter_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0)
        return queryset