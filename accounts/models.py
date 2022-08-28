from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.CharField(max_length=9)  
    name = models.CharField(max_length=30)  
    phnNum = models.CharField(max_length=10)  
    room = models.IntegerField() 
    wing = models.CharField(max_length=1)  
    hostel = models.CharField(max_length=20)  
    email = models.EmailField(max_length=50)  
    password = models.CharField(max_length=50)  

class Officer(models.Model):
    empid = models.CharField(max_length=9)  
    name = models.CharField(max_length=30)  
    phnnum = models.CharField(max_length=10)  
    rank = models.IntegerField() 
    officeRoom =  models.IntegerField() 
    wing = models.CharField(max_length=1)  
    hostel = models.CharField(max_length=20)  
    email = models.EmailField(max_length=50)  
    password = models.CharField(max_length=50)  


class Complaint(models.Model):
    cid = models.CharField(max_length=30)   
    typeOfIssue = models.CharField(max_length=30)  
    description = models.CharField(max_length=100)  
    avail_start = models.DateTimeField()
    avail_end = models.DateTimeField()
    status = models.CharField(max_length=10) 
