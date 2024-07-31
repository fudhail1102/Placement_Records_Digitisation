from django.contrib import admin
from .models import (
    Student, 
    Company, 
    PlacementActivity,
)
# Register your models here.


admin.site.register(Student)
admin.site.register(Company)
admin.site.register(PlacementActivity)


