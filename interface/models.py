from django.db import models

# Create your models here.


class interface(models.Model):
    base_url = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    method = models.CharField(max_length=16)
    args = models.CharField(max_length=100)

