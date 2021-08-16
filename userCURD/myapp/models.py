from django.db import models
from datetime import datetime
# Create your models here.
class Users(models.Model):
    #主键id可以省略不写
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)#默认值
    phone=models.CharField(max_length=16)
    addTime=models.DateTimeField(default=datetime.now)
'''
class Meta:
    db_table="myapp_users"
    不写就是默认名称
'''