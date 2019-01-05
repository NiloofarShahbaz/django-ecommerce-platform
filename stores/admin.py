from django.contrib import admin
from .models import Policy, ShippingMethod, Shipping, Store

# Register your models here.
admin.site.register(Policy)
admin.site.register(Shipping)
admin.site.register(ShippingMethod)
admin.site.register(Store)
