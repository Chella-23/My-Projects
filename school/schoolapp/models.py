from django.db import models



# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=200)
    Father_Name=models.CharField(max_length=200)
    Mother_Name=models.CharField(max_length=200)
    Age=models.IntegerField()
    Address=models.CharField(max_length=150)
    Class_For_Admission=models.IntegerField()

