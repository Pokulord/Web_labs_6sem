from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departmens, Employess
from .serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def DepartmentApi(request , id =0):
    if request.method == "GET":
        departments = Departmens.objects.all()
        departments_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(departments_serializer.data , safe= False)
    
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added successfully", safe = False)
        
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)

        department = Departmens.objects.get(DepartmentID = department_data['DepartmentID'])
        departments_serializer = DepartmentSerializer(department , data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        
        return JsonResponse("Deleted successfullt" , safe = False)
    

@csrf_exempt
def EmpApi(request, id = 0):
    if request.method == 'GET':
        employees = Employess.objects.all()
        employess_serializer = EmployeeSerializer(employees, many = True)
        return JsonResponse(employess_serializer.data, safe = False)
    
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfulyy", safe= False)
        return JsonResponse("Failed to add ", safe = False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employess.objects.get(EmpID=employee_data['EmpID'])
        employees_serializer =  EmployeeSerializer(employee, data = employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update")
    
    elif request.method == "DELETE":
        employee = Employess.objects.get(EmpID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe = False)
    

@csrf_exempt
def SaveFile(request):
    file = request.FILES['upload_file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe= False)
    