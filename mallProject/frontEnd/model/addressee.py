from django.db import models
from frontEnd.model.user import User


class Addressee(models.Model):
    addressee_id = models.AutoField(primary_key=True, verbose_name=u'收件人id')
    addressee_name = models.CharField(max_length=32,blank=True,null=True, verbose_name=u'收件人姓名')
    addressee_tel = models.IntegerField( blank=True,null=True,verbose_name='收件人手机号')
    addressee_site = models.CharField(max_length=256,blank=True,null=True, verbose_name='地址')
    addressee_tag = models.CharField(max_length=32, blank=True, null=True, verbose_name='标签')
    addressee_state = models.IntegerField(blank=True, null=True, choices=((0, '默认收货地址'),(None,None)),verbose_name='是否为默认，0默认')
    addressee_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='创建时间')
    AddresseeToUser=models.ForeignKey(User,to_field='user_id',on_delete=models.DO_NOTHING, verbose_name='多对一，多个Addressee对应一个User')

    class Meta:
        verbose_name = u'收件信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.addressee_id
