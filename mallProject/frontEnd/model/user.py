from django.db import models
from rest_framework import serializers


class User(models.Model):
    user_id = models.AutoField(primary_key=True,unique=True, verbose_name=u'用户id')
    user_name = models.CharField(max_length=18, unique=True, verbose_name=u'用户名')
    user_password = models.CharField(max_length=128, verbose_name=u'密码')
    user_pay_password = models.IntegerField(blank=True, null=True, verbose_name='支付密码')
    user_nickname = models.CharField(max_length=18, blank=True, null=True, verbose_name=u'用户昵称')
    user_sex = models.IntegerField( blank=True, null=True, choices=((None, None), (0, '女'), (1, u'男')),
                                   default=None,verbose_name=u'性别')
    user_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')
    user_registration_date = models.DateTimeField(auto_now_add=True, editable=False,verbose_name='最近一次登陆时间')
    user_portrait = models.ImageField(blank=True, null=True, verbose_name='头像')
    user_tel = models.CharField(max_length=11,blank=True,null=True, verbose_name='手机号')
    user_vip_class = models.IntegerField( choices=((0, u'普通VIP'), (1, '至尊VIP'), (2, u'代理商')), default=0,
                                         verbose_name='vip等级')
    user_status = models.IntegerField( choices=((0, u'从未下单的'), (1, '下单未支付的'), (2, u'下过单的')), default=0,
                                      verbose_name='用户质量')
    user_balance = models.IntegerField(default=0, verbose_name='账户余额')

    class Meta:
        verbose_name = u'账号信息'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.user_id
