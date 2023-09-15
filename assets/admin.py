from django.contrib import admin
from .models import AssetsCategory, Assets, CheckOutLog

# Registering models to django-admin.

admin.site.register(AssetsCategory)
admin.site.register(Assets)
admin.site.register(CheckOutLog)