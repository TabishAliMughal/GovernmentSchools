from django.db import models



class Provence(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    provencename = models.CharField(max_length = 150)
    def __str__(self):
        return str(self.provencename)

class Division(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    divisionname = models.CharField(max_length = 150)
    provence = models.ForeignKey(Provence , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.divisionname)

class District(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    districtname = models.CharField(max_length = 150)
    division = models.ForeignKey(Division , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.districtname)

class Tehsil(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    tehsilname = models.CharField(max_length = 150)
    district = models.ForeignKey(District , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.tehsilname)

class UnionCouncil(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    ucname = models.CharField(max_length = 150)
    tehsil = models.ForeignKey(Tehsil , on_delete = models.CASCADE)
    def __str__(self):
        return str(self.ucname)

class Qualification(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    qualificationname = models.CharField(max_length = 250)
    def __str__(self):
        return str(self.qualificationname)


class DocumentType(models.Model):
    code = models.AutoField(primary_key = True , unique = True)
    documenttype = models.CharField(max_length = 250)
    def __str__(self):
        return str(self.documenttype)
