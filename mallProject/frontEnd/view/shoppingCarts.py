from django.http import JsonResponse
from frontEnd.models import *

class shoppingCarts:
    def __init__(self,request):
        self.request = request

    def cart(self):
        # 加入购物车
        if self.request.method == 'POST':
            return True

        # 修改数量
        elif self.request.method == 'PUT':
            return True

        # 删除
        elif self.request.method == 'DEL':
            return True

        # 查看购物车列表
        elif self.request.method =='GET':
            return JsonResponse({})
