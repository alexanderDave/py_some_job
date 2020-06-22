# -*- coding: UTF-8 -*- 
"""XhjTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [
    # path matches.
    # path('', ),

    # 订单相关的路由导航
    path('index',views.index,name="index"),
    path('getTrade',views.getTradeInfo,name="getTrade"),
    path('getV2',views.getV2,name="getTrade"),           # 获取订单信息接口2.0
    path('changeV2',views.changeV2,name="changeV2"),            # 更改订单信息接口2.0
    path('otherapis',views.otherapis,name="otherapis"),
    # re_path(r'^$',views.index)

    # 创建订单相关路由导航地址：
    path('runflow',views.runflow,name="runflow"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),


    # erp系统相关的路由导航：
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    

    # ApiautoTestUtils系统相关的路由导航
    path('apitest',views.apitest,name="apitest"),
    path('gettscases',views.gettscases,name="gettscases"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),
    # path('stock',views.getTradeInfo,name="stock"),



    # 下载文件相关的路由导航
    path('downloads/<types>',views.downloads,name="stock"),
]
