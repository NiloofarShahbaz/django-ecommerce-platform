from django.urls import path

from .views import category_details, product_details, home

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/', category_details, name='category_details'),
    path('categories/<int:category_id>/<int:product_id>/', product_details, name='product_details'),

]
