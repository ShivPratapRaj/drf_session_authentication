from django.db import models

# Create your models here.

class Ceo(models.Model):
    company_name = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    since = models.IntegerField()