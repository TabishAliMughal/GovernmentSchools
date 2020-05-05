from django.db import models
from main.models import *
from institution.models import *
from django.contrib.auth.models import User


class Employ(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    semis_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    fathername = models.CharField(max_length = 100)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'),('F', 'Female')))
    designation = models.CharField(max_length=10)
    currentbps = models.IntegerField()
    persionalnumber = models.IntegerField()
    cnic = models.IntegerField()
    contact = models.IntegerField()
    dateofbirth = models.DateField()
    dateofapplication = models.DateField()
    dateofjoin = models.DateField()
    dateofmedical = models.DateField()
    dateofregularistation = models.DateField()
    bpsatfirstjoin = models.IntegerField()
    qualification = models.ForeignKey(Qualification,on_delete = models.CASCADE)
    domicile = models.ForeignKey(Division,on_delete=models.CASCADE)
    matricpassingyear = models.IntegerField()
    interpassingyear = models.IntegerField()
    graduationyear = models.IntegerField()
    otheraccademics = models.IntegerField()
    bedpassingyear = models.IntegerField()
    bedresultdate = models.DateField()
    otherprofessionalqualification = models.CharField(max_length=10)
    biometricverified = models.BooleanField()
    status = models.CharField(max_length=10, choices=(('A', 'Active'),('I', 'Inactive')))
    interdistricttransfer = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    dateofjoinindivision = models.DateField()
    dateofretirement = models.DateField()
    remarks = models.CharField(max_length = 100)
    uc = models.ForeignKey(UnionCouncil , on_delete = models.CASCADE)
    prefix = models.CharField(max_length = 50,null=True , blank=True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE,null=True , blank=True)
    address = models.CharField(max_length = 250)
    headname = models.CharField(max_length = 50,null=True , blank=True)
    head = models.CharField(max_length = 150,null=True , blank=True)
    training = models.CharField(max_length = 150,null=True , blank=True)
    def __str__(self):
        return self.name


class EmployDocuments(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    documenttype = models.ForeignKey(DocumentType,on_delete = models.CASCADE)
    employ = models.ForeignKey(Employ,on_delete = models.CASCADE)
    picture = models.ImageField(upload_to='static/images/user/%user')
    def __str__(self):
        return '{} of {}'.format(self.documenttype,self.employ)


