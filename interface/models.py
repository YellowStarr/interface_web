from django.db import models
from jsonfield import JSONField
# Create your models here.


class interface(models.Model):
    """
    接口表
    """
    base_url = models.CharField(max_length=300)
    header = models.CharField(max_length=1000,null=True, blank=True)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    method = models.IntegerField(verbose_name="方法", choices=[(1, "get"), (2, "post")])
    args = models.CharField(max_length=100)
    # create_time = models.DateTimeField(auto_now=True)
    modify_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField(default=1)

class Case(models.Model):
    """
    用例表，包含执行结果和执行时间等。外键是接口表的id
    """
    case_name = models.CharField(max_length=500,null=True, blank=True)
    args_json = models.CharField(max_length=1000,null=True, blank=True)
    response = models.CharField(max_length=1000)
    assertion = models.CharField(max_length=1000)
    result = models.CharField(max_length=16)
    modify_time = models.DateTimeField(auto_now=True)
    excute_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField(default=1)
    interf = models.ForeignKey(interface, on_delete=models.CASCADE, null=True, blank=True)
    # int_id = models.IntegerField(null=True, blank=True)




