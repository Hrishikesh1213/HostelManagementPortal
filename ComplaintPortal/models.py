from django.db import models

# Create your models here.

class Complaint(models.Model):
    cid = models.CharField(max_length=30)   
    typeOfIssue = models.CharField(max_length=30)  
    description = models.CharField(max_length=100)  
    avail_start = models.DateTimeField()
    avail_end = models.DateTimeField()
    status = models.CharField(max_length=10) 
    officer = models.CharField()
