from django.http import JsonResponse
from frontEnd.models import *
from django.views import View



class gets(View):
    def get(self,request,*args,**kwargs):
        return JsonResponse({
            '用户信息':'b',
            '商品信息':'b',
        })
    def post(self):
        return JsonResponse({})

