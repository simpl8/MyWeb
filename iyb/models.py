# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.


class UserInfo(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="女")
    c_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

# 工作时间
class WorkTimes(models.Model):
    status = (
        ('yes', '完成'),
        ('no', '未完成')
    )
    id = models.AutoField(primary_key=True)
    year_month = models.CharField(max_length=64, unique=True)  # 工作年月
    worker = models.CharField(max_length=64)  # 负责人
    create_time = models.DateTimeField(auto_now=True)  #创建时间
    status_info = models.CharField(max_length=32, choices=status, default="未完成")  # 完成状态


# 需求测试情况
class Function(models.Model):
    time = models.ForeignKey('WorkTimes', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    