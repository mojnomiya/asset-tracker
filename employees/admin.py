from django.contrib import admin
from .models import Company, Department, Employee

# Registering models to django-admin.

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)