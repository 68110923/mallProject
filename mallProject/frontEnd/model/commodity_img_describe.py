'''商品描述图片url，与商品多对一'''

from django.db import models
from frontEnd.model.commodity import Commodity


class CommodityImgDescribe(models.Model):
    img_describe_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'描述图片id')
    img_describe_url=models.CharField(max_length=128,verbose_name='描述图片链接')
    img_describe_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='添加的时间')
    ImgDescribeToCommodity=models.ForeignKey(Commodity,to_field='commodity_id',on_delete=models.CASCADE,verbose_name='商品di,多对一')


    class Meta:
        verbose_name = u'商品图片描述'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.img_describe_id
