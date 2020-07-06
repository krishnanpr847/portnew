from django.db import models

# Create your models here.
class port_model(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    feedback=models.TextField()