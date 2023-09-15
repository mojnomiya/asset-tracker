from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import AssetsSerializer, CheckOutLogSerializer
from employees.models import Employee
from .models import Assets, CheckOutLog

class AssignAssetView(CreateAPIView):
    """
    Assigns asset to an employee with his id
    """
    serializer_class = AssetsSerializer

    def create(self, request, *args, **kwargs):
        employee_id = self.kwargs.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            asset = serializer.save()

            CheckOutLog.objects.create(
                device=asset,
                employee=employee,
                check_out_date=asset.date_added,
                condition_at_checkout=asset.condition
            )

            return Response({'message': 'Asset assigned successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReturnAssetView(CreateAPIView):
    """
    Returned asset entried in the log 
    """

    serializer_class = AssetsSerializer

    def create(self, request, *args, **kwargs):
        serial_number = request.data.get('serial_number')
        employee_id = self.kwargs.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)

        try:
            asset = Assets.objects.get(serial_number=serial_number)
        except Assets.DoesNotExist:
            return Response({'message': 'Asset not found'}, status=status.HTTP_404_NOT_FOUND)


        CheckOutLog.objects.create(
                device=asset,
                employee=employee,
                check_out_date=asset.date_added,
                condition_at_checkout=asset.condition
        )

        return Response({'message': 'Asset returned successfully'}, status=status.HTTP_201_CREATED)
    

class AssetLogsView(ListAPIView):
    serializer_class = CheckOutLogSerializer
    def get_queryset(self):
        asset_id = self.kwargs.get('asset_id')
        employee_id = self.kwargs.get('employee_id')

        if asset_id is not None:
            # logs based on the asset's ID
            return CheckOutLog.objects.filter(device_id=asset_id)
        elif employee_id is not None:
            # logs based on the employee's ID
            return CheckOutLog.objects.filter(employee_id=employee_id)
        else:
            # all logs if neither asset_id nor employee_id is provided
            return CheckOutLog.objects.all()