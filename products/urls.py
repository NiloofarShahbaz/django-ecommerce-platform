from django.urls import path

from .views import category_details

urlpatterns=[
    path('categories/<int:category_id>/', category_details, name='category_details'),
]