# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Place(models.Model):
    name  = models.CharField(max_length = 40,verbose_name = "名字")
    address = models.TextField(verbose_name = "地址")
    openhours = models.CharField(max_length = 40, verbose_name = "开放时间")
    ticketInfo = models.CharField(max_length = 40, verbose_name = "门票信息")
    recommendTime = models.FloatField(max_length = 40, verbose_name = "推荐时长")
    score = models.FloatField(max_length = 40, verbose_name = "评分")
    intro = models.TextField(verbose_name = "景点介绍");
    tips = models.TextField(verbose_name = "旅行小贴士");
    experience = models.TextField(verbose_name = "网友经验");
    
    def __unicode__(self):
         return u'%s %s' %(self.name,self.address)
