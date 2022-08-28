from django.contrib import admin
from .models import Student,Officer,Complaint

# Register your models here.
admin.site.register(Student)
admin.site.register(Officer)
admin.site.register(Complaint)