'''订单评论，与商品多对一'''

from django.db import models
from frontEnd.table.commodity import Commodity
from frontEnd.table.user import User
from frontEnd.table.order import Order



class CommodityComment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name=u'评论id')
    comment_appraise=models.IntegerField(choices=((1,u'⭐'),(2,u'⭐⭐'),(3,u'⭐⭐⭐'),(4,u'⭐⭐⭐⭐'),(5,u'⭐⭐⭐⭐⭐')),verbose_name='商品评价')
    comment_content = models.CharField(max_length=256,blank=True,null=True, verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='评论时间')
    CommentToUser=models.ForeignKey(User,to_field='user_id',on_delete=models.DO_NOTHING,verbose_name='进行评论的用户id')
    CommentToCommodity=models.ForeignKey(Commodity,to_field='commodity_id',on_delete=models.CASCADE,verbose_name='商品di,多对一')
    CommentToOrder=models.ForeignKey(Order,to_field='order_id',on_delete=models.DO_NOTHING,verbose_name='订单di,多对一')



    class Meta:
        verbose_name = u'商品图片详情'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.comment_id
