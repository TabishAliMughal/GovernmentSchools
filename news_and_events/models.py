from django.db import models
from institution.models import *
from django.urls import reverse

# Create your models here.
class News(models.Model):
    news_code = models.AutoField(unique=True, primary_key=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default= 1)
    news = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.news


class School_Activities(models.Model):
    activity_code = models.AutoField(unique=True, primary_key=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, default = 1)
    activity_name = models.CharField(max_length=300)
    activity_pics = models.ImageField(upload_to='static/images/user/')
    Date = models.DateField()
    def __str__(self):
        return self.activity_name

