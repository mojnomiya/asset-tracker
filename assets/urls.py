from django.urls import path
from .views import AssignAssetView, ReturnAssetView

urlpatterns = [
    path('assign-asset/<int:employee_id>/', AssignAssetView.as_view(), name='assign-asset'),
    path('return-asset/<int:employee_id>/', ReturnAssetView.as_view(), name='return-asset'),
]