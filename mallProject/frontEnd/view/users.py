from django.http import JsonResponse, response, HttpResponse
from frontEnd.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.forms import model_to_dict


# 注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user_pay_password = request.POST['user_pay_password']
        user_nickname = request.POST['user_nickname']
        user_sex = request.POST['user_sex']
        user_tel = request.POST['user_tel']
        User.objects.create(user_name=user_name, user_password=user_password, user_pay_password=user_pay_password,
                            user_nickname=user_nickname,
                            user_sex=user_sex, user_tel=user_tel).save()
        obj = User.objects.filter(user_name=user_name)
        data = json.loads(serializers.serialize('json', obj))
        return JsonResponse(data, safe=False)


# 登录login
@csrf_exempt
def login(requser):
    if requser.method == 'POST':
        user_name = requser.POST['user_name']
        user_password = requser.POST['user_password']
        user = User.objects.filter(user_name=user_name)[0]
        if user_name == user.user_name and user_password == user.user_password:
            return JsonResponse({'state': True, 'msg': json.loads(serializers.serialize('json',[user])[1:-1])})
        else:
            return JsonResponse({'state': False, 'msg': '您的账号或者密码错误'})


class users:

    def __init__(self):
        self.request = self
        print(self)

    def user(self):
        # 查看用户(他人)信息
        if self.request.method == 'GET':
            return JsonResponse({'个人资料': ''})
        # 注册register
        elif self.request.method == 'POST':

            return JsonResponse({'个人资料': '登录成功'})
        # 修改个人资料modification
        elif self.request.method == 'PUT':
            return True
        # 注销账户
        elif self.request.method == 'DEL':
            return True

    # 查看个人资料
    def getPersonalMessage(self):
        return JsonResponse({'个人资料': ''})

    # 修改密码
    def modifyPassword(self):
        return True

    # 修改头像
    def modifyAvatar(self):
        return JsonResponse({'头像地址': ''})

    # 绑定手机号码
    def bindingTelNumber(self):
        return True
