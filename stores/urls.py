from django.urls import path

from .views import create_store, validate_store_name, add_store_details, add_store_logo, add_store_cover, add_store_policy

urlpatterns = [
    path('create/', create_store, name='create_store'),
    path('create/validate_name/', validate_store_name, name='validate_store_name'),
    path('create/<store_id>/details/', add_store_details, name='add_store_details'),
    path('create/<store_id>/details/logo/', add_store_logo, name='add_store_logo'),
    path('create/<store_id>/details/cover/', add_store_cover, name='add_store_cover'),
    path('create/<store_id>/policy', add_store_policy, name='add_store_policy'),

]
