from django.http import JsonResponse, response, HttpResponse,HttpResponseRedirect
from frontEnd.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
import json
from django.core import serializers
from django.forms import model_to_dict
from django.views import View
import functools



def check_user(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        #判断是否登录
        userid = args[0].session.get("login_user", "")
        if userid == "":
            #保存当前的url到session中
            # args[0].session["path"] = args[0].path
            #重定向到登录页面
            return HttpResponseRedirect('/login/',kwargs={'msg':'您还未登录，请登录'})
        return func(*args, **kwargs)
    return inner

@method_decorator(check_user,name='put')
# @method_decorator(csrf_exempt,name='dispatch')  #cbv免除csrf
class userView(View):
    def post(self,request,*args,**kwargs):
        # 注册
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user_pay_password = request.POST['user_pay_password']
        user_nickname = request.POST['user_nickname']
        user_sex = request.POST['user_sex']
        user_tel = request.POST['user_tel']

        if User.objects.filter(user_name=user_name):
            return JsonResponse({'msg':'用户名已经被使用'})
        if User.objects.filter(user_tel=user_tel):
            return JsonResponse({'msg':'手机号已经被使用'})
        User.objects.create(user_name=user_name, user_password=user_password, user_pay_password=user_pay_password,
                            user_nickname=user_nickname,
                            user_sex=user_sex, user_tel=user_tel).save()
        obj = User.objects.filter(user_name=user_name)
        data = json.loads(serializers.serialize('json', obj))
        return JsonResponse(data, safe=False)
    def get(self,request,*args,**kwargs):
        # 登录
        user_name = request.GET['username']
        user_password = request.GET['pwd']
        user = User.objects.filter(user_name=user_name)[0]

        if (user_name == user.user_name and user_password == user.user_password) or (user_name==user.user_tel and user_password==user.user_password):
            request.session["login_user"] = user.user_id
            return JsonResponse({'state': True, 'msg': json.loads(serializers.serialize('json',[user]))})
        else:
            return JsonResponse({'state': False, 'msg': '您的账号或者密码错误'})
    def put(self,request,*args,**kwargs):
        return JsonResponse({'msg':request.session['login_user']})



class users:


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
