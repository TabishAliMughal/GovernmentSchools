from django.db import models
from main.models import *
from django.contrib.auth.models import User



class Institution(models.Model):
    semis_id = models.IntegerField(primary_key = True , unique = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE , blank = True , null = True)
    name = models.CharField(max_length = 300)
    unioncouncil = models.ForeignKey(UnionCouncil,on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class InstitutionRooms(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    roomtype = models.ForeignKey(RoomType , on_delete=models.CASCADE)
    therefor = models.CharField(max_length=10, choices=(('S', 'Students'),('T', 'Staff')))
    rooms = models.IntegerField()
    def __str__(self):
        return '{} for {} of {}'.format(self.roomtype,self.therefor,self.institution)

class InstitutionBoundaryWall(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    ifyes = models.CharField(max_length=10, choices=(('C', 'Complete'),('I', 'InComplete')) , blank=True , null=True)
    def __str__(self):
        return 'Boundary Wall Of {}'.format(self.institution)

class InstitutionBuildingCondition(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    condition = models.CharField(max_length=10, choices=(('G', 'Good'),('R', 'Repairable'),('D', 'Dangerous')))
    ifrepairable = models.CharField(max_length=10, choices=(('F', 'Floor'),('R', 'Roof'),('W', 'Walls')) , blank=True , null=True)
    def __str__(self):
        return 'Building Condition Of {}'.format(self.institution)

class InstitutionArea(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    def __str__(self):
        return 'Area Of {}'.format(self.institution)

class InstitutionWaterAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    availabletype = models.CharField(max_length=10, choices=(('D', 'Drinking'),('N', 'Non-Drinking')) , blank=True , null=True)
    def __str__(self):
        return 'Water Availiblity Of {}'.format(self.institution)

class InstitutionROPlantAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    type = models.CharField(max_length=10, choices=(('F', 'Functional'),('N', 'Non-Functional')) , blank=True , null=True)
    qty = models.IntegerField(blank = True , null=True)
    def __str__(self):
        return 'RO Plant Availiblity Of {}'.format(self.institution)

class InstitutionWaterDispenserAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    type = models.CharField(max_length=10, choices=(('E', 'Electric-Chiller'),('C', 'Cooler')) , blank=True , null=True)
    qty = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return 'Water Dispenser Availiblity Of {}'.format(self.institution)

class InstitutionPlayGround(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    type = models.CharField(max_length=10, choices=(('H', 'Huge'),('N', 'Normal'),('S', 'Small')) , blank=True , null=True)
    def __str__(self):
        return 'Play Ground Availiblity Of {}'.format(self.institution)

class InstitutionPlantation(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    qtyoftrees = models.IntegerField(blank=True,null=True)
    qtyofplants = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return 'Plantation Availiblity Of {}'.format(self.institution)

class InstitutionToiletAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    qty = models.IntegerField(blank=True,null=True)
    functionalqty = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return 'Toilet Availiblity Of {}'.format(self.institution)

class InstitutionWiringAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    condition = models.CharField(max_length=10, choices=(('G', 'Good'),('R', 'Repairable'),('D', 'Dangerous')))
    def __str__(self):
        return 'Wiring Availiblity Of {}'.format(self.institution)

class InstitutionPlumbingAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    condition = models.CharField(max_length=10, choices=(('G', 'Good'),('R', 'Repairable'),('D', 'Dangerous')))
    def __str__(self):
        return 'Plumbing Availiblity Of {}'.format(self.institution)

class InstitutionSenitaryAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    def __str__(self):
        return 'Senetary Availiblity Of {}'.format(self.institution)

class InstitutionElectricityAvailiblity(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    available = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    meter = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')),blank=True,null=True)
    meterno = models.IntegerField(blank=True,null=True)
    consumerno = models.IntegerField(blank=True,null=True)
    contactaccnp = models.IntegerField(blank=True,null=True)
    kunda = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    solar = models.CharField(max_length=10, choices=(('Y', 'Yes'),('N', 'No')))
    solarqty = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return 'Electricity Availiblity Of {}'.format(self.institution)

class InstitutionFurniture(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    institution = models.ForeignKey(Institution,on_delete = models.CASCADE)
    therefor = models.CharField(max_length=10, choices=(('S', 'Students'),('T', 'Staff')))
    dualdeskqty = models.IntegerField(blank=True,null=True)
    chairsqty = models.IntegerField(blank=True,null=True)
    tablesqty = models.IntegerField(blank=True,null=True)
    shelvesqty = models.IntegerField(blank=True,null=True)
    lockersqty = models.IntegerField(blank=True,null=True)
    cupboardqty = models.IntegerField(blank=True,null=True)
    others = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return 'Furniture Availiblity Of {} For {}'.format(self.institution,self.therefor)
    



