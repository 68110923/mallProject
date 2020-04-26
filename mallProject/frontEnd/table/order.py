from django.db import models
from frontEnd.table.user import User
from frontEnd.table.commodity import Commodity
from frontEnd.table.addressee import Addressee


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name=u'订单id')
    order_number = models.IntegerField(verbose_name='订单编号')
    order_state = models.IntegerField(choices=((0, '未支付'), (1, '已支付'), (2, '已发货'), (3, '已到货'),
                                                            (4, '已签收'), (5, '已完成')),default=0, verbose_name='订单状态')
    order_serial_number = models.IntegerField(verbose_name='交易流水号')
    OrderToUser = models.ForeignKey(User, to_field='user_id', on_delete=models.DO_NOTHING, verbose_name='下单用户id')
    OrderToCommodity = models.ForeignKey(Commodity, to_field='commodity_id', on_delete=models.DO_NOTHING,
                                         verbose_name='购买的商品id')
    OrderToAddressee = models.ForeignKey(Addressee, to_field='addressee_id', on_delete=models.DO_NOTHING,
                                         verbose_name='购物使用的收货地址id')

    class Meta:
        verbose_name = u'订单信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.order_id
