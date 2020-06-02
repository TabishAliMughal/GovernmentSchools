from django.db import models
from institution.models import *
from django.urls import reverse

# Create your models here.
class Class(models.Model):
    class_code = models.AutoField(unique = True, primary_key= True)
    classes = models.CharField(max_length=20)
    def __str__(self):
        return self.classes

class Student(models.Model):
    school_name = models.ForeignKey(Institution, on_delete = models.CASCADE)
    gr = models.IntegerField(primary_key=True, unique = True)
    name = models.CharField(max_length=300)
    father_name = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'),('F', 'Female')))
    father_cnic_no = models.IntegerField()
    father_contact_no = models.CharField(max_length = 11)
    address = models.CharField(max_length=300)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    date_birth = models.DateField()
    date_admission = models.DateField()
    date_leaving_school = models.DateField(blank = True , null = True)
    Reason_of_leaving = models.TextField(blank = True , null = True)
    religion = models.CharField(max_length=300)
    def	get_absolute_url(self):
        return reverse('student_detail',args=(self.school_name.pk,self.gr))
    def __str__(self):
        return self.name 
