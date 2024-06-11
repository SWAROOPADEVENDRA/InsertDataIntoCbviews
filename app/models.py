from django.db import models

# Create your models here.
class Village(models.Model):
    Vname=models.CharField(max_length=100)
    Vaddress=models.CharField(max_length=100)
    Vmandal=models.CharField(max_length=100)
    Vpostnumber=models.IntegerField()