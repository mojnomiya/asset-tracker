from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import AssetsSerializer
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