from django.db import models
from django.db.models.fields import CharField

class registrar (models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
