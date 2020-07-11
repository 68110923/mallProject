from django.contrib import admin
from django.urls import path,include
from frontEnd import views
from rest_framework import routers


router = routers.DefaultRouter()



urlpatterns = [
    path('',views.gets.as_view(),name='getIndex'),
    path('user/',views.userView.as_view(),name='user'), # 注册，修改个人信息，注销用户





]