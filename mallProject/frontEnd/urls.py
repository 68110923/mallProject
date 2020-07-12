from django.contrib import admin
from django.urls import path,include,re_path
from frontEnd import views
from rest_framework import routers


router = routers.DefaultRouter()



urlpatterns = [
    path('',views.IndexApi.as_view(),name='index'),  # 获取首页页面
    path('login/',views.LoginApi.as_view(),name='login'),  # 获取首页页面
    path('register/',views.RegisterApi.as_view(),name='register'),  # 获取首页页面







]