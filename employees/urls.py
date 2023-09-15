from django.urls import path
from .views import AddEmployeeView
urlpatterns = [
    path('add-employees/', AddEmployeeView.as_view(), name='employee-create'),
]