from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
import logging

# Create your views here.

logger = logging.getLogger('login') # loggerを指定

def index(request):
    return redirect('/')

def login(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            user = models.User.objects.get(user_id=user_id)
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.name
                return redirect('/')
            else:
                return redirect('/account/login/')
        return redirect('/account/login/')

    form = forms.UserForm()
    context = {
        'form': form,
    }
    return render(request, 'account/login.html', context)

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')
    request.session.flush()
    return redirect('/account/login/')


def register_user(request):
    if request.session.get('is_login', None): #ログインしていない状態確認
        return redirect('/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "入力した内容を再度確認してください"
        if register_form.is_valid(): #form検査
            user_id = register_form.cleaned_data.get('id')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            name = register_form.cleaned_data.get('name')
            address = register_form.cleaned_data.get('address')
            if password1 != password2:
                message = '二回入力されたパスワードが一致しません。'
                return render(request, 'account/registerUser.html', locals())
            else:
                same_id_user = models.User.objects.filter(user_id=user_id)
                if same_id_user:
                    message = 'この会員IDが登録済です。'
                    return render(request, 'account/registerUser.html', locals())
                return render(request, 'account/registerUserConfirm.html', locals())
        else:
            return render(request, 'account/registerUser.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'account/registerUser.html', locals())

def register_user_commit(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_id = register_form.cleaned_data.get('id')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            name = register_form.cleaned_data.get('name')
            address = register_form.cleaned_data.get('address')
            new_user = models.User()
            new_user.user_id = user_id
            new_user.password = password1
            new_user.name = name
            new_user.address = address
            new_user.save()
            request.session['is_login'] = True
            request.session['user_id'] = new_user.user_id
            request.session['user_name'] = new_user.name
            return render(request, 'account/registerUserCommit.html')
        else:
            return render(request, 'account/registerUser.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'account/registerUser.html', locals())

def user_info(request):
    if not request.session.get('is_login', None):
        return redirect("/account/login/")
    user_id = request.session['user_id']
    user = models.User.objects.get(user_id=user_id)
    id = user_id
    name = user.name
    address = user.address
    register_form = forms.RegisterForm()
    return render(request, 'account/userInfo.html', locals())

def update_user(request):
    if not request.session.get('is_login', None):
        return redirect("/account/login/")
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('id')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')

    
    # 現状DBに登録されているユーザー情報を取得してフォームとして表示させる
    user_id = request.session['user_id']
    user = models.User.objects.get(user_id=user_id)
    data = {
        'user_id': user.user_id,
        'name': user.name,
        'password': user.password,
        'password2': user.password2,
        'address': user.address,
    }
    form = forms.RegisterForm(data)
    context = {
        'form': form,
    }
    return render(request, 'accout/updateUser.html', context)