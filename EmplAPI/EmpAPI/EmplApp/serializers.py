from rest_framework import serializers
from .models import Departmens, Employess


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departmens
        fields = ('DepartmentID', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employess
        fields = ('EmpID', 'EmpName','Department','DateOfJoining','PhotoFileName')