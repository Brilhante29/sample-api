from django.db import models

# Create your models here.
class Filmes(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    date = models.CharField(max_length=100)
    starts = models.IntegerField()

