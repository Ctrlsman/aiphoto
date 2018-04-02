# -*- coding:utf8 -*-
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return render(request, 'index.html')


def wenhua(request):
    '''
    品牌文化页面
    :param request:
    :return:
    '''
    return HttpResponse('wenhua')


def news(request):
    '''
    新闻活动
    :param request:
    :return:
    '''
    return HttpResponse('新闻')


def case(request):
    '''
    新婚摄影
    :param request:
    :return:
    '''
    return HttpResponse('新婚摄影')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        pass


def register(request):
    return HttpResponse('register')