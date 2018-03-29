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


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        pass


def register(request):
    return HttpResponse('register')