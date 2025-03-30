from django.contrib import admin
from .models import Departmens, Employess

# Register your models here.

list_to_reg = [Departmens, Employess]

for elem in list_to_reg: admin.site.register(elem)

