from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    phone_no = models.CharField(max_length=100, default='contact no')
    address = models.CharField(max_length=400,default="Hubli")

class CarDetails(models.Model):
    modal=models.CharField(max_length=400,default="Hubli")
    year=models.CharField(max_length=400,default="Hubli")
    price=models.CharField(max_length=400,default="Hubli")
    Engine=models.CharField(max_length=400,default="Hubli")
    Mileage=models.CharField(max_length=400,default="Hubli")
    about_car=models.CharField(max_length=400,default="Hubli")
    car_img1= models.FileField(upload_to='upload_img/')
    car_img2=models.FileField(upload_to='upload_img/')
    car_img3=models.FileField(upload_to='upload_img/')

class CarOrders(models.Model):
    car_id=models.ForeignKey('CarDetails', on_delete=models.CASCADE)
    Name=models.CharField(max_length=400,default="Hubli")
    email=models.CharField(max_length=400,default="Hubli")
    phone_no=models.CharField(max_length=400,default="Hubli")
    address=models.CharField(max_length=400,default="Hubli")

class Contacts(models.Model):
    Name=models.CharField(max_length=400,default="Hubli")
    email=models.CharField(max_length=400,default="Hubli")
    phone_no=models.CharField(max_length=400,default="Hubli")
    msg=models.CharField(max_length=400,default="Hubli")
   


