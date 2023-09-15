from .models import Employee
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import EmployeeSerializer, AllEmployeeSerializer

# Create your views here.

class AddEmployeeView(CreateAPIView):
    """
    Add employee
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class AllEmployeeView(ListAPIView):
    """
    This API will return all the employee list
    """
    serializer_class = AllEmployeeSerializer
    queryset = Employee.objects.all()