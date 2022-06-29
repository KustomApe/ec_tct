from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
import logging

# Create your views here.

logger = logging.getLogger('login') # loggerを指定

def index(request):
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        password = request.POST['password1']
        pass_len = len(password)
        user_data = {
            'password' : request.POST['password1'],
        }
        if register_form.is_valid():
            user_id = register_form.cleaned_data.get('id')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            return render(request, 'account/registerUserConfirm.html')
        return render(request, 'account/registerUser.html')
    return render(request, 'account/registerUser.html')
