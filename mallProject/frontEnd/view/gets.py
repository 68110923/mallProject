from django.http import JsonResponse
from frontEnd.models import *



class gets:
    def __init__(self,request):
        self.request = request
    def index(self):
        return JsonResponse({
            '用户信息':'b',
            '商品信息':'b',
        })
    def commodityDetailedInfo(self):
        return JsonResponse({})