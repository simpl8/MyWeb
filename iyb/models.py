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
    worker = models.CharField(max_length=64)  # 测试人员
    create_time = models.DateTimeField(auto_now=True)  #创建时间
    status_info = models.CharField(max_length=32, choices=status, default="未完成")  # 完成状态


# 需求测试情况
class Function(models.Model):
    in_test = (
        ('yes', '是'),
        ('no', '否')
    )

    time = models.ForeignKey('WorkTimes', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    function_name = models.CharField(max_length=128)  # 需求名称
    dev_front = models.CharField(max_length=32)  # 前端开发
    dev_back = models.CharField(max_length=32)  # 后台开发
    dev_h5 = models.CharField(max_length=32)  # h5开发
    dev_native = models.CharField(max_length=32)  # 原生开发
    tester = models.CharField(max_length=32)  # 测试人员
    platform = models.CharField(max_length=32)  # 涉及平台
    test_status = models.CharField(max_length=32, choices=in_test, default="否")  # 是否提测
    test_env = models.CharField(max_length=16)  # 测试环境测试进度
    uat_env = models.CharField(max_length=16)  # uat环境测试进度
    question_remark = models.CharField(max_length=256, null=True)  # 问题备注
    