from django.contrib import admin
from django.urls import path
from frontEnd import views

urlpatterns = [
    path('',views.gets.index,name='getIndex'),
    path('user/',views.users.user,name='user'), # 注册，登录，修改个人信息，注销用户
    path('getPersonalMessage/',views.users.getPersonalMessage,name='getPersonalMessage'),   #查看个人资料
    path('modifyPassword/',views.users.modifyPassword,name='modifyPassword'),   #修改密码
    path('modifyAvatar/',views.users.modifyAvatar,name='modifyAvatar'),   #修改头像
    path('bindingTelNumber/',views.users.bindingTelNumber,name='bindingTelNumber'),   #绑定手机号码

]