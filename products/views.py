from django.shortcuts import render
from .models import Category, SubCategory, Product


def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = SubCategory.objects.filter(category=category)
    products = Product.objects.filter()
    context = {
        'category': category,
        'subcategories': subcategories
    }

    return render(request, 'products/category_details.html', context)
