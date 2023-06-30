from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    foto = models.URLField(null=True)