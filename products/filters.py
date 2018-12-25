from django_filters import FilterSet, ModelChoiceFilter
from .widgets import CustomLinkWidget
from .models import Product, SubCategory


class ProductFilter(FilterSet):
    subcategory = ModelChoiceFilter(widget=CustomLinkWidget(attrs={'class': 'subcat-text d-flex flex-column'}))

    def __init__(self, *args, **kwargs):
        category_id = kwargs.pop('category_id', None)
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id)

    class Meta:
        model = Product
        fields = ['subcategory']
