from django.contrib import admin
from django.urls import path,include
from frontEnd import views
from rest_framework import routers


router = routers.DefaultRouter()



urlpatterns = [
    path('',views.gets.gets.index,name='getIndex'),
    # path('user/',views.users.user,name='user'), # 注册，修改个人信息，注销用户
    path('login/',views.users.login,name='login'), # 登录
    path('register/',views.users.register,name='register'), # 注册

    path('getPersonalMessage/',views.users.users.getPersonalMessage,name='getPersonalMessage'),   #查看个人资料
    # path('modifyPassword/',views.users.modifyPassword,name='modifyPassword'),   #修改密码
    # path('modifyAvatar/',views.users.modifyAvatar,name='modifyAvatar'),   #修改头像
    # path('bindingTelNumber/',views.users.bindingTelNumber,name='bindingTelNumber'),   #绑定手机号码

]