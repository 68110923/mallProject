from django.http import JsonResponse
from frontEnd.models import *

class orders:
    def __init__(self,request):
        self.request = request

    def order(self):
        # 查看订单信息
        if self.request.method == 'GET':
            return JsonResponse({})

        # 删除订单信息
        elif self.request.method == 'DEL':
            return True

        # 订单结束后的评价功能
        elif self.request.method == 'POST':
            return True

    # 结算(模仿淘宝结算功能)
    def settlement(self):
        pass

    # 提交订单，提交订单后直接跳转到支付页面
    def addOrder(self):
        return True

    # 取消订单
    def cancelOrder(self):
        return True

    # 支付功能
    def pay(self):
        return True
