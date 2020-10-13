from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . import models
from . import forms
import hashlib
from iyb.models import WorkTimes, Function
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage
import os
from MyWeb import settings


def hash_code(s, salt='MyWeb'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 主页
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/iybsite/')
    return render(request, 'iybsite/index.html')


# 登录
def login(request):
    # 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        '''username = request.POST.get('username')
        password = request.POST.get('password')'''
        # 使用表单验证
        login_form = forms.UserForm(request.POST)
        # message = '请检查填写的内容'
        # 用户名&密码为空校验
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.UserInfo.objects.get(name=username)
            except:
                message="!!!该用户不存在"
                return render(request,'login/login.html',locals())

            if user.password == hash_code(password):
                # 向session字典写入用户状态和数据
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码错误'
                return render(request,'login/login.html',locals())
        else:
            return render(request,'login/login.html',locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html')


# 注册
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        #message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.UserInfo.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.UserInfo.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.UserInfo()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


# 退出
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect("/login/")