from django.db import models

# Create your models here.

class Departmens(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Employess(models.Model):
    EmpID = models.AutoField(primary_key=True)
    EmpName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
    
