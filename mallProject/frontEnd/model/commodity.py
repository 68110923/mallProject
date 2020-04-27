from django.db import models
from frontEnd.model.user import User


class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'商品id')
    commodity_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='商品创建的时间')
    commodity_state_putaway = models.IntegerField(choices=(
        (0, '正在审核'), (1, '未上架'), (2, '已上架'), (3, '违规商品'), (4, '已删除')), default=0, verbose_name='商品的上架状态')
    commodity_state_recommend = models.IntegerField(choices=((0, '热卖推荐'), (1, '新品推荐'), (2, '季节推荐')),
                                                    blank=True, null=True, verbose_name='商品的推荐状态')
    commodity_cover=models.CharField(max_length=256, blank=True, null=True, verbose_name='商品主要的封面图')
    commodity_mc_video = models.CharField(max_length=256, blank=True, null=True, verbose_name='商品介绍视频')
    commodity_video_cover = models.CharField(max_length=256, blank=True, null=True, verbose_name='商品介绍视频的封面图')
    commodity_price_bazaar = models.IntegerField( blank=True, null=True, verbose_name='商品市场价')
    commodity_price_vip = models.IntegerField( blank=True, null=True, verbose_name='商品vip价格')
    commodity_price_svip = models.IntegerField( blank=True, null=True, verbose_name='商品svip价格')
    commodity_price_agency = models.IntegerField( blank=True, null=True, verbose_name='商品代理价格')
    commodity_title=models.CharField(max_length=128,blank=True,null=True,verbose_name='商品的标题')
    CommodityToUser = models.ForeignKey(User, to_field='user_id',on_delete=models.CASCADE, verbose_name='发布商品用户的ID')

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.commodity_id
