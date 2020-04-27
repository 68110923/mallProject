'''商品详情图片url，与商品多对一'''

from django.db import models
from frontEnd.model.commodity import Commodity


class CommodityImgDetails(models.Model):
    img_details_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'详情图片id')
    img_details_url=models.CharField(max_length=128,verbose_name='描述图片链接')
    img_details_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='添加的时间')
    ImgDetailsToCommodity=models.ForeignKey(Commodity,to_field='commodity_id',on_delete=models.CASCADE,verbose_name='商品di,多对一')


    class Meta:
        verbose_name = u'商品图片详情'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.img_details_id
