from django.urls import path
from .views import AddEmployeeView, AllEmployeeView

urlpatterns = [
    path('', AllEmployeeView.as_view(), name='all-employees'),
    path('add-employees/', AddEmployeeView.as_view(), name='employee-create'),
]