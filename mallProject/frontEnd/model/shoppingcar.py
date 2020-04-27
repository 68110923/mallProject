from django.db import models
from frontEnd.model.user import User
from frontEnd.model.commodity import Commodity


class ShoppingCar(models.Model):
    car_id = models.AutoField(primary_key=True, unique=True, verbose_name=u'购物车id')
    car_number=models.IntegerField(default=1,verbose_name='加入购物车的数量')
    car_created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='添加到购物车的时间')
    CarToCommodity=models.OneToOneField(Commodity,to_field='commodity_id',on_delete=models.DO_NOTHING,verbose_name='商品id,多对多，购物车中的对象与商品对象的关系')
    CarToUser=models.ForeignKey(User,to_field='user_id',on_delete=models.CASCADE,verbose_name='用户id,多对一，多个购物车中的商品对应一个用户')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.car_id
