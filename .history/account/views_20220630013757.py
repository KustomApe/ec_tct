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
    pass

def update_user(request):
    if request.method == 'POST':
        form = forms.RegisterUsers(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']

            context = {
                'form' : form,
                'user_id' : user_id,
                'password' : password,
                'password2' : password2,
                'name' : name,
                'address' : address,
            }
            return render(request,'account/updateUserConfirm.html',context)

    else:
        user_id = request.session['user_id']

        target_user = models.User.objects.get(pk = user_id)

        target_id = target_user.user_id

        disc ={
            'user_id' : target_user.user_id,
            'name' : target_user.name,
            'password' : target_user.password,
            'password2' : None,
            'address' : target_user.address,
        }

        form = forms.RegisterUsers(disc)

        context = {
            'form' : form,
            'target_id' : target_id,
        }

        return render(request,'account/updateUser.html',context)


