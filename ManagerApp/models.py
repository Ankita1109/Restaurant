from django.db import models
from django.db.models.base import Model

# Create your models here.
class Manager(models.Model):
    UserId=models.CharField(max_length=300,primary_key=True)
    Password=models.CharField(max_length=150)
    profilepic=models.FileField(upload_to="manager/profilepic",blank=True)
    Name=models.CharField(max_length=200)
    Phone=models.CharField(max_length=14)
    AdharCard=models.CharField(max_length=60)
    Date=models.DateField(auto_now=True)
    Time=models.TimeField(auto_now=True)

class ChiefModel(models.Model):
    UserId=models.CharField(max_length=300,primary_key=True)
    Password=models.CharField(max_length=300)
    ChiefName=models.CharField(max_length=300)
    Chief_Experiance=models.CharField(max_length=50)
    C_Post=models.CharField(max_length=50)
    Cheif_AdharCard=models.CharField(max_length=300)
    Chief_Number=models.CharField(max_length=300)
    ChiefAddress=models.CharField(max_length=300)
    ProfileImage=models.FileField(upload_to="Chief/ChiefProfile/",max_length=600,default='None')
    Date=models.DateTimeField(auto_now=True)

class CustomerBill(models.Model):
    
    userid=models.CharField(max_length=500,primary_key=True)
    password=models.CharField(max_length=300)
    name=models.CharField(max_length=200,blank=True)
    PhoneNubmber=models.CharField(max_length=20,blank=True)
    Date_Time=models.DateTimeField(auto_now=True)
class HomeDelivery(models.Model):
    userid=models.OneToOneField(CustomerBill,on_delete=models.CASCADE)
    address=models.CharField(max_length=800)
    PhoneNumber=models.CharField(max_length=15)

#class Records(models.Model):
class CustomerItems(models.Model):
    userid=models.ForeignKey(CustomerBill,on_delete=models.CASCADE)
    ItemName=models.CharField(max_length=300)
    quantity=models.CharField(max_length=10,default='1')
    orginalCost=models.CharField(max_length=10,default='0')
    itemCost=models.CharField(max_length=300)
    Date_Time=models.DateTimeField(auto_now=True)
class RecordsManger(models.Model):
    userid=models.ForeignKey(CustomerBill,on_delete=models.CASCADE)
    Check=models.CharField(max_length=50,default='table')
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    TotalCost=models.CharField(max_length=300)
    active=models.CharField(max_length=5,default='0')
