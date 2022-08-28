from django.db import models

# Create your models here.

class Complaint(models.Model):
    # cid = models.CharField(max_length=30)   
    sid = models.CharField( max_length=9) 
    date = models.DateTimeField()

    typeOfIssue = models.CharField(max_length=30)  
    description = models.CharField(max_length=100)  
    
    avail_start = models.DateTimeField()
    avail_end = models.DateTimeField()
    
    status = models.CharField(max_length=10) 
    officerName = models.CharField(max_length=30) 
    officerRank = models.IntegerField() 
