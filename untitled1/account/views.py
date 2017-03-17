#coding=utf-8
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from account.models import User
import time
import pdb

def login(request): 
    if request.method == "POST":
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userResult = User.objects.filter(username=username,password=password)
            #pdb.set_trace()
            if (len(userResult)>0):
                return render_to_response('success.html',{'operation':"登录"})
            else:
                return HttpResponse("该用户不存在")
    else:
        uf = UserFormLogin()
    return render_to_response("login.html", {'uf':uf})

def register(request):
    curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            #pdb.set_trace()
            #try:
            filterResult = User.objects.filter(username = username)
            if len(filterResult)>0:
                return render_to_response('register.html',{"errors":"用户名已存在"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render_to_response('register.html',{'errors':errors})
                    #return HttpResponse('两次输入的密码不一致!,请重新输入密码')
                password = password2
                email = uf.cleaned_data['email']
                #将表单写入数据库
                #user = User.objects.create(username=username,password=password1)
                user = User(username=username,password=password,email=email)
                user.save()
                #pdb.set_trace()
                #返回注册成功页面
                return render_to_response('success.html',{'operation':"注册"})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')

class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())