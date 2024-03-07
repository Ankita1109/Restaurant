from django.db import models
from ManagerApp.models import RecordsManger
# Create your models here.
class CheifFood(models.Model):
    userid=models.CharField(max_length=20,default='table')
    dishname=models.CharField(max_length=200)
    quantity=models.CharField(max_length=20)
