from .models import Employee
from rest_framework.generics import CreateAPIView
from .serializers import EmployeeSerializer

# Create your views here.

class AddEmployeeView(CreateAPIView):
    """
    Add employee
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()