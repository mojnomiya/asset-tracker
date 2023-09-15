from django.db import models
from employees.models import Employee

#Model to store assets category
class AssetsCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Assests details
class Assets(models.Model):
    category = models.ForeignKey(AssetsCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='devices')
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=255)
    date_added = models.DateField()

    def __str__(self) -> str:
        return self.name
    

#check in and out log.
class CheckOutLog(models.Model):
    device = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='checkout_logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='checkout_logs')
    check_out_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    condition_at_checkout = models.CharField(max_length=255)
    condition_at_return = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Check-Out : {self.device.name} by {self.employee.get_full_name()}"