from django.shortcuts import render
from .models import Category, SubCategory, Product
from .filters import ProductFilter


def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = SubCategory.objects.filter(category=category)
    products = ProductFilter(request.GET, category_id=category_id,
                             queryset=Product.objects.filter(subcategory__category=category))

    context = {
        'category': category,
        'subcategories': subcategories,
        'products': products
    }

    return render(request, 'products/category_details.html', context)
