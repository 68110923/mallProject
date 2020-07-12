from django.http import JsonResponse, response, HttpResponse, HttpResponseRedirect
from frontEnd.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
import json
from django.core import serializers
from django.forms import model_to_dict
from django.views import View
import functools
from django.shortcuts import render


class IndexApi(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginApi(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        # 注册
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        # user_pay_password = request.POST['user_pay_password']
        # user_nickname = request.POST['user_nickname']
        # user_sex = request.POST['user_sex']
        # user_tel = request.POST['user_tel']

        if User.objects.filter(user_name=user_name):
            return JsonResponse({'msg': '用户名已经被使用'})
        # if User.objects.filter(user_tel=user_tel):
        #     return JsonResponse({'msg': '手机号已经被使用'})
        # User.objects.create(user_name=user_name, user_password=user_password, user_pay_password=user_pay_password,
        #                     user_nickname=user_nickname,
        #                     user_sex=user_sex, user_tel=user_tel).save()
        User.objects.create(user_name=user_name, user_password=user_password).save()
        obj = User.objects.filter(user_name=user_name)
        data = json.loads(serializers.serialize('json', obj))
        return JsonResponse(data, safe=False)


class RegisterApi(View):
    def get(self,request):
        return render(request, 'user/register.html')
    def post(self, request):
        # 登录
        user_name = request.POST['username']
        user_password = request.POST['pwd']
        user = User.objects.filter(user_name=user_name)[0]
        if (user_name == user.user_name and user_password == user.user_password) or (
                user_name == user.user_tel and user_password == user.user_password):
            request.session["login_user"] = f'{user.user_id}:{user_name}'
            return JsonResponse({'state': True, 'msg': json.loads(serializers.serialize('json', [user]))})
        else:
            return JsonResponse({'state': False, 'msg': '您的账号或者密码错误'})


class UserApi(View):
    def get(self, request):
        # 查看用户资料
        # if request.GET['id']:
        #     data = json.loads(serializers.serialize('json', User.objects.get(id=request.GET['id'])))
        # else:
        data = json.loads(serializers.serialize('json', User.objects.all()))
        return JsonResponse(data, safe=False)
