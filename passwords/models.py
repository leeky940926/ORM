from django.db import models

class Admin(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=500)


class AuthUser(models.Model):
    phone_number = models.CharField(max_length=12)
    password= models.CharField(max_length=500)
    