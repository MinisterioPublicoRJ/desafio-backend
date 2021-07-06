from django.db import models


# Create your models here.
class LocalRegistrado(models.Model):
    nome = models.CharField(max_length=255)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
