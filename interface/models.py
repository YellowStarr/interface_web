from django.db import models

# Create your models here.


class interface(models.Model):
    base_url = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    method = models.CharField(max_length=16)
    args = models.CharField(max_length=100)

class Case(models.Model):
    case_name = models.CharField(max_length=300)
    base_url = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    method = models.CharField(max_length=16)
    args_json = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    assertion = models.CharField(max_length=1000)
    result = models.CharField(max_length=16)
    excute_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField(default=1)


