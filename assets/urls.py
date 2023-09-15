from django.urls import path
from .views import AssignAssetView

urlpatterns = [
    path('assign-asset/<int:employee_id>/', AssignAssetView.as_view(), name='assign-asset'),
]