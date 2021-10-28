from django.db import models

# Create your models here.
class cargos(models.Model):
    cargo = models.CharField(max_length=45)
