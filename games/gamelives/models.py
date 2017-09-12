from django.db import models
from django.utils import timezone
class userinfo(models.Model):

    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    createtime=models.DateTimeField('创建日期',default = timezone.now)
    createip=models.GenericIPAddressField(protocol='ipv4',null=True)


class news(models.Model):
    url=models.CharField(max_length=64)
    urlcontect=models.CharField(max_length=64)
    newstype=models.ForeignKey(to='newsType',to_field='id')

class newsType(models.Model):
    type_chices=(
        ('1','图片'),
        ('2','文字'),
        ('3','其他'),
    )
    what_type=models.CharField(max_length=20,choices=type_chices,default='2')

class sina(models.Model):
    url=models.CharField(max_length=300)
    utlstr=models.CharField(max_length=200)

class acf(models.Model):
    url=models.CharField(max_length=200)
    urlcontent=models.CharField(max_length=300)

class lives(models.Model):
    url=models.CharField(max_length=200)
    urlcontent=models.CharField(max_length=300)



