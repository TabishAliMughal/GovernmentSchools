from django.db import models



class Institution(models.Model):
    semis_id = models.IntegerField(primary_key = True , unique = True)
    name = models.CharField(max_length = 300)
    def __str__(self):
        return self.name