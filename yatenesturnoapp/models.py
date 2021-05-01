from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=30)
    direction=models.CharField(max_length=50)
    category=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    description=models.CharField(max_length=100)




# Create your models here.
