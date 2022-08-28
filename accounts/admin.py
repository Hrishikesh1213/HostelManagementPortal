from django.contrib import admin

from accounts.models import Student, Officer

# Register your models here.
admin.site.register(Student)
admin.site.register(Officer)