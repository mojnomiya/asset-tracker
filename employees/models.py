from django.db import models

# Basic models for storing Company, Departments and Employee informantion

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

# Department in the company
class Department(models.Model):
    department_name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.department_name

# Employee details
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.get_full_name()
    

